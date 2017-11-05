#! /usr/bin/env python3
from imgur_client import fetch_popular_memes as imgur
from mrisa_interface import identify_image as mrisa
from google_trends_client import pytrends_test as geo
import json

if __name__ == '__main__':
    memes = imgur.top_10('week')
    ids = mrisa.get_names(memes)
    geo.find_and_dump_geos('now 7-d', ids)  
