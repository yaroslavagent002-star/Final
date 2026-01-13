import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


class Coin:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.soup = None
        self.coin_data = []

    def auditSite(self):
        try:
            response = requests.get(self.url, headers=self.header, timeout=10)
            response.raise_for_status()

            self.soup = bs(response.text, "html.parser")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Не вдалося підключитися до сайту: {e}")
            return False

    def getInfo(self):
        coin = []

        table = self.soup.find("tbody")

        if not table:
            print('Помилка парсингу: Не знайдено таблицю ')
            return coin

        rows = table.find_all('tr')[0:10]

        for i in rows:
            circulatingSupply = i.find("div", class_="circulating-supply-value")
            cirS = circulatingSupply.text if circulatingSupply else 'Відсутнє значення'
            name = i.find('p', class_="coin-item-name")
            nameCoin = name.text if name else 'Назва відсутня '
            price = i.find('div', class_="eAphWs")
            priceCoin = price.text if price else 'Ціна відсутня'
            coin.append({
                'cs': cirS,
                'name': nameCoin,
                'price': priceCoin
            })


        self.coin_data = coin
        return coin

    def showInfo(self, coin):
        index = 1
        for i in coin:
            print(f"{index}")
            print("Назва:", coin["name"])
            print("Ціна:", coin["price"])
            print("Circulating Supply:", coin["supply"])
            print("-* " * 40)
            index += 1


url = "https://coinmarketcap.com/"
obj = Coin(url)

if obj.auditSite():
    site = obj.getInfo()

    if site:
        obj.showInfo()
        obj.showInfo(site)
        bitcoin = site[0]['price']
        bit = float(bitcoin.replace('$', '').replace(',', ''))
        print('\nЦіна Bitcoin x2=', bit, '=', bit * 2)
    else:
        print("Жодної інформації не отримано з сайту")
else:
    print("Програму зупинено через помилку підключення.")
