from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.blog, name="blog"),
    path('<int:blog_id>/', blog.views.detail, name="detail"),
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
    path('detail/<int:blog_id>/destroy', blog.views.destroy, name="destroy"),
    path('newblog/', blog.views.blogpost, name="newblog"),
]
