## Flask Boilerplate

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate

Arrancar aplicación con servidor Werkzeug:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    $ python app.py

Arrancer aplicación con servidor GreenUnicorn:

    $ cd <<carpeta-proyecto>>
    $ pip install -r requirements.txt
    # Sin logs ni reload
    $ gunicorn app:app -w 6 -b 0.0.0.0:3000
    # Con logs y reload
    $ gunicorn app:app -w 6 -b 0.0.0.0:3000 --reload --access-logfile -

### PyLint

    $ pylint <archivo>.py --reports=yes
    $ pylint **/*.py --reports=yes

### Migraciones

Migraciones con DBMATE - accesos:

    $ dbmate -d "db/migrations" -e "DB" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" -e "DB" up
    $ dbmate -d "db/migrations" -e "DB" new <<nombre_de_migracion>>
    $ dbmate -d "db/migrations" -e "DB" up
    $ dbmate -d "db/migrations" -e "DB" rollback

---

Fuentes:

+ https://github.com/pepeul1191/flask-boilerplate-v2
+ https://www.pylint.org/#install
+ https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python/
