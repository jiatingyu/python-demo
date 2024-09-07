from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    re_path(r'about/(?P<index>[0-9]+)/(?P<name>\w+)/$', views.about, name='about'),
]
