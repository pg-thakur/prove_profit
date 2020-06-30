from django.contrib import admin
from django.urls import path ,include
from home import views 

from django.conf.urls import url


from accounts import views as acc_views 
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('', views.home,name='home'),
    path('analysis',views.analysis,name='analysis'),
    path('article',views.article,name='article'),
    path('signup', acc_views.signup,name='signup'),
    path('login', acc_views.login,name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('report',views.report,name='report'),
]