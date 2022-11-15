from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('members/', include('sheets.urls')),
    path('admin/', admin.site.urls),
]