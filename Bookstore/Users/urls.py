from django.urls import path

from .views import register_user,login_user



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
    path("signup/", register_user, name="signup"),


     path("login/",login_user, name="login"),#render login view as function #function based views

    
]