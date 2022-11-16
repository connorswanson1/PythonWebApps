from django.contrib import admin
from django.urls import path, include

from hero.views import UserUpdateView

urlpatterns = [

    # Blog
   # path('', include('blog.urls')),

    # Hero
    path('', include('hero.urls')),

    # Photo
    path('', include('photos.urls')),

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>/', UserUpdateView.as_view(), name='account_edit'),
    

    # Admin views for users
    # path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]
