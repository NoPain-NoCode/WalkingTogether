# Generated by Django 3.2.6 on 2021-08-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_pet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name': '반려동물', 'verbose_name_plural': '반려동물'},
        ),
        migrations.AlterField(
            model_name='socialplatform',
            name='platform',
            field=models.CharField(default=0, max_length=20, unique=True),
        ),
    ]