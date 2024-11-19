from django.db import transaction
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Seeder:
    @classmethod
    def seedSuperAdmin(cls):       
        super_email_or_phone = input("Enter super user email or phone:")
        super_password = input("Enter super user password:")

        with transaction.atomic():
            # Recherchons un utilisateur existant basé sur email_or_phone
            super_user, created = User.objects.get_or_create(
                email_or_phone=super_email_or_phone,
                defaults={
                    'first_name': 'Super',
                    'last_name': 'Admin',
                    'is_staff': True,
                    'is_superuser': True,  # Assurons-nous que c'est un super utilisateur
                    'is_active': True,
                }
            )

            if created:
                super_user.set_password(super_password)  # Sécurise le mot de passe
                super_user.save()
            
            print(f"Message: Success, [Email/Phone: {super_email_or_phone}, Password: **********]")

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding Super Admin...')
        Seeder.seedSuperAdmin()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the Super Admin'))