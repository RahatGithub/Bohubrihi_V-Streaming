from django.urls import path
from App_Posts import views 

app_name = 'App_Posts'

urlpatterns = [
    path("", views.home, name='home'),
    path('post/<int:post_id>/', views.post_view, name='post_view')
]
