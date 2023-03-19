import requests
from bs4 import BeautifulSoup
headers1= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Authorization': 'Basic NzUyOTIxRUYtRjQzQS00Q0YyLUJCMEUtOUIwM0JGN0E5NDdE',
    'Origin': 'https://www.carolinadesigns.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.carolinadesigns.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response1 = requests.get(
    'https://siteservice.carolinadesigns.com/websiteservice.svc/10000/32/website/properties/d/162',
    headers=headers1,
)
json_text=response1.json()
overview=json_text['Sidebar'][0]['Items']
print(overview)
interior=json_text['Sidebar'][1]['Items']
print(interior)
exterior=json_text['Sidebar'][2]['Items']
print(exterior)
other_feature=json_text['Sidebar'][3]['Items']
print(other_feature)
price_length=json_text['Weeks1CurrAvail']
print(len(price_length))
f=0
while(f<len(price_length)):
    availibility_weeks=json_text['Weeks1CurrAvail'][0]['DisplayText']
    print(availibility_weeks)
    price_per_week=json_text['Weeks1CurrAvail'][0]['Rate']
    print(price_per_week)
    average_price=json_text['Weeks1CurrAvail'][0]['CostPerNight']
    print(average_price)
    f+=1
image_url=json_text['Pics']
print(len(image_url))
n=0
# with open('ll.csv','w') as f:
#     f.write(str(image_url))
a=len(image_url)

while(n < a):
    image_url=json_text['Pics'][n]['ImgUrl']
    print(image_url)
    print(n)
    n+=1

# page=requests.get("https://www.carolinadesigns.com/duck-vacation-rental/632-carolina-sunrise/")
# soup=BeautifulSoup(page.content,'html.parser')
# Main=soup.find(class_="main-section")
# print(page.text)
# print(Main)
# ground=soup.find('article')
# print(ground)
# for detail in ground:
#     print(detail.text)
# first=page.find(id="first").find_all('li')
# for detail in first:
#     print(detail.text)
# second=page.find(id="second").find_all('li')
# for detail in second:
    # print(detail.text)