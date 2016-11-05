from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import RegistrationForm, LoginForm


class HomepageView(generic.TemplateView):
    template_name = 'home1.html'

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('Success')
    model = User
    template_name = 'accounts/SignUp.html'


class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('user')
    template_name = 'accounts/Login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)

        if user is not None and user.is_active:
            login(self.request,user)
            return super(LoginView,self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy('home')
    def get(self,request,*args,**kwargs):
        logout(request)
        return super(LogoutView,self).get(request,*args,**kwargs)


def RegisterSuccess(request):
    return render(request, 'accounts/register_success.html')