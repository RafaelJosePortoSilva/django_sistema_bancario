# Generated by Django 5.0.6 on 2024-05-24 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_bancario_app', '0006_alter_contacorrente_conta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacorrente',
            name='conta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema_bancario_app.conta'),
        ),
    ]
