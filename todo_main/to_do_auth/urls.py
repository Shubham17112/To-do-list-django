from django.urls import path
from . import views
app_name = 'to_do_auth'
urlpatterns = [
    path('singup/',views.singup,name='singup')
]
