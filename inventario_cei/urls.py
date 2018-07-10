from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='home'),
    path('objetos', views.objects, name='objetos'),
    path('espacios', views.spaces, name='espacios'),

    # long
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),

    # helping urls
    path('testdata', views.testdata, name='testdata'),
    path('createtestdata', views.createtestdata, name='createtestdata')
]
