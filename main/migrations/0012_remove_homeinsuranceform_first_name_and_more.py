# Generated by Django 4.2.7 on 2023-12-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_cname_homeinsuranceform_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeinsuranceform',
            name='first_name',
        ),
        migrations.AddField(
            model_name='homeinsuranceform',
            name='first_name1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
