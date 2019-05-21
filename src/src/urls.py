from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('simel/', include('simel.urls')),
    path('admin/', admin.site.urls),
]
