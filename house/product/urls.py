from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('shop/', magazine, name='shop'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category')
]