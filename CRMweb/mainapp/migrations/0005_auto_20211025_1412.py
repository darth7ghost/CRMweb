# Generated by Django 3.2.7 on 2021-10-25 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20211025_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='organizacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='organizacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='organizacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='organizacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile'),
            preserve_default=False,
        ),
    ]
