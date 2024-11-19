from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from app.models import *
from app.serializers import *

def manage_type_spectacles(action, data=None, instance_id=None):
    """
    Fonction pour gérer les opérations CRUD sur les objets TypeSpectacle.
    
    :param action: L'action à effectuer ('list', 'retrieve', 'create', 'update', 'delete').
    :param data: Les données nécessaires pour créer ou mettre à jour un objet.
    :param instance_id: L'ID de l'objet à récupérer, mettre à jour ou supprimer.
    :return: Les données sérialisées ou un message d'état.
    """
    try:
        if action == 'list':
            queryset = TypeSpectacle.objects.all()
            serializer = TypeSpectacleSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = TypeSpectacle.objects.get(id=instance_id)
            serializer = TypeSpectacleSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = TypeSpectacleSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = TypeSpectacle.objects.get(id=instance_id)
            serializer = TypeSpectacleSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = TypeSpectacle.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'TypeSpectacle supprimé avec succès'}
        
    except ObjectDoesNotExist:
        return {'error': f"L'objet avec l'ID {instance_id} n'existe pas."}
    except Exception as e:
        return {'error': str(e)}

def manage_type_spectacles(action, data=None, instance_id=None):
    """
    Fonction utilitaire pour gérer les opérations CRUD sur les objets TypeSpectacle.

    :param action: L'action à effectuer ('list', 'retrieve', 'create', 'update', 'delete').
    :param data: Les données nécessaires pour créer ou mettre à jour un objet.
    :param instance_id: L'ID de l'objet à récupérer, mettre à jour ou supprimer.
    :return: Les données sérialisées ou un message d'état.
    """
    try:
        if action == 'list':
            queryset = TypeSpectacle.objects.all()
            serializer = TypeSpectacleSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = TypeSpectacle.objects.get(id=instance_id)
            serializer = TypeSpectacleSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = TypeSpectacleSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = TypeSpectacle.objects.get(id=instance_id)
            serializer = TypeSpectacleSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = TypeSpectacle.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'TypeSpectacle supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'TypeSpectacle introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_spectacles(action, data=None, instance_id=None):
    """
    Fonction utilitaire pour gérer les opérations CRUD sur les objets Spectacle.

    :param action: L'action à effectuer ('list', 'retrieve', 'create', 'update', 'delete').
    :param data: Les données nécessaires pour créer ou mettre à jour un objet.
    :param instance_id: L'ID de l'objet à récupérer, mettre à jour ou supprimer.
    :return: Les données sérialisées ou un message d'état.
    """
    try:
        if action == 'list':
            queryset = Spectacle.objects.all()
            serializer = SpectacleSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = Spectacle.objects.get(id=instance_id)
            serializer = SpectacleSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = SpectacleSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = Spectacle.objects.get(id=instance_id)
            serializer = SpectacleSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = Spectacle.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'Spectacle supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'Spectacle introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_centres(action, data=None, instance_id=None):
    """
    Fonction utilitaire pour gérer les opérations CRUD sur les objets Centre.

    :param action: L'action à effectuer ('list', 'retrieve', 'create', 'update', 'delete').
    :param data: Les données nécessaires pour créer ou mettre à jour un objet.
    :param instance_id: L'ID de l'objet à récupérer, mettre à jour ou supprimer.
    :return: Les données sérialisées ou un message d'état.
    """
    try:
        if action == 'list':
            queryset = Centre.objects.all()
            serializer = CentreSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = Centre.objects.get(id=instance_id)
            serializer = CentreSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = CentreSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = Centre.objects.get(id=instance_id)
            serializer = CentreSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = Centre.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'Centre supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'Centre introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_reservations(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = Reservation.objects.all()
            serializer = ReservationSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = Reservation.objects.get(id=instance_id)
            serializer = ReservationSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = ReservationSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = Reservation.objects.get(id=instance_id)
            serializer = ReservationSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = Reservation.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'Reservation supprimée avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'Reservation introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_type_instruments(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = TypeInstrument.objects.all()
            serializer = TypeInstrumentSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = TypeInstrument.objects.get(id=instance_id)
            serializer = TypeInstrumentSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = TypeInstrumentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = TypeInstrument.objects.get(id=instance_id)
            serializer = TypeInstrumentSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = TypeInstrument.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'TypeInstrument supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'TypeInstrument introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_instruments(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = Instrument.objects.all()
            serializer = InstrumentSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = Instrument.objects.get(id=instance_id)
            serializer = InstrumentSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = InstrumentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = Instrument.objects.get(id=instance_id)
            serializer = InstrumentSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = Instrument.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'Instrument supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'Instrument introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_nom_formations(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = NomFormation.objects.all()
            serializer = NomFormationSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = NomFormation.objects.get(id=instance_id)
            serializer = NomFormationSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = NomFormationSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = NomFormation.objects.get(id=instance_id)
            serializer = NomFormationSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = NomFormation.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'NomFormation supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'NomFormation introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_services(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = Service.objects.all()
            serializer = ServiceSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = Service.objects.get(id=instance_id)
            serializer = ServiceSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = ServiceSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = Service.objects.get(id=instance_id)
            serializer = ServiceSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = Service.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'Service supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'Service introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_type_paiements(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = TypePaiement.objects.all()
            serializer = TypePaiementSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = TypePaiement.objects.get(id=instance_id)
            serializer = TypePaiementSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = TypePaiementSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = TypePaiement.objects.get(id=instance_id)
            serializer = TypePaiementSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = TypePaiement.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'TypePaiement supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'TypePaiement introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_reserver_services(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = ReserverService.objects.all()
            serializer = ReserverServiceSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = ReserverService.objects.get(id=instance_id)
            serializer = ReserverServiceSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = ReserverServiceSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = ReserverService.objects.get(id=instance_id)
            serializer = ReserverServiceSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = ReserverService.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'ReserverService supprimé avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'ReserverService introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_restauration(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = Restauration.objects.all()
            serializer = RestaurationSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = Restauration.objects.get(id=instance_id)
            serializer = RestaurationSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = RestaurationSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = Restauration.objects.get(id=instance_id)
            serializer = RestaurationSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = Restauration.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'Restauration supprimée avec succès'}

    except ObjectDoesNotExist:
        return {'error': 'Restauration introuvable'}
    except Exception as e:
        return {'error': str(e)}

def manage_comander_menu(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = ComanderMenu.objects.all()
            serializer = ComanderMenuSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = ComanderMenu.objects.get(id=instance_id)
            serializer = ComanderMenuSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = ComanderMenuSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = ComanderMenu.objects.get(id=instance_id)
            serializer = ComanderMenuSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = ComanderMenu.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'ComanderMenu deleted successfully'}

    except ObjectDoesNotExist:
        return {'error': 'ComanderMenu not found'}
    except Exception as e:
        return {'error': str(e)}

def manage_reserver_formation(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = ReserverFormation.objects.all()
            serializer = ReserverFormationSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = ReserverFormation.objects.get(id=instance_id)
            serializer = ReserverFormationSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = ReserverFormationSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = ReserverFormation.objects.get(id=instance_id)
            serializer = ReserverFormationSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = ReserverFormation.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'ReserverFormation deleted successfully'}

    except ObjectDoesNotExist:
        return {'error': 'ReserverFormation not found'}
    except Exception as e:
        return {'error': str(e)}

def manage_artiste_invite(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = ArtisteInvite.objects.all()
            serializer = ArtisteInviteSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = ArtisteInvite.objects.get(id=instance_id)
            serializer = ArtisteInviteSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = ArtisteInviteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = ArtisteInvite.objects.get(id=instance_id)
            serializer = ArtisteInviteSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = ArtisteInvite.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'ArtisteInvite deleted successfully'}

    except ObjectDoesNotExist:
        return {'error': 'ArtisteInvite not found'}
    except Exception as e:
        return {'error': str(e)}

def manage_categorie_artiste(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = CategorieArtiste.objects.all()
            serializer = CategorieArtisteSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = CategorieArtiste.objects.get(id=instance_id)
            serializer = CategorieArtisteSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = CategorieArtisteSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = CategorieArtiste.objects.get(id=instance_id)
            serializer = CategorieArtisteSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = CategorieArtiste.objects.get(id=instance_id)
            instance.delete()
            return {'message': 'CategorieArtiste deleted successfully'}

    except ObjectDoesNotExist:
        return {'error': 'CategorieArtiste not found'}
    except Exception as e:
        return {'error': str(e)}

def manage_user(action, data=None, instance_id=None):
    try:
        if action == 'list':
            queryset = get_user_model().objects.all()
            serializer = RegisterUserSerializer(queryset, many=True)
            return serializer.data

        if action == 'retrieve':
            instance = get_user_model().objects.get(id=instance_id)
            serializer = RegisterUserSerializer(instance)
            return serializer.data

        if action == 'create':
            serializer = RegisterUserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'update':
            instance = get_user_model().objects.get(id=instance_id)
            serializer = RegisterUserSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data

        if action == 'delete':
            instance = get_user_model().objects.get(id=instance_id)
            instance.delete()
            return {'message': 'User deleted successfully'}

    except get_user_model().DoesNotExist:
        return {'error': 'User not found'}
    except Exception as e:
        return {'error': str(e)}