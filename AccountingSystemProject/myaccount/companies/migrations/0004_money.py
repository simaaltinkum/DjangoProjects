# Generated by Django 4.2.3 on 2023-08-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_companies_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt', models.IntegerField(default=0)),
                ('credit', models.IntegerField(default=0)),
            ],
        ),
    ]