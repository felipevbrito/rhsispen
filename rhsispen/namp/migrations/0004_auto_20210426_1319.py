# Generated by Django 3.1.7 on 2021-04-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('namp', '0003_auto_20210425_1959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='afastamento',
            options={'ordering': ['id_afastamento'], 'verbose_name': 'Afastamento', 'verbose_name_plural': 'Afastamentos'},
        ),
    ]
