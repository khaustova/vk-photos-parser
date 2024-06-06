import json
import requests
import ssl
import urllib.request
import vk_api
import webbrowser
from PySide6 import QtWidgets
from PySide6.QtCore import QThread

ssl._create_default_https_context = ssl._create_unverified_context


class Parser:
    """ Класс, работающий с VK API, для парсинга фотографий
    """

    def __init__(self, token: str):
        """ Инициализирует подключение к VK API с помощью переданного токена,
        а также атрибут vk, позволяющий обращаться к методам VK API как к
        обычным классам
        """

        self.token = token
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()

    @staticmethod
    def get_token_url(line_edit_client_id: QtWidgets.QLineEdit) -> None:
        """ Генерирует ссылку получения токена для переданного ID приложения
        и открывает её в браузере по умолчанию
        """

        client_id = line_edit_client_id.text()
        params = {
            "client_id": client_id,
            "scope": "photos",
            "response_type": "token",
            "display": "page",
            "redirect_uri": "https://oauth.vk.com/blank.html",
            "v": "5.236"
        }
        response = requests.get("http://oauth.vk.com/authorize/", params=params)

        webbrowser.open_new_tab(response.url)

    @staticmethod
    def save_photos(photos: dict, path: str, step: int, thread: QThread) -> int:
        """ Сохраняет фотографии в указанной папке
        """

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

    def get_total_photos(self, line_edit_group_id: QtWidgets.QLineEdit, album_id="wall") -> str:
        """ Возвращает общее количество фотографий на стене или в альбоме
        """

        owner_id = int(line_edit_group_id.text())
        total = self.vk.photos.get(owner_id=-owner_id, album_id=album_id, count=0)["count"]

        return str(total)

    def check_token_url(self, token: str) -> bool:
        """ Выполняет запрос к VK API для проверки действительности токена
        """

        params = {
            "access_token": token,
            "count": 1,
            "v": "5.236",
        }
        response = requests.get("https://api.vk.com/method/database.getCities/", params=params)
        content = json.loads(response.content)

        return True if content.get("response") else False

    def check_group_id(self, group_id: str) -> bool:
        """ Проверяет существование группы и фотографий в ней
        """

        try:
            group_id = int(group_id)
        except ValueError:
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

    def get_photos(self, group_id: int, album_id: int | str, count=None, offset=0) -> list:
        """ Возвращает список фотографий на стене или в альбоме

        Так как VK API ограничивает одновременное получение более 1000 фотографий,
        то процесс осуществляется в бесконечном цикле. При этом вводится переменная
        с целевым значением target, и когда сдвиг offset становится больше или
        равен ей, процесс завершается
        """

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

    def get_albums(self, group_id: int) -> dict[str: dict]:
        """ Возвращает словарь с альбомами группы, где ключами выступает
        отображаемое имя альбома, а значениями - словарь с его параметрами
        """

        all_albums = self.vk.photos.getAlbums(owner_id=-group_id)

        albums = {}
        for album in all_albums["items"]:
            each_album = {}
            each_album["id"] = album["id"]
            each_album["title"] = album["title"]
            each_album["size"] = album["size"]
            name = f"{each_album.get('title')} ({each_album.get('size')})"  
            albums[name] = each_album

        return albums
