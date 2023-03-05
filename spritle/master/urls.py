from django.urls import path
from .views import master_signup, master_tasks, masterlogin, master_solved, logoutview


urlpatterns = [
    path('signup',master_signup.as_view(), name= 'master-signup'),
    path('login',masterlogin.as_view(),name='master-login'),
    path('students_activities',master_tasks.as_view(),name='master-tasks'),
    path('master-solved',master_solved.as_view(),name='solved-by-me'),
    path('logout',logoutview.as_view(),name='master-logout')
]