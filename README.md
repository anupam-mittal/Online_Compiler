# Online_Compiler
Web based online compiler using django. It works on POST request of HTTP requests.
Currently it supports three languages.
The POST request is received at the backend and a file is created with the selected language extention. The file is executed at the backend and then the output is sent back to frontend.

# Requirements
1. Django
2. Subprocess
3. Languages installed in the host system
4. Prior knowledge of file handeling

# Execution
```
pipenv shell
python manage.py runserver
```
# Screenshot 
<img width="1680" alt="Screenshot 2022-11-10 at 3 24 02 PM" src="https://user-images.githubusercontent.com/81715230/209231405-bc84da5f-f1e6-4d11-991c-d1b7f0a86e92.png">
