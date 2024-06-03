from PySide6.QtCore import QThread, Signal
from parsing import Parser
import urllib.request
import time


class ParserThread(QThread):
 
    progress_signal = Signal(int)
    finished_signal = Signal()
    
    def __init__(self, checkbox_wall, token, group_id, path, count, parent=None):
        super(ParserThread, self).__init__(parent)
        self.parser = Parser(token)
                
        self.checkbox_wall = checkbox_wall
        self.group_id = group_id
        self.path = path
        self.count = count

        
    def run(self):
        if self.checkbox_wall:
            photos = self.parser.parse_wall(self.group_id, self.count)
            
            num = 0  
            for photo in photos['items']:
                max_size_photo = sorted(photo['sizes'], key=lambda dict: dict['height'])
                url = max_size_photo[-1]['url']
                name = f'{self.path}/{num}.jpg' 
                urllib.request.urlretrieve(url, name)
                num += 1
                self.progress_signal.emit(num)
            self.finished_signal.emit()