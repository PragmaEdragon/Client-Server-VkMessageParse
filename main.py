import vk_api
import socket
from bs4 import BeautifulSoup
from vk_api.longpoll import VkLongPoll, VkEventType


class VkAuth(object):
    headers = {
        'Host': 'vk.com',
        'User - Agent': 'Mozilla / 5.0(X11;Linux x86_64;rv: 60.0) Gecko / 20100101 Firefox / 60.0',
        'Accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, * / *;q = 0.8',
        'Accept - Language': 'en - US, en; q = 0.5',
        'Accept - Encoding': 'gzip, deflate',
        'Upgrade - Insecure - Requests': '1'
    }

    def __init__(self, auth_token='',
                 login=None, password=None,
                 remember_device=None,
                 long_poll=None,
                 vk_session=None):
        self.login = login
        self.password = password
        self.auth_token = auth_token
        self.remember_device = remember_device
        self.long_poll = long_poll
        self.vk_session = vk_session

    def auth_token_handler(self):
        self.auth_token = str(input("Input your auth token here: ")).strip(' ').strip('.')
        answr = str(input("Remember device? [Y]/[N]"))

        if answr == 'Y' or 'y':
            self.remember_device = True
        elif answr == 'N' or 'n':
            self.remember_device = False
        else:
            print("Cant understand you.")
            quit()

        return self.auth_token, self.remember_device

    def getDataFromUser(self):
        self.login = input("[!]Your login: ")
        self.password = input("[!]Your password: ")

        return self.login, self.password

    def login_with_token(self):
        try:
            self.getDataFromUser()
            self.vk_session = vk_api.VkApi(
                login=self.login,
                password=self.password,
                api_version='5.103',
                scope=vk_api.VkUserPermissions.MESSAGES | vk_api.VkUserPermissions.OFFLINE,
                app_id=2685278,
                auth_handler=self.auth_token_handler
            )
        except Exception:
            print("One of the parameters is wrong.")

        try:
            self.vk_session.auth()
        except Exception as error_message:
            print(error_message)

        self.long_poll = VkLongPoll(self.vk_session)


class WorkWithMessages(VkAuth):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostbyname('localhost'), 65432))

    def __init__(self, long_poll, vk_session):
        VkAuth.__init__(self, long_poll=long_poll,
                        vk_session=vk_session)

    def read_messages(self):
        for event in self.long_poll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                print()
                if not event.from_me:
                    WorkWithMessages.sock.send(bytes(f"[+]New message from: {self.soup(event.user_id)}. "
                                                     f"Text: \n{event.text}", 'utf-8'))
                    print(f"[+]New message from: {self.soup(event.user_id)}. Text: \n{event.text}")

            elif event.type == VkEventType.USER_OFFLINE:
                WorkWithMessages.sock.send(bytes(f"[+]User  {self.soup(event.user_id)}:{event.offline_type} offline now.",
                                                 'utf-8'))
                print(f"[+]User  {self.soup(event.user_id)}:{event.offline_type} offline now.")

    def soup(self, user_id):
        return BeautifulSoup(self.vk_session.http.request('GET', f'https://vk.com/id{user_id}').text, 'lxml').find('h1',{'class': 'page_name'}).text


user = VkAuth()
user.login_with_token()
messages = WorkWithMessages(user.long_poll, user.vk_session)
messages.read_messages()
# cd PycharmProjects\vk_bot_message_tool

