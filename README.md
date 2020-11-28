# Food Diary

내가 쓰려고 만드는 푸드 다이어리

## Getting Started

### Prerequisite

#### Tools

- [pyenv](https://github.com/pyenv/pyenv#installation)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#installation)

#### Settings

- secrets.json (See secrets.example.json)




### Create virtualenv

```
pyenv install 3.8.2 # if the version is already installed, this step can be ignored.
pyenv virtualenv 3.8.2 fooddiary
pyenv activate fooddiary
pip install -r requirements.txt
```

### DB migration

```
python manage.py migrate
```

### Run Dev Server

```
python manage.py runserver 0.0.0.0:8080
```