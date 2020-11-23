from django.urls import path
from basicapp import views

#Templates Tagging

app_name = 'basicapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='regiteration'),
    path('user_login',views.user_login,name='user_login')
]
