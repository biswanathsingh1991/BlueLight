from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls', namespace='post')),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('api.urls', namespace='api')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
