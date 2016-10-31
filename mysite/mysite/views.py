from django.contrib.auth.models import User
from django.views import generic

from .forms import RegistrationForm


class HomepageView(generic.TemplateView):
    template_name = 'home1.html'

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'accounts/SignUp.html'

