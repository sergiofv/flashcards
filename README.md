# Flashcards app with Django and Vue.js

## Installation

DOWNLOAD APP

1. Download or clone (https://github.com/sergiofv/flashcards.git) flashcards app repo.

2. Make sure you have installed python and pip (https://www.python.org/downloads/)

3. [Optional] Open a terminal and install virtualenv and create your custom virtual env and activate it:

```bash
pip install virtualenv

virtualenv venv

/venv/Scripts/activate
```

RUN DJANGO API

4. Open a terminal and go to the ..\flashcards-master\ folder and run:

```bash
pip install requirements.txt
```

5. In the same terminal go to ..\flashcards-master\prueba\ folder and run django server:

```bash
python manage.py runserver
```

RUN VUE APP 

6. Make sure you have installed node.js and npm (https://nodejs.org/en/download/)

7. Open another terminal and go to ..\flashcards-master\frontend\ and install vue dependencies:

```bash
npm install -g @vue/cli

npm i vue-flashcard
```

8. Run your Vue.js app:

```bash
npm run serve
```

8. Open http://192.168.0.212:8080/ in your web browser and create, edit and delete custom flashcards!

