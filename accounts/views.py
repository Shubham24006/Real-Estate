from .models import Profile
from contacts.models import Contact
from .froms import RegisterForm, LoginForm, UpdateProfileForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        email = request.POST['email']
        if Profile.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'user register succesfully')
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):

        logout(request)
        messages.success(request, 'user logout succesfully')
        return redirect('login')


def user_login(request):
    login_form = LoginForm(request.POST or None)
    # messages.success(request, 'user login succesfully')
    context = {
        "form": login_form
    }
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'UserName Or PassWord Incorrect')

    return render(request, 'accounts/login.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


class Dashboard(DetailView):
    template_name = 'accounts/dashboard.html'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs ):
        context = super(Dashboard, self).get_context_data(**kwargs)
        profile = Profile.objects.get(id=self.kwargs['pk'])
        context['listings'] = Contact.objects.order_by('-contact_date').filter(buyer_id=self.request.user.id)
        context['properties'] = profile.properties.all()
        return context


class ProfileUpdate(UpdateView, SuccessMessageMixin):
    success_message = 'Update sucessfully'
    template_name = 'accounts/register.html'
    form_class = UpdateProfileForm
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse('dashboard', kwargs={'pk': self.kwargs['pk']})
