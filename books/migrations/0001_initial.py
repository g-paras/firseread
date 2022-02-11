# Generated by Django 4.0.2 on 2022-02-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=50)),
                ('isbn', models.ImageField(upload_to='')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]