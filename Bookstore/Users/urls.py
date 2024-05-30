from django.urls import path

from .views import register_user,login_user,users_dashboard,logout_user

from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
    path("signup/", register_user, name="signup"),


     path("dashboard/",users_dashboard, name="dashboard"),


     path("login/",login_user, name="login"),#render login view as function #function based views

     path("logout/",logout_user, name="logout"),
     #path("password/reset/",password_reset, name="resetPassword"),



     path('password/reset/', 
        PasswordResetView.as_view(
            template_name='password_reset.html',
            html_email_template_name='password_reset_email.html'
        ),
        name='passwordReset'
    ),
    path('password/reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password/reset/complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]