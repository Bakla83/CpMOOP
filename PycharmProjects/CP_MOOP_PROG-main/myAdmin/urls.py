from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminViewList.as_view(), name='myAdmin'),
    path('products', views.AdminListProducts.as_view(), name='adminArticles'),
    path('products/create', views.AdminCreateProducts.as_view(), name='adminArticlesCreate'),
    path('products/<int:pk>/delete', views.AdminDeleteProducts.as_view(), name='adminArticlesDelete'),
    path('products/<int:pk>/update', views.AdminUpdateProducts.as_view(), name='adminArticlesUpdate'),
    path('users', views.AdminListUsers.as_view(), name='adminUsers'),
    path('users/create/', views.AdminCreateUsers.as_view(), name='adminUsersCreate'),
    path('users/delete/<int:pk>', views.AdminDeleteUsers.as_view(), name='adminUsersDelete'),
    path('users/update/<int:pk>', views.AdminUpdateUsers.as_view(), name='adminUsersUpdate'),
]
