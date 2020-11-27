FLASHCARDS APP WITH DJANGO AND VUE.JS

How to run:


A) DOWNLOAD APP

1. Download or clone (https://github.com/sergiofv/flashcards.git) flashcards app repo.

2. Make sure you have installed python and pip (https://www.python.org/downloads/)

3. [Optional] Open a terminal and install virtualenv and create your custom virtual env and activate it:

$ pip install virtualenv

$ virtualenv venv

$ /venv/Scripts/activate


B) RUN DJANGO API

3. Open a terminal and go to the ..\flashcards-master\ folder and run:

$ pip install requirements.txt

4. In the same terminal go to ..\flashcards-master\prueba\ folder and run django server:

$ python manage.py runserver


C) RUN VUE APP 

5. Make sure you have installed node.js and npm (https://nodejs.org/en/download/)

6. Open another terminal and go to ..\flashcards-master\frontend\ and install vue dependencies:

$ npm install -g @vue/cli

$ npm i vue-flashcard

7. Run your Vue.js app:

$ npm run serve

8. Open http://192.168.0.212:8080/ in your web browser and create, edit and delete custom flashcards!

