# Generated by Django 3.2.7 on 2021-10-03 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Postman_working_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='PostApp.postman'),
        ),
    ]
