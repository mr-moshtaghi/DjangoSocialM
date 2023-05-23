from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('base/', include('base.urls', namespace='base')),
    path('', include('pwa.urls')),
    path('account/', include('account.urls', namespace='account')),
]
