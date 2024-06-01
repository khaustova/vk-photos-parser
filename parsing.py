import vk_api
import os
import sys
import urllib.request
import ssl 
import json
import requests
import webbrowser

ssl._create_default_https_context = ssl._create_unverified_context

class Parser:
    
    def __init__(self):
        pass
        #self.token = self.get_token_url(51930696)
        
    
    @staticmethod
    def get_token_url(client_id):
        params = {
            "client_id" : client_id,
            "scope" : "photos",
            "response_type" : "token",
            "display" : "page",
            "redirect_uri": "https://oauth.vk.com/blank.html",
            "v" : "5.236"
        }
        response = requests.get('http://oauth.vk.com/authorize/', params=params)
        webbrowser.open_new_tab(response.url)
        
        
    @staticmethod
    def check_token_url(token):
        params = {
            'access_token': token,
            'count': 1,
            'v': "5.236",
        }
        response = requests.get('https://api.vk.com/method/database.getCities/', params=params)
        content = json.loads(response.content)
        return True if content.get('response') else False
        
parser = Parser()