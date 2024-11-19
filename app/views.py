# Standard library imports
from datetime import date, datetime

# Django imports
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from django.utils.encoding import force_bytes, force_str
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import activate
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

# Django REST Framework imports
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import *
from .serializers import *
from app.function import *

User = get_user_model()

class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        self.send_registration_email(user)

    def send_registration_email(self, user):
        subject = 'Bienvenue sur AfricaSoundCity'
        html_message = render_to_string('authentication/registration_email.html', {'user': user})
        plain_message = strip_tags(html_message)
        from_email = 'jenniferstallone8@gmail.com'
        to_email = [user.email_or_phone]
        send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return render(request, 'authentication/200_registration_email.html', status=200)


@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = get_user_model().objects.get(pk=user_id)
        user.delete()
        return Response({'message': f'User with ID {user_id} has been deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except get_user_model().DoesNotExist:
        return Response({'message': f'User with ID {user_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        email_or_phone = request.data.get('email_or_phone')
        password = request.data.get('password')

        user = authenticate(request, email_or_phone=email_or_phone, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser or user.is_staff:
                return JsonResponse({'message': 'Authentification réussie.', 'redirect_url': '/administration/'})
            else:
                return JsonResponse({'message': 'Authentification réussie.', 'redirect_url': '/'})
        else:
            return JsonResponse({'error': 'Identifiant ou mot de passe incorrect.'}, status=400)
    else:
        return Response({'error': 'La méthode HTTP doit être POST.'}, status=405)

@api_view(['POST'])
def reset_password_email(request):
    if request.method == 'POST':
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'Utilisateur non trouvé.'}, status=status.HTTP_404_NOT_FOUND)

        token = default_token_generator.make_token(user)
        uri = urlsafe_base64_encode(force_bytes(user.pk))

        # Construire l'URL complète
        # reset_url = f'http://localhost:8000/reset-password/{uri}/{token}'
        reset_url = request.build_absolute_uri(reverse('reset_password_confirm', kwargs={'uidb64': uri, 'token': token}))

        # Envoyer l'e-mail avec le lien de réinitialisation de mot de passe
        subject = 'Réinitialisation de mot de passe'
        html_message = render_to_string('authentication/reset_message.html', {'reset_url': reset_url, 'email': email})

        from_email = 'jenniferstallone8@gmail.com'
        to_email = [user.email]

        try:
            send_mail(subject, '', from_email, to_email, html_message=html_message, fail_silently=False)
            # return Response({'message': 'Un e-mail de réinitialisation de mot de passe a été envoyé.'}, status=status.HTTP_200_OK)
            return render(request, 'authentication/200_reset_password_email_sent.html')
        except BadHeaderError:
            # return Response({'message': 'Erreur lors de l\'envoi de l\'e-mail.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return render(request, 'authentication/500_reset_password_email_sent.html')
        except (DjangoValidationError, DRFValidationError) as e:
            # return Response({'message': 'Erreur lors de la validation des données.', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)
            return render(request, 'authentication/400_reset_password_email_sent.html')
    else:
        return Response({'message': 'Méthode non autorisée.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def reset_password_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('page_login')
        else:
            form = SetPasswordForm(user)

        return render(request, 'authentication/reset_password_confirm.html', {'form': form, 'uidb64': uidb64, 'token': token})

    else:
        messages.error(request, 'Ce lien de réinitialisation de mot de passe est invalide.')
        return redirect('page_password_email')

class RendreArtisteView(APIView):
    def post(self, request, user_id):
        # Récupérez les données soumises par l'utilisateur
        serializer = ArtistesSerializer(data=request.data)
        if serializer.is_valid():
            # Créez une instance du modèle Artistes
            artiste = serializer.save(user_id=user_id)
            # Mettez à jour l'utilisateur pour le marquer comme artiste
            user = User.objects.get(pk=user_id)
            user.is_artistes = True
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArtistesListView(APIView):
    def get(self, request):
        artistes = Artistes.objects.all()  # Récupère tous les artistes
        serializer = ArtistesSerializer(artistes, many=True)  # Sérialise la liste des artistes
        return Response(serializer.data, status=status.HTTP_200_OK)

class CodeQRListCreateAPIView(generics.ListCreateAPIView):
    queryset = CodeQR.objects.all()
    serializer_class = CodeQRSerializer

class CodeQRRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CodeQR.objects.all()
    serializer_class = CodeQRSerializer

class GenererCodeQRView(generics.CreateAPIView):
    queryset = Spectacle.objects.all()
    serializer_class = SpectacleSerializer

    def post(self, request, *args, **kwargs):
        spectacle = self.get_object()
        code_qr = spectacle.generer_code_qr()
        serializer = CodeQRSerializer(code_qr)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def delete(self, request, *args, **kwargs):
        spectacle = self.get_object()
        code_qr = spectacle.code_qr
        if code_qr:
            code_qr.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        spectacle = self.get_object()
        code_qr = spectacle.code_qr
        if code_qr:
            serializer = CodeQRSerializer(code_qr)
            return Response(serializer.data)
        else:
            rcode_qr = spectacle.generer_code_qr()
            serializer = CodeQRSerializer(code_qr)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def regenerate_qr_codes(request):
    CodeQR.objects.all().delete()

    for spectacle in Spectacle.objects.all():
        spectacle.generer_code_qr()

    return HttpResponse("Codes QR régénérés avec succès.")


###################    La vue des pages    ###################
def change_language(request, language):
    activate(language_code)
    if language:
        translation.activate(language)
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def countdown(request):
    # Récupérer la prochaine date de concert à partir de la base de données
    prochain_evenement = ProchainConcert.objects.select_related('spectacle').first()
    return render(request, 'countdown.html', {'prochain_evenement': prochain_evenement,})

def home(request):
    
    spectacles = manage_spectacles(action='list')
    centres = manage_centres(action='list')
    
    prochain_evenement = ProchainConcert.objects.first()
    prochainconcert = ProchainConcert.objects.all()
    
    # carrousel = ProchainConcert.objects.first()
    carrousels = Carrousel.objects.all()

    context = {
        'spectacles': spectacles,
        'centres': centres,
        'prochain_evenement': prochain_evenement,
        'prochainconcert': prochainconcert,
        'carrousels': carrousels,
    }
    

    return render(request, 'control_user/pages/index.html', context)

def streamings(request):
    spectacles = manage_spectacles(action='list')
    return render(request, 'control_user/pages/streamings.html', {'spectacles': spectacles})

@login_required
def access_streaming(request, spectacle_id):
    spectacle = get_object_or_404(Spectacle, pk=spectacle_id)
    device_info = request.META['HTTP_USER_AGENT']  # Utiliser le user agent comme information sur l'appareil

    if request.method == 'POST':
        code_input = ''.join([
            request.POST.get(f'code_digit_{i}', '') for i in range(1, 7)
        ])
        try:
            code_qr = CodeQR.objects.get(spectacle=spectacle, code_secret=code_input)

            if code_qr.is_used:
                if code_qr.device_info != device_info:
                    error_message = "Ce code secret a déjà été utilisé sur un autre appareil."
                    return render(request, 'control_user/pages/access_streaming.html', {
                        'spectacle': spectacle,
                        'error_message': error_message,
                    })
            else:
                code_qr.is_used = True
                code_qr.device_info = device_info
                code_qr.save()
                success_message = "Votre code est correct."
                return render(request, 'control_user/pages/access_streaming.html', {
                    'spectacle': spectacle,
                    'success_message': success_message,
                    'streaming_url': redirect('streaming_content', spectacle_id=spectacle.id).url,
                })
        except CodeQR.DoesNotExist:
            error_message = "Le code secret est incorrect. Veuillez réessayer."
            return render(request, 'control_user/pages/access_streaming.html', {
                'spectacle': spectacle,
                'error_message': error_message,
            })
    return render(request, 'control_user/pages/access_streaming.html', {'spectacle': spectacle})

def create_kkiapay_session(request, spectacle_id):
    spectacle = Spectacle.objects.get(id=spectacle_id)
    quantity = int(request.GET.get('quantity', 1))
    total_amount = int(spectacle.prix * quantity * 100)
    
    redirect_url = f"https://kkiapay.me/api/paymentlink?amount={total_amount}&apikey={settings.KKIAPAY_API_KEY}&custom_data[spectacle_id]={spectacle.id}&custom_data[quantity]={quantity}&callback_url={request.build_absolute_uri('/webhook/kkiapay/')}"
   
    return redirect(redirect_url)

def envoyer_codes_secrets_par_email(email, tickets_codes, spectacle):
    if len(tickets_codes) == 1:
        sujet = 'Votre code secret pour le streaming payant'
    else:
        sujet = 'Vos codes secrets pour le streaming payant'

    message = render_to_string('control_user/pages/codes_secrets_email.html', {
        'tickets_codes': tickets_codes,
        'spectacle': spectacle,
        'single_ticket': len(tickets_codes) == 1
    })
    destinataires = [email]
    send_mail(sujet, message, None, destinataires)

@csrf_exempt
def kkiapay_webhook(request):
    import json
    payload = json.loads(request.body)
   
    if payload['status'] == 'SUCCESS':
        customer_email = payload.get('customer_email')
        spectacle_id = payload.get('custom_data', {}).get('spectacle_id')
        quantity = int(payload.get('custom_data', {}).get('quantity', 1))
        montant_total = payload.get('amount')
        transaction_id = payload.get('transaction_id')
       
        if customer_email and spectacle_id:
            try:
                spectacle = Spectacle.objects.get(id=spectacle_id)
                
                achat = Achat.objects.create(
                    spectacle=spectacle,
                    user_email=customer_email,
                    quantity=quantity,
                    montant_total=montant_total,
                    transaction_id=transaction_id,
                    statut_paiement='SUCCESS'
                )
                
                tickets_codes = []
                for i in range(quantity):
                    code_qr = spectacle.generer_code_qr()
                    tickets_codes.append({
                        'numero': i + 1,
                        'code': code_qr.code_secret
                    })
                
                envoyer_codes_secrets_par_email(customer_email, tickets_codes, spectacle)
                
            except Spectacle.DoesNotExist:
                return JsonResponse({'status': 'spectacle not found'}, status=404)

    return JsonResponse({'status': 'success'}, status=200)

def service(request):
    formations = manage_nom_formations(action='list')

    return render(request, 'control_user/pages/service.html', {'formations': formations})

def reservet(request):
    instrument = request.GET.get('instrument', '')
    prix = request.GET.get('prix', '')
    context = {
        'formation': {'type_instrument': instrument},
        'prix': prix
    }
    return render(request, 'control_user/pages/reservet.html', context)

@csrf_exempt
def kkiapay_callback(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        amount = request.POST.get('amount')
        
        nom = request.POST.get('last_name')
        prenom = request.POST.get('first_name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        instrument_id = request.POST.get('instrument')
        nombre_places = request.POST.get('nombrePlaces')
        
        instrument = Instrument.objects.get(id=instrument_id)
        reservation = ReserverFormation.objects.create(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            instrument=instrument,
            nombre_de_places=nombre_places,
            montant=amount
        )
        
        template = get_template('control_user/pages/recu.html')
        html = template.render({
            'reservation': reservation,
            'instructeur': f"{instrument.nom_instructeur} {instrument.prenom_instructeur}"
        })
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        
        email = EmailMessage(
            'Reçu de paiement pour votre réservation',
            'Veuillez trouver ci-joint le reçu de votre paiement.',
            'jenniferstallone8@gmail.com',
            [reservation.email]
        )
        email.attach('recu.pdf', result.getvalue(), 'application/pdf')
        email.send()
        
        return HttpResponse('OK', status=200)
    return HttpResponse('Method not allowed', status=405)

def commander(request):
    return render(request, 'control_user/pages/commander.html')

def ticketdetails(request, spectacle_id):
    spectacle = manage_spectacles(action='retrieve', instance_id=spectacle_id)
    return render(
        request, 
        'control_user/pages/ticketdetails.html', 
        {
            'spectacle': spectacle, 
            'kkiapay_api_key': 'kkiapay_api_key', 
            'kkiapay_callback_url': 'kkiapay_callback_url'
        }
    )

class ShowsListView(ListView):
    template_name = 'control_user/pages/shows.html'
    context_object_name = 'spectacles'

    def get_queryset(self):
        # Récupérer la liste des spectacles via la fonction utilitaire
        spectacles = manage_spectacles(action='list')
        if not isinstance(spectacles, list):
            spectacles = []  # Gestion d'erreur si la fonction utilitaire retourne un message d'erreur

        type_spectacle_id = self.kwargs.get('type_spectacle_id')

        queryset = []
        for spectacle in spectacles:
            try:
                date_spectacle = datetime.strptime(spectacle.get('date'), '%Y-%m-%d').date()
                if date_spectacle >= date.today():  # Filtrer les spectacles à venir
                    spectacle_data = {
                        'type_spectacle': spectacle.get('type_spectacle'),
                        'nom_spectacle': spectacle.get('nom_spectacle'),
                        'image': spectacle.get('image'),
                        'date': date_spectacle,
                        'lieu': spectacle.get('lieu'),
                        'description': spectacle.get('description'),
                        'ticket_disponible': spectacle.get('ticket_disponible'),
                        'is_gratuit': spectacle.get('is_gratuit'),
                        'prix': spectacle.get('prix'),
                        'heure_debut': spectacle.get('heure_debut'),
                        'heure_fin': spectacle.get('heure_fin'),
                        'is_valid': spectacle.get('is_valid'),
                    }
                    if type_spectacle_id:
                        if str(type_spectacle_id) == str(spectacle_data['type_spectacle']):
                            queryset.append(spectacle_data)
                    else:
                        queryset.append(spectacle_data)
            except Exception as e:
                print(f"Error processing spectacle data: {e}")
                continue

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer la liste des types de spectacles via la fonction utilitaire
        typespectacles = manage_type_spectacles(action='list')
        context['typespectacles'] = typespectacles if isinstance(typespectacles, list) else []

        return context

def restaurant(request):
    restaurants = manage_restauration(action='list')
    
    return render(request, 'control_user/pages/restaurant.html', {'restaurants': restaurants})

def page_register(request):
    return render(request, 'authentication/authentication-register.html')

def page_login(request):
	return render(request, 'authentication/authentication-login.html')

def page_password_email(request):
	return render(request, 'authentication/reset_password_email.html')