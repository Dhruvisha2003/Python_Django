# Generated by Django 5.0.3 on 2024-08-28 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=20)),
            ],
        ),
    ]