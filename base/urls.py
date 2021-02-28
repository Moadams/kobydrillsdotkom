from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name = 'loginPage'),
    path('logout/',views.logoutUser, name = 'logoutUser'),
    path('',views.home,name = 'home'),
    path('post/<slug:slug>/',views.post,name = 'post'),
    path('categories/<int:pk>/', views.categoryPosts, name = 'categories'),
    path('video-posts/',views.videoPosts, name = 'videoPosts'),
    path('video-post/<slug:slug>/',views.videoPost, name = 'videoPost'),
    path('audio-posts/',views.audioPostsView, name = 'audioPosts'),
    path('audio-post/<slug:slug>/',views.audioPost, name = 'audio'),
    path('contact-us/',views.contactView, name = 'contact'),
    
    
    #CRUD PATHS
    path('categories/add-category/', views.addCategoryView, name = 'add_category'),
    path('posts/add-post/', views.addPostView, name = 'add_post'),
    path('posts/delete-post/<slug:slug>/', views.deletePost, name = 'delete_post'),
    path('posts/update-post/<slug:slug>/',views.updatePost, name = 'update_post'),
    path('video-posts/add-video-post/',views.addVideoPost,name = 'add_video_post'),
    path('video-posts/update-video-post/<slug:slug>/',views.updateVideoPost, name = 'update_video_post'),
    path('video-posts/delete/<slug:slug>/', views.deleteVideoPost, name = 'delete_video_post'),
    path('audio-posts/add-audio-post/',views.addAudioView,name = 'add_audio_post'),
    path('audio-posts/update-audio-post/<slug:slug>/',views.updateAudioPost, name = 'update_audio_post'),
    path('audio-posts/delete/<slug:slug>/', views.deleteAudioPost, name = 'delete_audio_post'),
]