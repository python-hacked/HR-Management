# Generated by Django 4.0.2 on 2022-10-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_alter_addstudents_due_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudents',
            name='due_amount',
            field=models.IntegerField(),
        ),
    ]
