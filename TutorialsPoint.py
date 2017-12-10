from bs4 import BeautifulSoup
import requests

base_url = "https://www.tutorialspoint.com/"

source = requests.get(base_url)
source_text = source.text
soup = BeautifulSoup(source_text,"html.parser")

title_list = []
def getTitle():
    for title_div in soup.find_all("div",class_ = "row featured-boxes"):
        for title in title_div.find_all("div",{"class":"featured-box"}):
            for title_text in title.find_all("h4"):
                title_list.append(title_text.text)

library = {}

def getLibrary():
    i = 0
    for ul in soup.find_all("ul",{"class":"menu"}):
        temp_dic = {}
        for a in ul.find_all("a"):
            temp_dic.update({a.text:a.get("href")})
        i+=1
        library.update({i:temp_dic})
    # for k,v in library.items():
    #     print("-----------------------------------------------------------------------------------------------------------------------------")
    #     print(title_list[k-1])
    #     print("-----------------------------------------------------------------------------------------------------------------------------")
    #     for in_k,in_v in v.items():
    #         print(str(in_k+"--->"+"https://www.tutorialspoint.com"+str(in_v)))

def getUrl(input_stream,input_topic):
    key_index = 0
    topic_url = ""
    for k, v in library[int(input_stream)].items():
        key_index += 1
        if key_index == int(input_topic):
            topic_url = "https://www.tutorialspoint.com" + v
            break
    return topic_url

def getContents(url):
    source = requests.get(url)
    source_text = source.text
    contents = {}
    soup = BeautifulSoup(source_text,"html.parser")
    for ul in soup.find_all("ul",class_ = "nav nav-list primary left-menu"):
        for li in ul.find_all("li",class_ = False):
            contents.update({li.text:li.find("a").get("href")})
    return contents
def get_key_topic_url():
    key_index = 1
    key_topic_url = ""
    for k, v in contents.items():
        if key_index == int(input_key_topic):
            key_topic_url = "https://www.tutorialspoint.com" + v
            break
        key_index += 1
    return key_topic_url

def getTutorial(url):
    source = requests.get(url)
    source_text = source.text
    contents = {}
    soup = BeautifulSoup(source_text, "html.parser")
    for contents in soup.findAll("div",class_ = "col-md-7 middle-col"):
        print(contents.text)


print("Welcome to TutorialsPoint.com")
print("-----------------------------------------------------------------------------------------------------------------------------")
getTitle()
print("Here are the list of subjects : ")
print("-----------------------------------------------------------------------------------------------------------------------------")
j=1
for i in title_list:
    print(str(j)+"--->"+i)
    j+=1
print("-----------------------------------------------------------------------------------------------------------------------------")
input_stream = input("What do u want to learn ? (index) : ")
while int(input_stream) > 25 or int(input_stream) <1:
    input_stream = input("Enter valid index please : ")
print("-----------------------------------------------------------------------------------------------------------------------------")

getLibrary()

x = 1
for key in library[int(input_stream)]:
    print(str(x)+" ---> "+key)
    x+=1
print("-----------------------------------------------------------------------------------------------------------------------------")

input_topic = input("Enter one topic : (index) : ")
# print(len(library[int(input_stream)]))
while int(input_topic) > len(library[int(input_stream)]) or int(input_topic) <1:
    input_topic = input("Enter valid index please : ")
print("-----------------------------------------------------------------------------------------------------------------------------")
url = getUrl(input_stream,input_topic)
key_index = 1
contents = getContents(url)
for k,v in contents.items():
    print(str(key_index)+" ---> "+k)
    key_index += 1
print("-----------------------------------------------------------------------------------------------------------------------------")
input_key_topic = input("Enter one specific topic : (index) : ")
while int(input_key_topic) > len(contents) or int(input_key_topic) <1:
    input_key_topic = input("Enter valid index please : ")
print("-----------------------------------------------------------------------------------------------------------------------------")

key_topic_url = get_key_topic_url()
getTutorial(key_topic_url)