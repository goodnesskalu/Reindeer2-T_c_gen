# Generated by Django 4.1.3 on 2022-12-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_tc_gen', '0003_alter_company_owner_alter_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='is_privacypolicy',
            field=models.BooleanField(default=False, verbose_name='IS PRIVACY POLICY'),
        ),
        migrations.AddField(
            model_name='document',
            name='is_termsandcondition',
            field=models.BooleanField(default=False, verbose_name='IS Terms and Condition'),
        ),
    ]