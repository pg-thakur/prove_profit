from django.contrib import admin
from django.conf.urls import url

from django.urls import path ,include
from accounts import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # path('analysis',views.analysis,name='analysis'),
    # path('article',views.article,name='article')
]