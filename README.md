# ASL
ASL backend assignment

1 
C:\Users\ganesh\auth>django-admin startproject auth
C:\Users\ganesh\auth>django-admin startapp users
created django project named auth inside another django proj/app created named users

2 
C:\Users\ganesh\auth>python manage.py runserver

add rest_framework and users in setting 


3 

C:\Users\ganesh\auth>python manage.py makemigrations
Migrations for 'users':
  users\migrations\0001_initial.py
    - Create model User

C:\Users\ganesh\auth>

4 

C:\Users\ganesh\auth>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying users.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying sessions.0001_initial... OK

C:\Users\ganesh\auth>

5
gave url in auth/urls.py foldr

created urls.py file in users for register route

created view in views.py for register

created serializer.py imported user mode in it

6

{
    "name":"ganesh",
    "email":"abc@gmail.com",
    "password":"Computer"
    }
