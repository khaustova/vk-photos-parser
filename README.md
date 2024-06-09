### 1. О программе ###
Программа для парсинга фотографий из групп Вконтакте.

:small_blue_diamond: Загрузка фотографий со стены и альбомов группы в указанную папку  
:small_blue_diamond: Выбор количества фотографий (с начала или с конца), загружаемых со стены группы  
:small_blue_diamond: Выбор загружаемых альбомов  

Для работы программы требуется действительный токен, который следует получить и ввести в соответствии с инструкциями на вкладке "Авторизация".

### 2. Технологии ###
:small_orange_diamond: Python 3.10.9  
:small_orange_diamond: PySide6 6.7.1  
:small_orange_diamond: VK API 5.236
### 3. Запуск ###
Скачайте исполняемый файл [на странице релизов](https://github.com/khaustova/vk-photos-parser/releases) или запустите проект в среде разработки:
1. Клонируйте репозиторий:
```shell
git clone https://github.com/khaustova/vk-photos-parser.git
```
2. Создайте виртуальное окружение:
```shell
python3 -m venv .venv
```
3. Активируйте виртуальное окружение на Windows:
```shell
.venv\Scripts\activate
```
или на macOS/Linux:
```shell
source .venv/bin/activate
```
4. Установите зависимости:
```shell
pip install -r requirements.txt
```
5. Запустите программу:
```shell
python3 main.py
```

### 4. Скриншоты ###

![main_window_photos](https://github.com/khaustova/vk-photos-parser/assets/143105312/3d79120a-e6b4-4098-9649-b7b12bdf6da9)
![main_window_auto](https://github.com/khaustova/vk-photos-parser/assets/143105312/33cb9699-bd20-482d-a8eb-d4110b0f1e13)
![choose_photos](https://github.com/khaustova/vk-photos-parser/assets/143105312/a2b7a62f-a5df-4d3f-b80e-ad9e2c4ea7af)
![choose_albums](https://github.com/khaustova/vk-photos-parser/assets/143105312/3c6b6bc8-f689-47c9-a47b-e14fd2140e4d)
