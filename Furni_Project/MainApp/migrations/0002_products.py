# Generated by Django 5.1 on 2024-08-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
    ]
