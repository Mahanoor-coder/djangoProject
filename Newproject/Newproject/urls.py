from django.contrib import admin
from django.urls import path, include  # Import `include` for including other URL patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Correct way to include home.urls
]
