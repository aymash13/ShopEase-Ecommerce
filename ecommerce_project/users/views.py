from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Profile, Address
from .forms import SignUpForm, ProfileForm, AddressForm

# ---------------------------------
# 1️⃣ Signup View
# ---------------------------------
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('home')  # redirect to homepage after signup

    def form_valid(self, form):
        response = super().form_valid(form)
        # Create Profile automatically
        Profile.objects.get_or_create(user=self.object)
        # Auto-login after signup
        login(self.request, self.object)
        return response

# ---------------------------------
# 2️⃣ Login & Logout Views
# ---------------------------------
class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

# ---------------------------------
# 3️⃣ Profile View (Display & Update)
# ---------------------------------
@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile

# ---------------------------------
# 4️⃣ Address List View
# ---------------------------------
@method_decorator(login_required, name='dispatch')
class AddressListView(ListView):
    model = Address
    template_name = 'users/address_list.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        # Only show addresses belonging to the logged-in user
        return Address.objects.filter(profile=self.request.user.profile)

# ---------------------------------
# 5️⃣ Address Add View
# ---------------------------------
@method_decorator(login_required, name='dispatch')
class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'users/address_form.html'
    success_url = reverse_lazy('address_list')

    def form_valid(self, form):
        # Link new address to the logged-in user's profile
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

# ---------------------------------
# 6️⃣ Address Edit View
# ---------------------------------
@method_decorator(login_required, name='dispatch')
class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'users/address_form.html'
    success_url = reverse_lazy('address_list')

    def get_queryset(self):
        # Restrict editing to addresses owned by the logged-in user
        return Address.objects.filter(profile=self.request.user.profile)

# ---------------------------------
# 7️⃣ Address Delete View
# ---------------------------------
@method_decorator(login_required, name='dispatch')
class AddressDeleteView(DeleteView):
    model = Address
    template_name = 'users/address_confirm_delete.html'
    success_url = reverse_lazy('address_list')

    def get_queryset(self):
        # Restrict deletion to addresses owned by the logged-in user
        return Address.objects.filter(profile=self.request.user.profile)