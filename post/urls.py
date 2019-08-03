from django.conf.urls import url, include
from django.urls import path
from post import views

urlpatterns = [
    path('post/list-post/', views.List_Publish_Posts.as_view(), name='get-posts'), # list k can login
    path('post/list-post-user/', views.List_Posts_User.as_view(), name='get-posts-user'), # list cua user can login vao user do
    path('post/',views.Create_Posts.as_view(), name='posts'), # login user nao thi author cua post 
    path('post/get-post-detail/<int:pk>/', views.Get_Deatail_Post.as_view(), name="get-detail-post"), # get detail
    path('post/post-detail/<int:pk>/', views.Update_Delete_Post.as_view(), name='post-detail'), # 
    path('post/like-post/', views.Users_Like.as_view(), name='post-detail'),
    
   
]