1. Instalezi python
2. Iti creezi un environment virtual: python -m venv ./VirtualEnv
3. Din VirtualEnv/Scripts/ activezi din environmentul cu activate.bat
4. Ai un fisier requirements, instalezi ce e inauntru:  pip install -r requirements.txt
5. Intrii in folderul cu manage.py
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py runserver