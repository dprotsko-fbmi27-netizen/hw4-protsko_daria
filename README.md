# Titanic MySQL Docker Project

## Мета проєкту

Навчитись піднімати реляційну базу даних у Docker, завантажувати в неї реальний датасет і зчитувати дані з Python.

У цьому проєкті використовується датасет Titanic, який завантажується у MySQL 8.0 через `LOAD DATA INFILE`, а потім зчитується у Python як `pandas.DataFrame`.

## Структура проєкту

```text
project/
├── docker-compose.yml
├── init.sql
├── titanic.csv
├── main.py
├── requirements.txt
└── README.md
```

## Як запустити

Перейти в папку проєкту
```
cd project
```

Створити та активувати віртуальне середовище
```
python3 -m venv .venv
source .venv/bin/activate
```

Встановити Python-залежності
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Запустити MySQL у Docker
```
docker compose up -d
```

Перевірити статус контейнера
```
docker compose ps
```

Запустити Python-скрипт
```
python main.py
```
