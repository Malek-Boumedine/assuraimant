# Generated by Django 5.1.5 on 2025-01-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assurance', '0006_alter_user_date_de_naissance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_prospect',
            field=models.BooleanField(default=0, null=True),
        ),
    ]
