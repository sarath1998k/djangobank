# Generated by Django 4.0.5 on 2022-06-14 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('wiki', models.URLField()),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbapp.district')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
                'ordering': ('name',),
            },
        ),
    ]
