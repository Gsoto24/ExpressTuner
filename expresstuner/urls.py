"""expresstuner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from core import views as core_views
from core import download_logic as DL

urlpatterns = [
    url(r'^$', core_views.upload_new_declines),
    url(r'^runexpresstuner/$', core_views.run_expresstuner),
    url(r'^uploadhistory/$', core_views.upload_history),
    url(r'^howtouse/$', core_views.how_to_use),
    url(r'^downloads/(?P<method_name>[-\w]+)$', core_views.downloads_dispatcher),
    url(r'^admin/', admin.site.urls),
]
