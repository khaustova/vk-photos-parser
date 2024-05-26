import vk_api
import json
import os
import urllib
import urllib.request
import ssl 
from configuration import config

ssl._create_default_https_context = ssl._create_unverified_context

token = config.token.get_secret_value()

owner_id = -220740378

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

photos = vk.photos.get(owner_id=owner_id, album_id='wall', photo_sizes=1, count=200)
count = 0

images_path = 'images'
if not os.path.exists(images_path):
    os.makedirs(images_path)

path = os.getcwd() + '/images'

for photo in photos['items']:
    max_size_photo = sorted(photo['sizes'], key=lambda dict: dict['height'])
    url = max_size_photo[-1]['url']
    name = f'{path}/{count}.jpg' 
    urllib.request.urlretrieve(url, name)
    count += 1
    
# with open('data.json', 'w') as fp:
#     fp.write(json.dumps(photos))
