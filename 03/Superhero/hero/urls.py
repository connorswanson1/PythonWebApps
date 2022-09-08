from django.urls import path
from .views import BlackWidow, HulkView, IndexView, IronManView, MoonKnight, SilverSurfer

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidow.as_view()),
    path('silversurfer', SilverSurfer.as_view()),
    path('moonknight', MoonKnight.as_view()),
]
