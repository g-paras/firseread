# Generated by Django 4.0.2 on 2022-02-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.IntegerField(),
        ),
    ]
