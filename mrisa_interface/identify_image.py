#! /usr/bin/env python3

import os, requests, sys, json

mrisa_url = 'http://localhost:5000/search'

def get_name(image):
    r = requests.post(mrisa_url, json={'image_url':image})
    resp = json.loads(r.text)
    if 'best_guess' in resp:
        return resp['best_guess']
    else:
        return None

if __name__ == '__main__':
    print(get_name(sys.argv[1]))




