# Generated by Django 3.2.19 on 2023-08-27 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('change_csv', '0002_auto_20230827_1052'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModelForBuild2',
            new_name='CounterAgent',
        ),
        migrations.RenameField(
            model_name='cellvalue',
            old_name='modelforbuild2',
            new_name='counteragent',
        ),
    ]
