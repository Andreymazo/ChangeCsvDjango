# Generated by Django 3.2.19 on 2023-08-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_csv', '0003_remove_person_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacttype',
            name='name',
            field=models.CharField(default='ModelProkladka', max_length=100),
        ),
    ]
