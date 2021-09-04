from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login_success/',views.login_success)
]
