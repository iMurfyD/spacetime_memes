#! /usr/bin/env python


from imgurpython import ImgurClient



client_id = '0f354899f3c1841'

client_secret = '771df959e3b381b5035854dbad02f226abb81ba1'



client = ImgurClient(client_id, client_secret)

# Takes an imgurpython item and returns the id of the meme
# TODO makes this do something smarter (a real meme detection algorythm)
# Guessing the name of the meme also gets guesses later down the pipeline
def find_id(item):
    return item.title


def top_10(time):
    # Request for viral memes from past time 
    # value for time is expected to be 'week'
    items = client.memes_subgallery(sort='viral', page=0, window=time)
    ret = [dict() for i in range(10)] # Array of dicts - each a single meme entry
    i = 0;
    for item in items:
        if i == 10:
            break
        ret[i]['id'] = find_id(item)
        ret[i]['link'] = item.link
        i = i+1
    return ret

if __name__ == '__main__':
    memes = top_10('week')
    for m in memes:
        print(m['id'])

if __name__ == '__test_old__':
    timeframe = 'all' 
    search = 'e'


    # Request for viral memes from past timeframe
    items = client.memes_subgallery(sort='viral', page=0, window=timeframe)
    
    for item in items:
        if search in item.title:
            print(item.title)
            print(type(item.title))
            print(dir(item))
            print(item.link)
            print(item.section)
            print # Newline
