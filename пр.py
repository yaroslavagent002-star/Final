import requests
from bs4 import BeautifulSoup as bs

class Coin:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        self.soup = None
        self.car = []

    def auditSite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
            return True
        print("Не вдалося підключитися до сайту")
        return False


      def getInfo(self):  # парсинг даних (зчитування необхідної інфи)
            coin = []
            table = self.soup.find("tbody")
            if not table:
                print('Не знайдено таблицю')
                return coin

rows = table.find_all('tr')[0:10]  # 0 1 2 3 4 5 6 7 8 9
for i in rows:
    name = i.find('p', class_="coin-item-name")
    nameCoin = name.text if name else 'Назва відсутня'
    price = i.find('div', class_="eAphWs")
    priceCoin = price.text if price else 'Ціна відсутня'

    coin.append({
        'name': nameCoin,
        'price': priceCoin
    })
url="https://coinmarketcap.com/"
obj=CoinMarketCap(url)
obj.auditSite()
site=obj.getInfo()
if site: obj.showInfo()
else:print("Жодної інформації не отримано з сайту")