# Generated by Django 3.2.19 on 2023-08-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_csv', '0004_alter_contacttype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacttype',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
