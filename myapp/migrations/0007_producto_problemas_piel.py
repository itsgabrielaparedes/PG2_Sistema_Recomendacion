# Generated by Django 4.2.4 on 2023-09-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_usuarioo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='problemas_piel',
            field=models.CharField(default='Sin problemas', max_length=500),
            preserve_default=False,
        ),
    ]
