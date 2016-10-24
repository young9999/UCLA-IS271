#Yang Guo

from pymarc import MARCReader
import csv

marc = open('marc_sample.mrc', 'rb')
reader = MARCReader(marc)
records = [rec for rec in reader]
#print(records)
length = len(records)
title = []
pubyear = []
url = []
callnum = []
for n in range(0,length):
    item1 = str(records[n]['245']['a']) + str(records[n]['245']['b'])#.title()
    title.append(item1)
    item2 = records[n]['260']['c']
    pubyear.append(item2)
    item3 = records[n]['856']['u']
    url.append(item3)
    field = records[n]['090']
    if not field == None:
        string = field.format_field()
    else:
        string = ''
    callnum.append(string)

with open('marc_data.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['title','pubyear','url','callnum'])
    writer.writerows(zip(title,pubyear,url,callnum))
