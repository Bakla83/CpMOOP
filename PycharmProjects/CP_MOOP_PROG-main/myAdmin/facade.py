from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, CreateView
from products.models import Product, ProductImage
from django.contrib.auth.models import User


class AdminFacade:

    @staticmethod
    def admin_view_list():
        return TemplateView

    @staticmethod
    def admin_list_products():
        return ListView

    @staticmethod
    def admin_create_products():
        return CreateView

    @staticmethod
    def admin_update_products():
        return UpdateView

    @staticmethod
    def admin_delete_products():
        return DeleteView

    @staticmethod
    def admin_create_users():
        return CreateView

    @staticmethod
    def admin_list_users():
        return ListView

    @staticmethod
    def admin_delete_users():
        return DeleteView

    @staticmethod
    def admin_update_users():
        return UpdateView
