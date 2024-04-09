
from django.contrib import admin
from django.urls import path
from lynx.views import index,contact

urlpatterns = [
    path('',contact,name="contact"),
    path("contact", index, name="index"),
    path('admin/', admin.site.urls),
]
