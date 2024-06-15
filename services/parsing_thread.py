import os
import re

from PySide6.QtCore import QThread, Signal

from services.parsing import Parser


class ParserThread(QThread):
    """ Создаёт отдельный поток для процесса загрузки фотографий.
    Сигнал progress_signal возвращает текущий шаг загрузки, а сигнал
    finished_signal уведомляет о завершении процесса
    """

    progress_signal = Signal(int)
    finished_signal = Signal()

    def __init__(
        self, 
        checkbox_wall: bool,
        checkbox_album: bool,
        token: str,
        group_id: int,
        path: str,
        count: int,
        offset: int,
        checked_albums: list,
        parent=None
    ):
        super(ParserThread, self).__init__(parent)
        self.parser = Parser(token)
      
        self.checkbox_wall = checkbox_wall
        self.checkbox_album = checkbox_album
        self.group_id = group_id
        self.path = path
        self.count = count
        self.offset = offset
        self.checked_albums = checked_albums

    def run(self) -> int:
        step = 0
        if self.checkbox_wall:
            photos = self.parser.get_photos(group_id=self.group_id, album_id="wall", count=self.count, offset=self.offset)
            step = self.parser.save_photos(photos, self.path, step, self)

        if self.checkbox_album:

            for album_id, title in self.checked_albums.items():
                title = re.sub(r"[^\s\w]", " ", title)
                title = re.sub(r"\s+", " ", title)
                album_path = self.path + "/" + title.strip()
                os.makedirs(album_path, exist_ok=True)

                photos = self.parser.get_photos(group_id=self.group_id, album_id=album_id)
                step = self.parser.save_photos(photos, album_path, step, self)

        self.finished_signal.emit()
