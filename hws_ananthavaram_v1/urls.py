"""hws_ananthavaram_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboardaction
from medicine.views import medicineaction
from dashboard.views import index
from dashboard.views import sessfun
# from article.views import article_detail
# from article.views import article
# from article.views import add_comment
from dashboard.views import klumapaction
from hospitals.views import chart_view
from blog.views import blog_detail, blog_list
from authentication.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeaction, name = 'home'),

    path('dashboard/', dashboardaction, name = 'dashboard'),
    path('medicine/', medicineaction),
    path('index/', index, name = 'index'),
    path('session/', sessfun, name = 'session'),
    # path('articles/', article, name='article'),
    # path('articles/<slug:slug>/', article_detail, name='article_detail'),
    # path('articles/<slug:slug>/add_comment/', add_comment, name='add_comment'),
    path('klumap/', klumapaction, name = 'klumap'),
    path('viz/', chart_view, name = 'chartview'),
    path('blog/', blog_list, name='blog_list'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'), 
    # path('blog/', create_blog, name='blog_create'),   
    path('login/',login_user, name ='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', register_user, name='register'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    path('profile/', profile, name='profile'),









]
