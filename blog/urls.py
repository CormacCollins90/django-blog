from django.urls import path
from blog.views import read_post, edit_post, write_post, publish_post, get_unpublished_posts


urlpatterns = [
    path('unpublished', get_unpublished_posts, name='get_unpublished_posts'),
    path('write/', write_post, name='write_post'),
    path('<int:id>/', read_post, name='read_post'),
    path('<int:id>/edit/', edit_post, name='edit_post'),
    path('<int:id>/publish/', publish_post, name='publish_post'),
    ]