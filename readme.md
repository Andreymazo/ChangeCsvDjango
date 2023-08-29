App - organaizer.

User can add, update, delete (CRUD) fields from admin panel. User can use tree effect - to CRUD child fields. For that one must import .xls file with existing data and depending on logic in .exl file one must change views.read_file_create_model in appropriate way or start from the begining without importing any file.

Insalling process:

 - mkdir <appname>
 - git clone git@github.com:Andreymazo/ChangeCsvDjango.git
 - pip install -r requirements.txt
 - python manage.py create_super_user
 - choose file with .exl extension and manage to import right way into proper model fields

 to use admin panel paste ../admin/ 
 enter  username: 'andreymazo@mail.ru'
        password: 'qwert123asd'

