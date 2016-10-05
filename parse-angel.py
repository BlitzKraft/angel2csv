#! /usr/bin/python
# -*- coding: utf-8 -*-
import bs4 as bs
import csv

input_html = "Yes List - AngelList.html"
out_csv = "out.csv"

page = bs.BeautifulSoup(open(input_html),"html.parser")

a = page.findAll("div", {"class" : "browse_startups_table_row"})

out = []
for s in a:
    company = s.find("a", {"class" : "startup-link"})
    titles = s.findAll("div", {"class" : "collapsed-title"})
    comp = s.findAll("div", {"class": "compensation" }) 
    for jt, co in zip(titles, comp):
        o = []
        o.append(company.text.strip('\n'))
        o.append(jt.text.strip('\n'))
        for each in co.text.strip('\n').split(u' \xb7 '):
            o.append(each)
        out.append(o)

outfile = open(out_csv, 'wb')
for each in out:
    wr = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    try:
        wr.writerow(each)
    except:
        UnicodeEncodeError

