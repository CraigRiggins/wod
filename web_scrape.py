import requests
from lxml import html
from datetime import date, timedelta as td
import couchdb

#begin_address = 'https://crossfit.com/workout'
begin = 'http://www.norcalcrossfit.com/sitemap.xml'

date_start = date(2002,1,1)
date_end = date(2015,12,31)
date = date_start

couch = couchdb.Server()
db = couch['workouts']

#use str(int) to convert integer to string for date iteration

while date < date_end:
    #get string values to build the url
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    
    if len(day) < 2:
        day = '0' + day

    if len(month) < 2:
        month = '0'+ month
        
    url = begin_address + '/' + year + '/' + month + '/' + day
    
    #parse page for contents
    print url
    page = requests.get(url)
    tree = html.fromstring(page.content)
    contents = tree.xpath('//div[@class="content"]/p/text()')
    workout = ""
    #print contents
    for word in contents:
        workout += word

    #print workout
    #store into couchdb
    doc = {'Date':str(date),'Workout': workout}
    #print doc
    db.save(doc)
    
    date += td(days=1)
    


#print(page.content)



#print contents


