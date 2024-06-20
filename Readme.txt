-----Установка-----

-Клонировать проект в пустую папку:
git clone https://github.com/DmAlFat/Test_task_bot.git.

-Установить необходимые модули:
pip install -r requirements.txt.

-Создать базу данных MongoDB и наполнить её данными, скачанными по ссылке в конце Test_task.txt

-Создать файл .env в корне проекта и задать в нём:
* параметры для подключения к Вашей базе данных MongoDB (HOST, PORT, DATABASE, COLLECTION);
* TOKEN_API вашего телеграм-бота.

-Активировать бота, запустив файл main.py.