# Generated by Django 3.2.7 on 2021-10-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='es_agente',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='es_organizador',
            field=models.BooleanField(default=True),
        ),
    ]
