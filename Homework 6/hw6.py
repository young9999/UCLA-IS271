#Yang Guo
import requests
import csv

url = 'http://api.dp.la/v2/items'
#url='http://api.dp.la/v2/items?q=Rene+Magritte&page_size=25&api_key=0cc7601df126f677a6a8a0a221c56363'
params = {}
params['q'] = 'Rene+Magritte'
params['api_key'] = '0cc7601df126f677a6a8a0a221c56363'
response = requests.get(url, params = params)
#print(response)
url = 'http://api.dp.la/v2/items?q=Rene+Magritte&page_size=25&api_key=0cc7601df126f677a6a8a0a221c56363'
params['page_size'] = 25
data = response.json()
#print(data)

#data.keys()

docs = data['docs']
len(docs)

title_ = []
for doc in docs:
    title = doc['sourceResource']['title']
    if type(title) == list:
        title = title[0]
    title_.append(title)

date_ =[]
for doc in docs:
    date = doc['sourceResource']['date']
    date = date['displayDate']
    if type(date) == list:
        date = date[0]
    date_.append(date)

creator_ = []
for doc in docs:
    creator = doc['sourceResource'].get('creator', 'Anonymous')
    if type(creator) == list:
        creator = creator[0]
    creator_.append(creator)


with open('rene_magritte.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(zip(title_, date_, creator_))
