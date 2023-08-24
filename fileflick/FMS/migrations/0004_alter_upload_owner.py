# Generated by Django 4.1.10 on 2023-08-24 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FMS', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='uploads', to=settings.AUTH_USER_MODEL),
        ),
    ]
