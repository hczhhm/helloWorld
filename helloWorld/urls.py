"""helloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from . import view,myFirstPost,userInfo,postName,dataFormMysql

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^myFirstPost', myFirstPost.myFirstPost),
    url(r'^api/user', userInfo.userInfo),
    url(r'^api/searchForUserId', postName.post_name),
    url(r'^api/myInfo', dataFormMysql.catMyInfo),
]