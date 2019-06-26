from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

def get_template_path(file_name):
    return "registration/{}.html".format(file_name)
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = get_template_path('login')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = get_template_path('logout')), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = get_template_path('password_reset_form'),html_email_template_name="registration/password_reset_email.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = get_template_path('password_reset_done')), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = get_template_path('password_reset_confirm')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = get_template_path('password_reset_complete')), name='password_reset_complete'),
    path('activate/<uidb64>/<token>', views.Activate.as_view(), name='activate'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
