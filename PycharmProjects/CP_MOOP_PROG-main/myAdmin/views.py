from .facade import AdminFacade
from products.models import Product, ProductImage
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class AdminViewList(AdminFacade.admin_view_list()):
    template_name = 'admin/admin.html'

class AdminListProducts(AdminFacade.admin_list_products()):
    template_name = 'admin/products.html'
    model = ProductImage

class AdminCreateProducts(AdminFacade.admin_create_products()):
    template_name = 'admin/product_add.html'
    model = Product
    fields = ['name', 'price', 'discount', 'category', 'description']

class AdminUpdateProducts(AdminFacade.admin_update_products()):
    template_name = 'admin/product_update.html'
    model = Product
    fields = ['name', 'price', 'discount', 'category', 'description']

class AdminDeleteProducts(AdminFacade.admin_delete_products()):
    template_name = 'admin/product_delete.html'
    model = Product
    success_url = reverse_lazy('adminArticles')

class AdminCreateUsers(AdminFacade.admin_create_users()):
    template_name = 'admin/create_users.html'
    model = User
    fields = ['username', 'email', 'is_superuser', 'is_active']
    success_url = reverse_lazy('adminUsers')

class AdminListUsers(AdminFacade.admin_list_users()):
    template_name = 'admin/users.html'
    model = User

class AdminDeleteUsers(AdminFacade.admin_delete_users()):
    template_name = 'admin/delete_users.html'
    model = User
    success_url = reverse_lazy('adminUsers')

class AdminUpdateUsers(AdminFacade.admin_update_users()):
    template_name = 'admin/update_users.html'
    model = User
    fields = ['username', 'email', 'is_superuser', 'is_active']
    success_url = reverse_lazy('adminUsers')
