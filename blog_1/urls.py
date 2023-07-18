from django.urls import  path
from .views import (
    BlogListview,
    BlogDetailview,
    BlogCreateview,
    BlogUpdateview,
    BlogDeleteview
)
urlpatterns=[
    path('post/<int:pk>/delete/',BlogDeleteview.as_view(), name='post_delete'),
    path('post/<int:pk>/edit',BlogUpdateview.as_view(), name='post_edit'),
    path('post/new/', BlogCreateview.as_view(), name='post_new'),
    path('',BlogListview.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetailview.as_view(), name='post_detail')
]