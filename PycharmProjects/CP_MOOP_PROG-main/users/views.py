from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class AbstractSignUpView(generic.CreateView):
    """
    Абстрактный класс, реализующий шаблонный метод для представления регистрации.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'

    def form_valid(self, form):
        """
        Шаблонный метод, который может быть переопределен подклассами.
        """
        return super().form_valid(form)

class SignUpView(AbstractSignUpView):
    """
    Конкретный класс, реализующий шаблонный метод регистрации.
    """
    def form_valid(self, form):
        """
        Переопределение метода для добавления дополнительной логики.
        """
        response = super().form_valid(form)
        return response
