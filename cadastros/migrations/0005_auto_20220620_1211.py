# Generated by Django 2.2.12 on 2022-06-20 15:11

import cadastros.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_auto_20220615_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprovante',
            name='arquivo',
            field=models.FileField(upload_to=cadastros.models.user_path),
        ),
    ]
