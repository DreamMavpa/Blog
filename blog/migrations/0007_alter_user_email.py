# Generated by Django 4.2 on 2023-05-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=30, unique=True, verbose_name='Email'),
        ),
    ]
