from django.urls import path
from .views import (
    SignUpView, UserLoginView, UserLogoutView, ProfileView,
    AddressListView, AddressCreateView, AddressUpdateView, AddressDeleteView
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('addresses/', AddressListView.as_view(), name='address_list'),
    path('addresses/add/', AddressCreateView.as_view(), name='address_add'),
    path('addresses/<int:pk>/edit/', AddressUpdateView.as_view(), name='address_edit'),
    path('addresses/<int:pk>/delete/', AddressDeleteView.as_view(), name='address_delete'),
]