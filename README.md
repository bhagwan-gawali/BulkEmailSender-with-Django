# BulkEmailSender-with-Django
small app for sending bulk email with django

---

## How to Use

1. clone repository or download into your machine.
2. install the dependency of the project.
3. change the settigs.py file (look at the bottom of the file Email Setting section)
  Email Settings:
  
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'Enter your smtp-host'
  EMAIL_USE_TLS = True
  EMAIL_PORT = 587
  EMAIL_HOST_USER = 'enter your username/email address'
  EMAIL_HOST_PASSWORD = 'enter your password' 
4. Change this accoring to your settings.
5. run the deveopment server:
    **python manage.py runserver**
6. In the web browser goto **http://127.0.0.1:8000/blkmailsender/home/**
7. Thats it.
