from django.urls import path 
from App_Accounts import views 

app_name = "App_Accounts" 

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'), 
    path('login/', views.log_in, name='log_in'),
    # path('edit/', views.edit_profile, name='edit_profile'), 
    path('logout/', views.logout_user, name='logout'), 
    # path('profile/', views.profile, name='profile'),
    # path('user/<username>/', views.user, name='user'),
    # path('follow/<username>', views.follow, name='follow'),
    # path('unfollow/<username>', views.unfollow, name='unfollow'),
]