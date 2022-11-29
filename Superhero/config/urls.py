from django.contrib import admin
from django.urls import path, include
from hero.views import *
from django.conf import settings
from django.conf.urls.static import static
from messenger.views import *
urlpatterns = [

    # Blog
   # path('', include('blog.urls')),

    # Hero
    path('', include('hero.urls')),

    # Photo
    path('', include('photos.urls')),

    #Messages
    path('', include('messenger.urls')),

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/', UserUpdateView.as_view(), name='account_edit'),
    

    # Admin views for users
    # path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
