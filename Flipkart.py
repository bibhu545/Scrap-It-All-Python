from bs4 import BeautifulSoup
import requests

base_url = "https://www.compareraja.in"
subjects = {}
code = requests.get(base_url)
source = code.text
soup = BeautifulSoup(source,"html.parser")
navigation = {}
for items in soup.findAll("ul",{"class":"nav"}):
    for items_text in items.findAll("a"):
        navigation.update({items_text.text.strip():items_text.get("href")})

print(navigation)

mobiles = navigation['Mobiles']
print(mobiles)
print()

code = requests.get(mobiles)
source = code.text
soup = BeautifulSoup(source,"html.parser")
for products in soup.findAll("div",{"class":"prodcut-listing"}):
    for product in products.findAll('article',{"class":"product"}):
        a = product.find('a',{"class":"db"})
        print(a.get("href"))
        img = product.find('img')
        print(img.get("src"))
        price = product.find("b")
        print(price.text.strip())
        star = product.find("div",{"class":"bxStr"})
        print(star.text.strip())
        summery = product.find("ul",{"class":"sumery"})
        for li in summery.findAll("li"):
            print(str(1)+li.text)
        # print(product.text.split("   "))
        print("------------------------------------")

url = "https://www.compareraja.in/apple-iphone-8-plus-64-gb-price.html"
source = requests.get(url)
code = source.text
soup = BeautifulSoup(code,"html.parser")
for stores in soup.findAll("div",{"class":"topmerchant"}):
    for redirect in stores.findAll("li"):
        link = redirect.find("a")
        if str(link.get("href")).startswith('#'):
            continue
        print(link.get("href"))
        brand = redirect.find("span")
        if brand != None:
            # print(brand)
            print(brand.get("class")[0])
    print("-----------------------------------------------------")