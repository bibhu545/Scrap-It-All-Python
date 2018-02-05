from bs4 import BeautifulSoup
import requests


base_url = "https://www.compareraja.in"


def get_item_details(url):
    source = requests.get(url)
    code = source.text
    soup = BeautifulSoup(code, "html.parser")
    sites = {}
    for stores in soup.findAll("div", {"class": "topmerchant"}):
        for redirect in stores.findAll("li"):
            link = redirect.find("a")

            if str(link.get("href")).startswith('#'):
                continue

            site_link = link.get("href")
            site_brand = []
            brand = redirect.find("span")
            if brand != None:
                site_brand = brand.get("class")[0]
            sites.update({site_brand:site_link})

        print("-----------------------------------------------------")
    return sites


def get_categorys(url):
    subjects = {}
    code = requests.get(url)
    source = code.text
    soup = BeautifulSoup(source, "html.parser")
    navigation = {}

    for items in soup.findAll("ul", {"class": "nav"}):
        for items_text in items.findAll("a"):
            navigation.update({items_text.text.strip(): items_text.get("href")})

    for categories in soup.findAll("div",{"class":"home-pop-cate"}):
        for left_cat in categories.findAll("div",{"class":"leftcon"}):
            name = left_cat.find("a")
            print(name.text.strip()+"--->"+name.get("href"))
            for subcat in left_cat.findAll("li"):
                if subcat != None:
                    a_link = subcat.find("a").get("href")
                    print(str(subcat.string).replace("\\s","",200).strip() +"   "+a_link)
            print("--------------")
    return navigation


# get_categorys(base_url)
def all_categories(url="https://www.compareraja.in/all-categories.html"):
    code = requests.get(url)
    source = code.text
    soup = BeautifulSoup(source, "html.parser")
    for items in soup.findAll("div",{"class":"allcategories"}):
        main = items.find("h2").text
        for li in items.findAll("li"):
            print(li.text+"-->"+li.find("a").get("href"))
        print('---------------------')

all_categories()

def get_item_list(url):
    code = requests.get(url)
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

            print("------------------------------------")


def get_category_items(item_name,nav_items):
    for k,v in nav_items.items():
        if k == item_name:
            get_item_list(v)
