# Generated by Django 3.2.7 on 2021-10-26 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20211025_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='organizacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile'),
            preserve_default=False,
        ),
    ]
