import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import csv
urls=[]
title_l=[]
Main_details_l=[]
featured_aminities_l=[]
entertainment_aminities_l=[]
indoor_l=[]
outdoor_l=[]
additional_l=[]
description_l=[]
price_date_l=[]
price_cost_l=[]
location_l=[]
cookies = {
    'has_js': '1',
    '_gcl_au': '1.1.1735123174.1670740775',
    '_ga': 'GA1.1.1206315740.1670740775',
    '_gid': 'GA1.2.1418374326.1670740775',
    '_gat': '1',
    '__smVID': '6e1402b4d559f94ecdf61c4fb5c4c8c70ff07360b3774bb5f2bdcead5bc5d0e2',
    '_ga_1XBH53MH72': 'GS1.1.1670740776.1.1.1670740797.0.0.0',
    '_kdd_ses.656f': '*',
    '_kdd_id.656f': '4057d2c9-0b99-4b9f-888a-6765e87652fc.1670740777.1.1670740798.1670740777.4a2065de-f4e8-4c30-8568-5dba7b2cb9be',
    '__smToken': 'IF9pA5wEgTeH5mhneYf0JOqP',
    '__smSmartbarShown': 'Sun%20Dec%2011%202022%2011:39:41%20GMT+0500%20(Pakistan%20Standard%20Time)',
    '_fbp': 'fb.1.1670740783154.1276180586',
    '_hjSessionUser_850673': 'eyJpZCI6ImM0ZDE2YjJiLWMzNGQtNTAxOC05ZmMxLWNmNzY3ZTY3Y2JmNSIsImNyZWF0ZWQiOjE2NzA3NDA3ODMzODUsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample': '0',
    '_hjSession_850673': 'eyJpZCI6IjJiNTk0NjM3LWY5NzQtNDNiMi1hMGNhLTc3YmUyMDk1Y2E5ZCIsImNyZWF0ZWQiOjE2NzA3NDA3ODMzOTYsImluU2FtcGxlIjpmYWxzZX0=',
    '_hjIncludedInPageviewSample': '1',
    '_hjAbsoluteSessionInProgress': '1',
    '__smScrollBoxShown': 'Sun%20Dec%2011%202022%2011:39:45%20GMT+0500%20(Pakistan%20Standard%20Time)',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.beachrealtync.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.beachrealtync.com/duck-rentals',
    # 'Cookie': 'has_js=1; _gcl_au=1.1.1735123174.1670740775; _ga=GA1.1.1206315740.1670740775; _gid=GA1.2.1418374326.1670740775; _gat=1; __smVID=6e1402b4d559f94ecdf61c4fb5c4c8c70ff07360b3774bb5f2bdcead5bc5d0e2; _ga_1XBH53MH72=GS1.1.1670740776.1.1.1670740797.0.0.0; _kdd_ses.656f=*; _kdd_id.656f=4057d2c9-0b99-4b9f-888a-6765e87652fc.1670740777.1.1670740798.1670740777.4a2065de-f4e8-4c30-8568-5dba7b2cb9be; __smToken=IF9pA5wEgTeH5mhneYf0JOqP; __smSmartbarShown=Sun%20Dec%2011%202022%2011:39:41%20GMT+0500%20(Pakistan%20Standard%20Time); _fbp=fb.1.1670740783154.1276180586; _hjSessionUser_850673=eyJpZCI6ImM0ZDE2YjJiLWMzNGQtNTAxOC05ZmMxLWNmNzY3ZTY3Y2JmNSIsImNyZWF0ZWQiOjE2NzA3NDA3ODMzODUsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_850673=eyJpZCI6IjJiNTk0NjM3LWY5NzQtNDNiMi1hMGNhLTc3YmUyMDk1Y2E5ZCIsImNyZWF0ZWQiOjE2NzA3NDA3ODMzOTYsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; __smScrollBoxShown=Sun%20Dec%2011%202022%2011:39:45%20GMT+0500%20(Pakistan%20Standard%20Time)',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = 'ids=maqfd5-rci-47,maqfd5-rci-52,maqfd5-rci-54,maqfd5-rci-62,maqfd5-rci-66,maqfd5-rci-68,maqfd5-rci-71,maqfd5-rci-75,maqfd5-rci-76,maqfd5-rci-79,maqfd5-rci-80,maqfd5-rci-87,maqfd5-rci-88,maqfd5-rci-91,maqfd5-rci-95,maqfd5-rci-101,maqfd5-rci-103,maqfd5-rci-111,maqfd5-rci-118,maqfd5-rci-133,maqfd5-rci-140,maqfd5-rci-164,maqfd5-rci-237,maqfd5-rci-246,maqfd5-rci-301,maqfd5-rci-304,maqfd5-rci-309,maqfd5-rci-310,maqfd5-rci-311,maqfd5-rci-318,maqfd5-rci-321,maqfd5-rci-325,maqfd5-rci-379,maqfd5-rci-389,maqfd5-rci-391,maqfd5-rci-393,maqfd5-rci-399,maqfd5-rci-409,maqfd5-rci-432,maqfd5-rci-487,maqfd5-rci-488,maqfd5-rci-492,maqfd5-rci-495,maqfd5-rci-505,maqfd5-rci-523,maqfd5-rci-559,maqfd5-rci-567,maqfd5-rci-575,maqfd5-rci-623,maqfd5-rci-628,maqfd5-rci-630,maqfd5-rci-648,maqfd5-rci-652,maqfd5-rci-653,maqfd5-rci-658,maqfd5-rci-670,maqfd5-rci-684,maqfd5-rci-687,maqfd5-rci-689,maqfd5-rci-711,maqfd5-rci-718,maqfd5-rci-731,maqfd5-rci-734,maqfd5-rci-744,maqfd5-rci-300,maqfd5-rci-119,maqfd5-rci-679,maqfd5-rci-508,maqfd5-rci-558&wt=json&json.wrf=jQuery110209409870599692013_1670740796762&fq=index_id:rci'

response = requests.post('https://www.beachrealtync.com/solr/', cookies=cookies, headers=headers, data=data)
response_text=response.text[42:-2]
count=response_text.count('ss_url')
print(count)
response_json=json.loads(response_text)
i=0
url1=[]
while(i < int(count)):
    url=response_json['response']['docs'][i]['ss_url']
    i+=1
    url1.append(url)
    urls.append(url1)
    url1=[]
    # print(url)
print(urls)
header = ['urls']
with open('urls .csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(urls)   