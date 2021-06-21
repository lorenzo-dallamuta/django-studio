# Generated by Django 3.2 on 2021-06-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='hobby',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='sesso',
            field=models.CharField(blank=True, choices=[('M', 'uomo'), ('F', 'donna')], max_length=1),
        ),
    ]