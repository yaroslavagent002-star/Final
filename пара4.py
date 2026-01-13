import requests
from bs4 import BeautifulSoup
class Name:
    def __init__(self, url):
        self.url = url
        self.haader = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

        }

        self.soup = None

def auditSite(self):
    response = requests.get(self.url, headers=self.header)
    if response.status_code == 200:
        self.soup = BeautifulSoup(response.text, "html.parser")
    else:
        print("Не вдалось підключиться до сайту")
        def getInfo(self):
            pass
        def showInfo(self):
            pass



url="посилання на сайт"
obj=Name(url)
obj.auditSite()
site=obj.getInfo()
if site==True: obj.showInfo()
else:print("Жодної інформації не отримано з сайту")

