from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('extractor.api.urls')),  # Make sure this line is here!
]
