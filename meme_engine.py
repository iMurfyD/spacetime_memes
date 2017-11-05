#! /usr/bin/env python3
from imgur_client import fetch_popular_memes as imgur
from mrisa_interface import identify_image as mrisa

if __name__ == '__main__':
    memes = imgur.top_10('week')
    ids = mrisa.get_names(memes)
    print(ids)
    print("Meme engine confirmed")
    

