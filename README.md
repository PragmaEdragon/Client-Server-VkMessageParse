# Client-Server-VkMessageParse

A tool for access and parsing offline and messages, with transmission to the server and after - scattering on users.

## Getting Started

To deploy the project, only 1 file should be launched, hinting at this - start_project.py. The script will do the rest for you :)

### Prerequisites

What things you need to install the software and how to install them

```
python root/<urpathhere>/start_project.py
```

### Installing

The main thing you need is to connect all the necessary libraries. If you are not running on a localhost, change the host and network connections accordingly.

```
class SocketServer(object):
    HOST = socket.gethostbyname('localhost')
    PORT = 65432
    # Need to change here
```

And repeat

```
class ClientSocket(object):
    HOST = socket.gethostbyname('localhost')
    PORT = 65432
    # Need to change here tho 
```

[+] Server started
New connection from: ('127.0.0.1', 53042)
{'Connection1': ('127.0.0.1', 53042)}
New connection from: ('127.0.0.1', 53043)
{'Connection1': ('127.0.0.1', 53042), 'Connection2': ('127.0.0.1', 53043)}
New connection from: ('127.0.0.1', 53044)
{'Connection1': ('127.0.0.1', 53042), 'Connection2': ('127.0.0.1', 53043), 'Connection3': ('127.0.0.1', 53044)}

[!]Your login: login
[!]Your password: password
Input your auth token here: token
Remember device? [Y]/[N]Y
[+]User Username:0 offline now.
[+]User  Username:0 offline now.
[+]User  Username:0 offline now.

[+]New message from: Username Text:
Мур
[+]User  Username:0 offline now.
[+]User  Username:0 offline now.


## Built With

* [vk_api](https://vk.com/dev/manuals) - The api used
* [socket](https://docs.python.org/3/library/socket.html) - Low-level networking interface
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used to parse data


## Authors

* **r1v3n** - [PragmaEdragon](https://github.com/PragmaEdragon)

![MoreCmds](https://i.imgur.com/nKwswHg.jpg)
