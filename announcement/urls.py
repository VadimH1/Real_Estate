from django.urls import path
from . import views
from .views import AnnounceAPIView, DeleteAnnounceApiView, UpdateAnnounceApiView

urlpatterns = [
    path('create_announce/', AnnounceAPIView.as_view(), name='announcement'),
    path('delete_announce/<int:author_id>/', DeleteAnnounceApiView.as_view(), name='delete_announce'),
    path('update_announce/<int:author_id>/', UpdateAnnounceApiView.as_view(), name='update_announce'),
]
