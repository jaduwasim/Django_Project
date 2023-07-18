from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

# This Will call When user login successfully.
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('login Success:')
    print('---------------------------------------------')
    print('logged in singnal ... Run Intro')
    print('sender:', sender)
    print('Rquest:',request)
    print('User:', user)
    print('User Password:',user.password)
    print(f'kwargs: {kwargs}')
# user_logged_in.connect(login_success, sender=User) #We can use this instead of decorator @reversed(user_logged_in, sender=User)

# This will call when user logedin 
@receiver(user_logged_out, sender=User)
def loguot_success(sender, request, user, **kwargs):
    print('logout Success;')
    print('==========================================')
    print('logedout in signal...Run Intro')
    print('sender', sender)
    print('Request:',request)
    print('user:',user)
    print('user password:', user.password)
    print(f'kwargs: {kwargs}')
# user_logged_out.connect(loguot_success, sender=User) #We can use this instead of decorator @receiver(user_logged_out, sender=User)

# This will call when user login failed, Thats means given credentials were worong!!!!
@receiver(user_login_failed)
def login_failded(sender, credentials, request, **kwargs):
    print('login Failled;')
    print('==========================================')
    print('logedin Failled signal...Run Intro')
    print('sender', sender)
    print('Request:',request)
    print('credentials:',credentials)
    print(f'kwargs: {kwargs}')
# user_login_failed.connect(login_failded) #We can use this instead of decorator @receiver(user_login_failed)