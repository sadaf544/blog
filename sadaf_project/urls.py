from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('main/', include('main.Urls')), # main will be the name of your app
    path('admin/', admin.site.urls),
]
