from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from . import views
from administration.views import *
from django.conf.urls.i18n import set_language
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
	path('register/', RegisterUserView.as_view(), name='register'),
	
    path('api/delete-user/<int:user_id>/', delete_user, name='delete_user'),

	path('login/', login_view, name='login'),
	path('reset_password_email/', reset_password_email, name='reset_password_email'),
	path('reset_password_confirm/<str:uidb64>/<str:token>', reset_password_confirm, name='reset_password_confirm'),

    path('artistes/', ArtistesListView.as_view(), name='artistes-list'),    
    path('regenerate-qr-codes/', views.regenerate_qr_codes, name='regenerate_qr_codes'),
    
    path('codeqr/', views.CodeQRListCreateAPIView.as_view(), name='codeqr-list-create'),
    path('codeqr/<int:pk>/', views.CodeQRRetrieveUpdateDestroyAPIView.as_view(), name='codeqr-retrieve-update-destroy'),
    
    ###################    La vue des pages    ###################
    # path('home', home, name='home'),
    path('streamings/', streamings, name='streamings'),
    path('access_streaming/<int:spectacle_id>/', views.access_streaming, name='access_streaming'),
    path('webhook/kkiapay/', views.kkiapay_webhook, name='kkiapay_webhook'),
    # path('shows/', ShowsListView.as_view(), name='shows'),
    # path('shows/<int:type_spectacle_id>/', ShowsListView.as_view(), name='shows_by_type'),
    path('shows/', ShowsListView.as_view(), name='shows'),
    path('shows/<int:type_spectacle_id>/', ShowsListView.as_view(), name='shows_by_type'),
    path('service/', service, name='service'), 
    path('ticketdetails/<int:spectacle_id>/', ticketdetails, name='ticketdetails'),
    path('restaurant/', restaurant, name='restaurant'),
    path('reservet/', reservet, name='reservet'), 
    path('kkiapay-callback/', views.kkiapay_callback, name='kkiapay_callback'),
    path('commander/', commander, name='commander'),
    
    path('change_language/<str:language>/', views.change_language, name='change_language'),
    
    path('page_register/', page_register, name='page_register'),
    path('page_login/', page_login, name='page_login'),
    path('logout/', LogoutView.as_view(next_page=('home')), name='logout'),
    path('page_password_email/', page_password_email, name='page_password_email'),
]



