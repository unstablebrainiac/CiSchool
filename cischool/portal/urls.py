"""cischool URL Configuration

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
from django.urls import include
from django.urls import path

from portal import views

urlpatterns = [
	path('^', views.land, name='landing'),
	path('login/^', views.login, name='login'),
	path('register/^', views.regsiter, name='register'),
	path('courses/^', views.courses, name='courses'),
	path('courses/?P<pk>\d+/edit/^', views.edit_course, name='edit_course'),
	path('mypolicies/^', views.policies, name='get_policies'),
	path('policy/?P<pk>\d+/edit/^', views.edit_policies, name='edit_policies')
]
