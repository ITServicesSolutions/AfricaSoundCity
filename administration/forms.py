from django.forms import ModelForm
from app.models import *
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email_or_phone', 'password', 'hostname', 'is_active', 'is_admin', 'is_artistes', 'is_superuser']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ArtistesForm(ModelForm):
    class Meta:
        model = Artistes
        fields = ['nom', 'biographie', 'image']


class CentreForm(ModelForm):
    class Meta:
        model = Centre
        fields = ['nom', 'logo', 'cygle', 'adresse']
        
        
class ArtisteInviteForm(ModelForm):
    class Meta:
        model = ArtisteInvite
        fields = ['nom', 'phone', 'image_artiste']
        
        
class CategorieArtisteForm(ModelForm):
    class Meta:
        model = CategorieArtiste
        fields = ['nom_artiste', 'categorie']
        
        
class TypeDiffusionForm(ModelForm):
    class Meta:
        model = TypeDiffusion
        fields = ['nom', 'is_gratuit']
        
        
class TypeSpectacleForm(ModelForm):
    class Meta:
        model = TypeSpectacle
        fields = ['type', 'is_valid']
        
        
class SpectacleForm(ModelForm):
    class Meta:
        model = Spectacle
        fields = ['type_spectacle', 'nom_spectacle', 'image', 'date', 'lieu', 'description', 
                    'ticket_disponible', 'is_gratuit', 'prix', 'heure_debut', 'heure_fin', 'lien_streaming', 'is_valid']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_debut': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'heure_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
        

class CodeQRForm(ModelForm):
    class Meta:
        model = CodeQR
        fields = ['spectacle', 'token']


class AchatForm(ModelForm):
    class Meta:
        model = Achat
        fields = ['spectacle', 'user_email', 'quantity', 'montant_total', 'transaction_id', 'statut_paiement']



class ProchainConcertForm(ModelForm):
    class Meta:
        model = ProchainConcert
        fields = ['date', 'spectacle']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
     
     
class CarrouselForm(ModelForm):
    class Meta:
        model = Carrousel
        fields = ['prochain_concert', 'image_affiche']     

        
class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom', 'email', 'spectacle', 'nombre_billets', 'cout_total', 'statut_paiement', 'is_valid']
        
        
class TypeInstrumentForm(ModelForm):
    class Meta:
        model = TypeInstrument
        fields = ['type_instrument']
        
        
class InstrumentForm(ModelForm):
    class Meta:
        model = Instrument
        fields = ['type_instrument', 'nom_instructeur', 'prenom_instructeur']
        
        
class NomFormationForm(ModelForm):
    class Meta:
        model = NomFormation
        fields = ['nom_formation', 'type_instrument', 'image', 'description', 'prix']
        
        
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['nom_formation', 'type_formation', 'instrument', 'date_formation']
        
        
class TypePaiementForm(ModelForm):
    class Meta:
        model = TypePaiement
        fields = ['nom']
        
        
class RestaurationForm(ModelForm):
    class Meta:
        model = Restauration
        fields = ['menu', 'description', 'image', 'prix']
        
        
class ComanderMenuForm(ModelForm):
    class Meta:
        model = ComanderMenu
        fields = ['menu', 'nom', 'prenoms', 'email', 'telephone', 'nombre_commande',
                  'date_paiement', 'montant', 'is_valid']
        
        
# class PaymentForm(ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['date', 'montant', 'montant_remis', 'relicat']
        
        
class ReserverFormationForm(ModelForm):
    class Meta:
        model = ReserverFormation
        fields = ['nom', 'prenom', 'email', 'telephone', 'instrument', 'nombre_de_places', 'montant']
        
        

        
        
