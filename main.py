import vk_api
import json
import os
import urllib.request
import ssl 
from configuration import config

ssl._create_default_https_context = ssl._create_unverified_context


class Parser():
    
    def __init__(self):
        self.token = config.token.get_secret_value()
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
        self.count = 0
        self.offset = 0
        
    def parsing(self, owner_id=-220740378):
        images_folder = 'images'
        
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
            
        path = os.getcwd() + '/' + images_folder
        
        while True:
            images = self.vk.photos.get(owner_id=owner_id, album_id='wall', photo_sizes=1, count=1000, offset=self.offset)
            
            for image in images['items']:
                max_size_photo = sorted(image['sizes'], key=lambda dict: dict['height'])
                url = max_size_photo[-1]['url']
                name = f'{path}/{self.count}.jpg' 
                urllib.request.urlretrieve(url, name)
                self.count += 1
                
            self.offset += 1000
            if self.offset >= images['count']:
                break


def main():
    parser = Parser()
    parser.parsing()
    

if __name__ == "__main__":
    main()
