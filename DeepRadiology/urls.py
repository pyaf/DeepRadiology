from django.conf.urls import url, include
from django.contrib import admin
from app.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),

]
