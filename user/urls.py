from django.urls import path
from . import views
from .views import UserRegistration, UserLogin, ProfileApiView, ActivateApiView, ChangeEmailApiView, ChangePasswordApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/register/', UserRegistration.as_view(), name='register'),
    path('login', UserLogin.as_view(), name='login'),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('user_profile/', ProfileApiView.as_view(), name='profile'),  
    path('activate/<user_uuid_number>', ActivateApiView.as_view(), name='activate'),
    path('change_email/', ChangeEmailApiView.as_view(), name='change_email'),
    path('change_password/', ChangePasswordApiView.as_view(), name='change_password'),

]