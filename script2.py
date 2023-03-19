import requests
import pandas as pd
bath_l=[]
Bedroom_l=[]
title_l=[]
display_sub_l=[]
id_l=[]
availibility_weeks_l=[]
price_per_week_l=[]
average_price_l=[]
image_url_l=[]
Beds_m=[]
TopAmenities_m=[]
ovrview_m=[]
interior_m=[]
exterior_m=[]
other_m=[]
availibility_weeks_m=[]
price_per_week_m=[]
average_price_m=[]
images_url_m=[]
headers = {
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

response = requests.get(
    'https://siteservice.carolinadesigns.com/websiteservice.svc/10000/32/website/searchresults/33/d?{%22searchType%22:%2233%22}',
    headers=headers,
)
# print(len(response.json()['DdlPropname']))

count=len(response.json()['Results'])
h=0
while( h<count):
    id=response.json()['Results'][h]['Propid']
    # print(id)
    id_l.append(id)
    h+=1
print(id_l)
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


i=0

print(id_l[0])
while( i<count):
    response1 = requests.get(
    f"https://siteservice.carolinadesigns.com/websiteservice.svc/10000/32/website/properties/d/{(id_l[i])}",
    headers=headers1,
    )
    json_text=response1.json()
    bath=response.json()['Results'][i]['Baths']
    print(bath)
    bath_l.append(bath)
    Beds=response.json()['Results'][i]['BedTypeList']
    print(Beds)
    Bedroom=response.json()['Results'][i]['Bedrooms']
    print(Bedroom)
    Bedroom_l.append(Bedroom)
    title=response.json()['Results'][i]['Propname']
    print(title)
    title_l.append(title)
    TopAmenities=response.json()['Results'][i]['TopAmenities']
    print(TopAmenities)
    DisplaySub=response.json()['Results'][i]['DisplaySub']
    display_sub_l.append(DisplaySub)
    print(DisplaySub)
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
    if (len(price_length) >0):
        f=0
        while(f<len(price_length)):
            availibility_weeks=json_text['Weeks1CurrAvail'][f]['DisplayText']
            print(availibility_weeks)
            availibility_weeks_l.append(availibility_weeks)
            price_per_week=json_text['Weeks1CurrAvail'][f]['Orate']
            print(price_per_week)
            price_per_week_l.append(price_per_week)
            average_price=json_text['Weeks1CurrAvail'][f]['CostPerNight']
            print(average_price)
            average_price_l.append(average_price)
            f+=1
    else:
            price_length=len(json_text['Weeks1NextAvail'])
            f=0
            while(f<price_length):
                availibility_weeks=json_text['Weeks1NextAvail'][f]['DisplayText']
                print(availibility_weeks)
                availibility_weeks_l.append(availibility_weeks)
                price_per_week=json_text['Weeks1NextAvail'][f]['Rate']
                print(price_per_week)
                price_per_week_l.append(price_per_week)
                average_price=json_text['Weeks1NextAvail'][f]['CostPerNight']
                print(average_price)
                average_price_l.append(average_price)
                f+=1

    image_url=json_text['Pics']
    print(len(image_url))
    n=0
    leng=len(image_url)
    while(n<leng):
        image_url=json_text['Pics'][n]['ImgUrl']
        image_url_l.append(image_url)
        n+=1

    Beds_m.append(Beds)
    TopAmenities_m.append(TopAmenities)
    ovrview_m.append(overview)
    interior_m.append(interior)
    exterior_m.append(exterior)
    other_m.append(other_feature)
    availibility_weeks_m.append(availibility_weeks_l)
    price_per_week_m.append(price_per_week_l)
    average_price_m.append(average_price_l)
    images_url_m.append(image_url_l)
    if (i!=count-1):
        price_per_week_l=[]
        availibility_weeks_l=[]
        image_url_l=[]
        average_price_l=[]
    i+=1

print(images_url_m)
print("here is teh amenier")
print(TopAmenities_m)
A=pd.DataFrame({'Title': title_l})
B=pd.DataFrame({'Baths': bath_l})
C=pd.DataFrame({'Beds':Beds_m})
D=pd.DataFrame({'Bedroom':Bedroom_l})
E=pd.DataFrame({'Top Amentiess':TopAmenities_m})
F=pd.DataFrame({'Disply sub':display_sub_l})
G=pd.DataFrame({'Availability Weeks':availibility_weeks_m})
H=pd.DataFrame({'Overview':ovrview_m})
I=pd.DataFrame({'Interior':interior_m})
J=pd.DataFrame({'Exterior':exterior_m})
K=pd.DataFrame({'Other':other_m})
Y=pd.DataFrame({'Price per week':price_per_week_m})
Z=pd.DataFrame({'Average Price':average_price_m})
ZZ=pd.DataFrame({'Images URl':images_url_m})
pd.concat([A,B,C,D,E,F,H,I,J,K,G,Y,Z,ZZ],axis=1).to_csv('main_data.csv', index = True)