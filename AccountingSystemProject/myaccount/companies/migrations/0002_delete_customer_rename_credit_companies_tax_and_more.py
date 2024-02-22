# Generated by Django 4.2.3 on 2023-08-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='credit',
            new_name='tax',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='debt',
            new_name='telephone',
        ),
        migrations.AddField(
            model_name='companies',
            name='email',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
