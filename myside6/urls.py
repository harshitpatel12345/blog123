"""
URL configuration for myside6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog6.views import (CreatePostView, UpdatePostView, ListPostView,
                         DeletePostView, CreateCategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_post/', CreatePostView.as_view(), name='create-post'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('list_post/', ListPostView.as_view(), name='list-post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('createcategory/', CreateCategoryView.as_view(), name='create-category'),


]
