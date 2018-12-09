"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from .views import home, get_page, get_type, blog_with_date, login_blog

urlpatterns = [
    path('', home,name='home'),
    path('<int:blog_page>',get_page,name='get_page'),
    path('type/<str:blog_type>', get_type, name='get_type'),
    path('date/<int:year>/<int:month>', blog_with_date, name='blog_with_date'),
    path('login/', login_blog, name='login'),
]
