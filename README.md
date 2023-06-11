# DjangoBlog

# Steps to run:
1. `python3 manage.py runserver  `
2. Vist `http://localhost:3000/`

# Mandatory changes to be done for email server:
1. If you want to use localhost as mail server run `python -m smtpd -n -c DebuggingServer localhost:1025`
2. If you want to use gmail as mail server add values here your email host and password in `DjangoBlog/blog/settings.py`:

   ` EMAIL_HOST_USER =` 
   `EMAIL_HOST_PASSWORD = `
