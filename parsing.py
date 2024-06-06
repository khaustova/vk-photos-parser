import vk_api
import ssl 
import json
import requests
import webbrowser
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context


class Parser:
    
    def __init__(self, token):
        self.token = token
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
           
    @staticmethod
    def get_token_url(line_edit_client_id):
        client_id = line_edit_client_id.text()
        params = {
            "client_id" : client_id,
            "scope" : "photos",
            "response_type" : "token",
            "display" : "page",
            "redirect_uri": "https://oauth.vk.com/blank.html",
            "v" : "5.236"
        }
        response = requests.get("http://oauth.vk.com/authorize/", params=params)
        
        webbrowser.open_new_tab(response.url)
        
    def get_total_photos(self, line_edit_group_id):
        owner_id = int(line_edit_group_id.text())
        total = self.vk.photos.get(owner_id=-owner_id, album_id="wall", count=0)["count"]
            
        return str(total)
        
    def check_token_url(self, token):
        params = {
            "access_token": token,
            "count": 1,
            "v": "5.236",
        }
        response = requests.get("https://api.vk.com/method/database.getCities/", params=params)
        content = json.loads(response.content)
        return True if content.get("response") else False
    
    def check_group_id(self, group_id):
        try:
            group_id = int(group_id)
        except:
            return False
        
        params = {
            "access_token": self.token,
            "owner_id": -group_id,
            "album_id": "wall",
            "count": 1,
            "v": "5.236",
        }
        response = requests.get("https://api.vk.com/method/photos.get/", params=params)
        content = json.loads(response.content)
        return True if content.get("response") else False
    
    def get_photos(self, group_id, album_id, count=None, offset=0):
        parsed_photos = []
        target = int(self.get_total_photos(group_id)) if not count else int(count)   
        count = 1000 if target > 1000 else count
        offset = offset if offset else 0

        while True:
            photos = self.vk.photos.get(
                owner_id=-group_id, 
                album_id=album_id, 
                photo_sizes=1, 
                count=count, 
                offset=offset)
            parsed_photos.extend(photos)
            offset += 1000
            
            if target <= offset:
                break

        return photos
    
    def get_albums(self, group_id):
        all_albums = self.vk.photos.getAlbums(owner_id = -group_id)
        
        albums = {}
        for album in all_albums["items"]:
            each_album = {}
            each_album["id"] = album["id"]
            each_album["title"] = album["title"]
            each_album["size"] = album["size"]
            name = f"{each_album.get('title')} ({each_album.get('size')})"  
            albums[name] = each_album

        return albums
    
    @staticmethod
    def save_photos(photos, path, step, thread):
        num = 1
        for photo in photos["items"]:
            max_size_photo = sorted(photo["sizes"], key=lambda dict: dict["height"])
            url = max_size_photo[-1]["url"]
            name = f"{path}/{num}.jpg" 
            urllib.request.urlretrieve(url, name)
            num += 1
            step += 1
            thread.progress_signal.emit(step)
        return step




    
        
        

    
