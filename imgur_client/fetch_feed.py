#! /usr/bin/env python


from imgurpython import ImgurClient



client_id = '0f354899f3c1841'

client_secret = '771df959e3b381b5035854dbad02f226abb81ba1'



client = ImgurClient(client_id, client_secret)



# Example request

items = client.memes_subgallery(sort='viral', page=0)

for item in items:

    print(item.link)
