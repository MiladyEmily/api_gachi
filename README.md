# GACHI

### Описание проекта gachi

GACHI - это API для генерации никнейма из своего имени в стиле GachiMuchi. (ДимASS, СтаниSlave и т.п.)

При помощи GACHI можно:
* 🙃 посмотреть список гач для своего имени или имени друга (если такого имени еще не было, то список сгенерируется алгоритмом)
* 🙃 добавить собственную гачу к любому имени (будет проверена модератором)
* 🙃 оценить чужие гачи
* 🙃 посмотреть список лучших гач (самых высокорейтинговых) среди всех имен

### Технологии:

Python 3.7 | Django 2.2.16

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MiladyEmily/hw05_final
```

```
cd hw05_final
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
