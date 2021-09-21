import lxml
from lxml import html, etree
import requests
import csv

page = requests.get("https://www.macrotrends.net/countries/PAK/pakistan/population-growth-rate")
#print(page.content)
#input()
extractedHtml = lxml.html.fromstring(page.content)
#print(extractedHtml)
#input()
#bookTitle = extractedHtml.xpath("/html/body/center/h1")
#table_header = extractedHtml.xpath('//table[@class="historical_data_table table table-striped table-bordered"]/thead/tr/th//text()')
#print(table_header)
#input()
table_data = extractedHtml.xpath('//table[@class="historical_data_table table table-striped table-bordered"]/tbody/tr/td//text()')
#print(table_data)
#input()
#tbody = table.xpath('//thead/tr/td//text()')
#print("tbody")
#headers_list = []
one_day_data = []
row_data = []
#print(table_data)
#input()

#for row in range(0, len(table_header)):
#    headers_list.append(table_header[row])
#one_day_data.append(headers_list)

count =0

for row in range(0, len(table_data)):
    row_data.append(table_data[row])
    count = count+1
    #print(count)
    #print(row_data)
    #input()
    if count==3:
        one_day_data.append(row_data)
        row_data=[]
        count=0
        #print(one_day_data)
        #print(count)
        #input()


print(one_day_data)
file = open('pop.csv', 'a+', newline ='')
with file:
    write = csv.writer(file)
    write.writerows(one_day_data)