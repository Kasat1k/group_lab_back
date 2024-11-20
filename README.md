# Star on local machine

```
$ python3 -m venv .venv

# On Unix
$ source .venv/bin/activate

# On Windows
$ .venv/Scripts/Activate

$ pip install -r requirements.txt

uvicorn app.main:app --reload
```

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

# Start on Docker
```
$ docker-compose up --build
```

http://0.0.0.0:8000
http://0.0.0.0:8000/docs