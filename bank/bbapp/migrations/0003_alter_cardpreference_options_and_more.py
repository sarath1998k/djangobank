# Generated by Django 4.0.5 on 2022-06-14 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbapp', '0002_gender_cardpreference_accountdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardpreference',
            options={'ordering': ('name',), 'verbose_name': 'Card', 'verbose_name_plural': 'cards'},
        ),
        migrations.RemoveField(
            model_name='cardpreference',
            name='district',
        ),
        migrations.RemoveField(
            model_name='cardpreference',
            name='slug',
        ),
    ]