# Generated by Django 5.1.2 on 2024-11-15 07:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_resetuuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertable',
            name='u_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserTable',
        ),
    ]