# import requests #запит HTTP
# from bs4 import BeautifulSoup as bs #робота з HTML
#
# class Name:
#     def __init__(self, url):
#         self.url = url
#         self.header = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#
#     def auditSite(self): #завантеження запиту на спробу парсингу
#         response = requests.get(self.url, headers=self.header)#відправка GET запиту
#         if response.status_code == 200:
#             self.soup = bs(response.text, "html.parser")
#         else:
#             print("Не вдалося підключитися до сайту")
#
#     def getInfo(self): #парсинг даних (зчитування необхідної інфи)
#         pass
#
#     def showInfo(self):
#         pass
#
# url="посилання на сайт"
# obj=Name(url)
# obj.auditSite()
# site=obj.getInfo()
# if site==True: obj.showInfo()
# else:print("Жодної інформації не отримано з сайту")

import requests
from bs4 import BeautifulSoup as bs


class AutoRia:
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

    def getInfo(self):
        if not self.soup:
            return False

        teg = self.soup.find_all("section", class_="proposition")

        for k in teg:
            name = k.find("h3", class_="proposition_name")
            link = k.find("a", class_="proposition_link")
            priceUSD = k.find("span", class_="size20 tooltip-price")
            city = k.find("span", class_="region")

            price_text = priceUSD.get_text(strip=True) if priceUSD else "0"
            price_num = int(''.join(i for i in price_text if i.isdigit()))

            self.car.append({
                "Назва": name.get_text(strip=True) if name else "Назви немає",
                "Посилання": link["href"] if link else "Немає посилання",
                "Ціна $": price_text,
                "Ціна_число": price_num,
                "Місто": city.get_text(strip=True) if city else "Невідомо"
            })

        return True

    def sortPrice(self, limit=5):
        self.car.sort(key=lambda x: x["Ціна_число"], reverse=True)
        self.car = self.car[:limit]

    def showInfo(self):
        if not self.car:
            print("Дані по авто не знайдено")
            return

        for car in self.car:
            print(car)


url = "https://auto.ria.com/uk/newauto/marka-jeep/"
obj = AutoRia(url)

if obj.auditSite() and obj.getInfo():
    obj.sortPrice(5)
    obj.showInfo()
else:
    print("Жодної інформації не отримано з сайту")
