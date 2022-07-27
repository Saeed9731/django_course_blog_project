from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # path('home/', include('blog.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('accounts.urls')),
]
