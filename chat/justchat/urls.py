from  django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name="index"),
    path('usersa/', include('django.contrib.auth.urls')),
    path('reg/',views.signup,name="registration"),
    # path('chat/<str:room_name>/', views.room,name="room"),
    path('booknew/',views.CreatePost.as_view(),name="AddBook"),
    path('g/',views.beb)

]