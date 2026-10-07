# Сайт факультету гуманітарних наук НаУКМА

```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Сторінки: `/`, `/departments/`, `/programs/`, `/exchange/` (`/exchange/?country=Польща`), адмінка: `/admin/`.

Перевірка відкату:
```
python manage.py migrate exchange zero
python manage.py migrate
python manage.py makemigrations --check
```
