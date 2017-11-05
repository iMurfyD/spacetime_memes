#! /usr/bin/env python3
from pytrends.request import TrendReq
import json, os, sys

def find_geos(tf, phrases):
	pytrends = TrendReq(hl='en-US', tz=360)
	pytrends.build_payload(phrases, cat=0, timeframe='now 7-d', geo='', gprop='')
	print(type(pytrends.interest_by_region(resolution='COUNTRY')))
	return pytrends.interest_by_region(resolution='COUNTRY')

def find_and_dump_geos(tf, phrases):
    geos = find_geos(tf,phrases)
    data = geos.to_json()
    fh = open('data.json', 'w')
    fh.write(data)
    fh.close() 
    return geos

if __name__ == '__main__':
	kw_list = ['Normie Memes', 'reposts']
	print(find_and_dump_geos('now 7-d', kw_list))
