# Generated by Django 4.0.2 on 2022-03-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Uom',
                'verbose_name_plural': 'Uoms',
                'db_table': 'unit_of_measure',
                'managed': True,
            },
        ),
    ]
