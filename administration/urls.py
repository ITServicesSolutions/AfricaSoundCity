from django.urls import path
from .views import *
from . import views
from app.views import *

urlpatterns = [
    
    path('', views.administration, name='administration'), 
    # path('create_superadmin/', AdminUserCreateAPIView.as_view(), name='create_superadmin'),
    
    
    path('users/', UserList, name='UserList'),
    path('users/create/', UserCreate, name='UserCreate'),
    path('users/update/<int:pk>/', UserUpdate, name='UserUpdate'),
    path('users/delete/<int:pk>/', UserDelete, name='UserDelete'),
    
    path('create_superadmin/', page_register, name='create_superadmin'),
    path('artistes/', ArtistesList, name='ArtistesList'),
    path('artistes/create/', ArtistesCreate, name='ArtistesCreate'),
    path('artistes/update/<int:pk>/', ArtistesUpdate, name='ArtistesUpdate'),
    path('artistes/delete/<int:pk>/', ArtistesDelete, name='ArtistesDelete'),
    
    path('centre/', CentreList, name='CentreList'),
    path('centre/create/', CentreCreate, name='CentreCreate'),
    path('centre/update/<int:pk>/', CentreUpdate, name='CentreUpdate'),
    path('centre/delete/<int:pk>/', CentreDelete, name='CentreDelete'),
    
    path('artisteInvite/', ArtisteInviteList, name='ArtisteInviteList'),
    path('artisteInvite/create/', ArtisteInviteCreate, name='ArtisteInviteCreate'),
    path('artisteInvite/update/<int:pk>/', ArtisteInviteUpdate, name='ArtisteInviteUpdate'),
    path('artisteInvite/delete/<int:pk>/', ArtisteInviteDelete, name='ArtisteInviteDelete'),
    
    path('categorieArtiste/', CategorieArtisteList, name='CategorieArtisteList'),
    path('categorieArtiste/create/', CategorieArtisteCreate, name='CategorieArtisteCreate'),
    path('categorieArtiste/update/<int:pk>/', CategorieArtisteUpdate, name='CategorieArtisteUpdate'),
    path('categorieArtiste/delete/<int:pk>/', CategorieArtisteDelete, name='CategorieArtisteDelete'),
    
    path('typeDiffusion/', TypeDiffusionList, name='TypeDiffusionList'),
    path('typeDiffusion/create/', TypeDiffusionCreate, name='TypeDiffusionCreate'),
    path('typeDiffusion/update/<int:pk>/', TypeDiffusionUpdate, name='TypeDiffusionUpdate'),
    path('typeDiffusion/delete/<int:pk>/', TypeDiffusionDelete, name='TypeDiffusionDelete'),
    
    path('typeSpectacle/', TypeSpectacleList, name='TypeSpectacleList'),
    path('typeSpectacle/create/', TypeSpectacleCreate, name='TypeSpectacleCreate'),
    path('typeSpectacle/update/<int:pk>/', TypeSpectacleUpdate, name='TypeSpectacleUpdate'),
    path('typeSpectacle/delete/<int:pk>/', TypeSpectacleDelete, name='TypeSpectacleDelete'),
    
    path('spectacle/', SpectacleList, name='SpectacleList'),
    path('spectacle/create/', SpectacleCreate, name='SpectacleCreate'),
    path('spectacle/update/<int:pk>/', SpectacleUpdate, name='SpectacleUpdate'),
    path('spectacle/delete/<int:pk>/', SpectacleDelete, name='SpectacleDelete'),

    path('achat/', AchatList, name='AchatList'),
    path('statistiques/', statistiques, name='statistiques'),
    
    path('codeQR/', CodeQRList, name='CodeQRList'),
    path('codeQR/create/', CodeQRCreate, name='CodeQRCreate'),
    path('codeQR/update/<int:pk>/', CodeQRUpdate, name='CodeQRUpdate'),
    path('codeQR/delete/<int:pk>/', CodeQRDelete, name='CodeQRDelete'),
    
    path('prochainConcert/', ProchainConcertList, name='ProchainConcertList'),
    path('prochainConcert/create/', ProchainConcertCreate, name='ProchainConcertCreate'),
    path('prochainConcert/update/<int:pk>/', ProchainConcertUpdate, name='ProchainConcertUpdate'),
    path('prochainConcert/delete/<int:pk>/', ProchainConcertDelete, name='ProchainConcertDelete'),
    
    path('carrousel/', CarrouselList, name='CarrouselList'),
    path('carrousel/create/', CarrouselCreate, name='CarrouselCreate'),
    path('carrousel/update/<int:pk>/', CarrouselUpdate, name='CarrouselUpdate'),
    path('carousel/delete/<int:pk>/', CarrouselDelete, name='CarrouselDelete'),
    
    path('reservation/', ReservationList, name='ReservationList'),
    path('reservation/create/', ReservationCreate, name='ReservationCreate'),
    path('reservation/update/<int:pk>/', ReservationUpdate, name='ReservationUpdate'),
    path('reservation/delete/<int:pk>/', ReservationDelete, name='ReservationDelete'),
    
    path('typeInstrument/', TypeInstrumentList, name='TypeInstrumentList'),
    path('typeInstrument/create/', TypeInstrumentCreate, name='TypeInstrumentCreate'),
    path('typeInstrument/update/<int:pk>/', TypeInstrumentUpdate, name='TypeInstrumentUpdate'),
    path('typeInstrument/delete/<int:pk>/', TypeInstrumentDelete, name='TypeInstrumentDelete'),
    
    path('instrument/', InstrumentList, name='InstrumentList'),
    path('instrument/create/', InstrumentCreate, name='InstrumentCreate'),
    path('instrument/update/<int:pk>/', InstrumentUpdate, name='InstrumentUpdate'),
    path('instrument/delete/<int:pk>/', InstrumentDelete, name='InstrumentDelete'),
    
    path('nomFormation/', NomFormationList, name='NomFormationList'),
    path('nomFormation/create/', NomFormationCreate, name='NomFormationCreate'),
    path('nomFormation/update/<int:pk>/', NomFormationUpdate, name='NomFormationUpdate'),
    path('nomFormation/delete/<int:pk>/', NomFormationDelete, name='NomFormationDelete'),
    
    
    path('restauration/', RestaurationList, name='RestaurationList'),
    path('restauration/create/', RestaurationCreate, name='RestaurationCreate'),
    path('restauration/update/<int:pk>/', RestaurationUpdate, name='RestaurationUpdate'),
    path('restauration/delete/<int:pk>/', RestaurationDelete, name='RestaurationDelete'),
    
    path('comanderMenu/', ComanderMenuList, name='ComanderMenuList'),
    path('comanderMenu/delete/<int:pk>/', ComanderMenuDelete, name='ComanderMenuDelete'),
    
    path('reserverFormation/', ReserverFormationList, name='ReserverFormationList'),
    path('reserverFormation/create/', ReserverFormationCreate, name='ReserverFormationCreate'),
    path('reserverFormation/update/<int:pk>/', ReserverFormationUpdate, name='ReserverFormationUpdate'),
    path('reserverFormation/delete/<int:pk>/', ReserverFormationDelete, name='ReserverFormationDelete'),
]