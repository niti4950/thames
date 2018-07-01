"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    url(r'^products/$',products,name='products'),
    url(r'^products/(\w+)/$',single_category,name='category'),
    url(r'^aboutus/$',aboutus,name='aboutus'),
    url(r'^blog/$',blog,name='blog'),
    url(r'^blog_detail/$', blog_detail,name='blog_detail'),
    url(r'^product_details/(\d+)$', product_details,name='product_details'),
    url(r'^contactus/$', contactus,name='contactus'),
    url(r'^signup/$', sign_up,name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^auth-check/$', auth_view,name='check'),
    url(r'^logout/$', logout,name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
