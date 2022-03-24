# Generated by Django 4.0.3 on 2022-03-24 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_form_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='formitems',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.form'),
        ),
    ]
