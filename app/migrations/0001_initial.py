# Generated by Django 5.0.3 on 2024-08-13 10:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtisteInvite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('image_artiste', models.ImageField(blank=True, null=True, upload_to='artiste_invite_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='centre_logos/')),
                ('cygle', models.CharField(blank=True, max_length=100, null=True)),
                ('adresse', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_instructeur', models.CharField(max_length=100)),
                ('prenom_instructeur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NomFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_formation', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='instrument/')),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProchainConcert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Restauration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='restaurants/')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Spectacle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_spectacle', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='spectacles/')),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ticket_disponible', models.PositiveIntegerField()),
                ('is_gratuit', models.BooleanField(default=False)),
                ('prix', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('lien_streaming', models.URLField(blank=True, null=True)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeDiffusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('is_gratuit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInstrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_instrument', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypePaiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TypeSpectacle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_or_phone', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('hostname', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login_date', models.DateTimeField(blank=True, null=True)),
                ('last_modify_date', models.DateTimeField(blank=True, null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_artistes', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='user_groups', related_query_name='user', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_permissions', related_query_name='user', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Artistes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('biographie', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='artistes/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artiste_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategorieArtiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('nationale', 'Nationale'), ('internationale', 'Internationale')], max_length=20)),
                ('nom_artiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='app.artisteinvite')),
            ],
        ),
        migrations.CreateModel(
            name='Carrousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_affiche', models.ImageField(upload_to='carrousel_images/')),
                ('prochain_concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrousels', to='app.prochainconcert')),
            ],
        ),
        migrations.CreateModel(
            name='ReserverFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('nombre_de_places', models.PositiveIntegerField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instrument')),
            ],
        ),
        migrations.CreateModel(
            name='ComanderMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=100)),
                ('nombre_commande', models.PositiveIntegerField()),
                ('date_paiement', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_valid', models.BooleanField(default=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.restauration')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_formation', models.CharField(choices=[('presentiel', 'Présentiel'), ('en_ligne', 'En ligne'), ('hybride', 'Hybride')], max_length=20)),
                ('date_formation', models.DateField()),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instrument')),
                ('nom_formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nomformation')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('nombre_billets', models.PositiveIntegerField()),
                ('cout_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('statut_paiement', models.BooleanField(default=False)),
                ('is_valid', models.BooleanField(default=True)),
                ('spectacle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.spectacle')),
            ],
        ),
        migrations.AddField(
            model_name='prochainconcert',
            name='spectacle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.spectacle'),
        ),
        migrations.CreateModel(
            name='CodeQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_qr', models.ImageField(blank=True, null=True, upload_to='codes_qr/')),
                ('token', models.CharField(max_length=32, unique=True)),
                ('code_secret', models.CharField(max_length=6, unique=True)),
                ('device_info', models.CharField(blank=True, max_length=255, null=True)),
                ('is_used', models.BooleanField(default=False)),
                ('spectacle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='code_qr', to='app.spectacle')),
            ],
        ),
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('quantity', models.PositiveIntegerField()),
                ('date_achat', models.DateTimeField(auto_now_add=True)),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('statut_paiement', models.CharField(max_length=20)),
                ('spectacle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.spectacle')),
            ],
        ),
        migrations.AddField(
            model_name='nomformation',
            name='type_instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typeinstrument'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='type_instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typeinstrument'),
        ),
        migrations.CreateModel(
            name='ReserverService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('nombre_place', models.PositiveIntegerField()),
                ('date_paiement', models.DateField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_valid', models.BooleanField(default=True)),
                ('nom_formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nomformation')),
                ('type_instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typeinstrument')),
                ('type_paiement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typepaiement')),
            ],
        ),
        migrations.AddField(
            model_name='spectacle',
            name='type_spectacle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typespectacle'),
        ),
    ]
