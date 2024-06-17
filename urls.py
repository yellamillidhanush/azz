from django.urls import path
from . import views
urlpatterns=[
   path('',views.loginform,name='loginurl'),
   path('createaccount/',views.createaccount,name='createurl'),
   path('forgotpassword/',views.forgotpassword,name='forgotpaasurl'),
   path('terms/',views.terms,name='termsurl')
]