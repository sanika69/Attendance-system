# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path('admin/',admin.site.urls),
    path('',views.home),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('teacher_info/<int:id>/',views.teacher_info,name="teacher_info"),
    path('t_details/',views.t_details,name="t_details"),
    # path('signup/',views.signup,name='signup'),
    path('signup/',views.signup,name='signup'),
    path('fy_cform/',views.fy_cform,name='fy_cform'),
    path('fy_cdetails/',views.fy_cdetails,name='fy_cdetails'),
    path('sy_form/',views.sy_form,name='sy_form'),
    path('sy_details/',views.sy_details,name='sy_details'),
    path('ty_form/',views.ty_form,name='ty_form'),
    path('ty_details/',views.ty_details,name='ty_details'),
    path('ly_form/',views.ly_form,name='ly_form'),
    path('ly_details/',views.ly_details,name='ly_details'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),



    # path('signup/',views.signup,name='signup'),
]