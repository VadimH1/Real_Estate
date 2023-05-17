from django.urls import path
from . import views
from .views import AnnounceAPIView

urlpatterns = [
    path('api/v1/announce/', AnnounceAPIView.as_view()),
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
]


