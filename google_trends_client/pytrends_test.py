#! /usr/bin/env python3
from pytrends.request import TrendReq
import json, os, sys

def find_geos(tf, phrase):
	pytrends = TrendReq(hl='en-US', tz=360)
	pytrends.build_payload([phrase], cat=0, timeframe='now 7-d', geo='', gprop='')
	print(type(pytrends.interest_by_region(resolution='COUNTRY')))
	return pytrends.interest_by_region(resolution='COUNTRY')

def find_and_dump_geos(tf, phrases):
    print(phrases)
    print(tf)
    fh = open('data.json', 'a')
    for phrase in phrases:
        print(phrase)
        if len(phrase) < 20:
            try:
                geos = find_geos(tf,phrase)
                data = geos.to_json()
                fh.write(data)
            except:
                print("Fucked up")
    fh.close() 
    return 1

if __name__ == '__main__':
	kw_list = ['Normie Memes', 'reposts', 'weirdest thing done sexually', 'cat face against floor']
	print(find_and_dump_geos('now 7-d', kw_list))
