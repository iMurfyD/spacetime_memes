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

def get_names(memes):
    names = list()
    for m in memes: # For now just pass in image from multiimage set 
        if len(m['images']) > 1:
            print(m['original link'])
            all_names = list()
            for img in m['images']: # Tries all images against google, picks best one
                all_names.append(get_name(img)) 
                print(all_names[-1]) # Print the most recent addition
                names.append(all_names[-1])
        else: # Only one image per set 
            names.append(get_name(m['images'][0]))
    return names 

if __name__ == '__main__':
    print(get_name(sys.argv[1]))




