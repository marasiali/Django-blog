# Django-blog
An exercise blog project to learn Django

## Usage

### Clone this repository in your terminal
```
git clone https://github.com/marasiali/Django-blog.git
```

### Create virtualenv and install dependencies
```
cd Django-blog
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Migrations

```
cd DjangoBlog
python manage.py makemigrations
python manage.py migrate
```

### Test it
run this code :
```
python manage.py runserver
```
Then, open a browser and go to `http://127.0.0.1:8000/`

## Note:
In production, make sure you have changed the SECRET_KEY and turned off DEBUG in `DjangoBlog/DjangoBlog/settings.py`
