# Generated by Django 4.0.3 on 2022-03-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='İsim')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Güncelleşirme Tarihi')),
            ],
        ),
    ]