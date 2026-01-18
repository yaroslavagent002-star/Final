import requests
from bs4 import BeautifulSoup as bs


class Coin:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
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
            print("Помилка парсингу: таблицю не знайдено")
            return coin

        rows = table.find_all("tr")
        if not rows:
            print("Помилка парсингу: рядки не знайдено")
            return coin
        for row in rows:
            cols = row.find_all("td")
            if not cols:
                print("Помилка парсингу: таблицю не знайдено")
                return coin
            if len(cols) < 3:
                continue

            name = cols[0].text.strip()

            buy_text = cols[1].text.strip().replace(",", ".")
            sell_text = cols[2].text.strip().replace(",", ".")
            buy = float(buy_text.split('.')[0] + '.' + buy_text.split('.')[1][:2])
            sell = float(sell_text.split('.')[0] + '.' + sell_text.split('.')[1][:2])



            coin.append({
                "name": name,
                "buy": buy,
                "sell": sell
            })

            #if len(coin) == 5:
            #    break

       # self.coin_data = coin
        return coin

    def showInfo(self, coin):
        index = 1
        for i in coin:
            print(index)
            print("Назва:", i["name"])
            print("Купівля:", i["buy"], "грн")
            print("Продаж:", i["sell"], "грн")
            print("-* " * 30)
            index += 1


url = "https://minfin.com.ua/ua/currency/"
obj = Coin(url)

if obj.auditSite():
    site = obj.getInfo()

    if site:
        obj.showInfo(site)



        first = site[0]
        print ("Наипшить в гривнях суму на яку ви хочете купити")
        amount = int(input())
        result = amount / first["sell"]
        print(f"\nЗа {amount} грн можна купити {round(result, 2)} {first['name']}")
    else:
        print("Жодної інформації не отримано з сайту")
else:
    print("Програму зупинено через помилку підключення.")
