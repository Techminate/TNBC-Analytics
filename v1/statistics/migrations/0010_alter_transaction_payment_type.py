# Generated by Django 3.2.5 on 2021-09-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0009_transaction_txs_sent_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_type',
            field=models.CharField(choices=[('NEW', 'New'), ('TIMESHEET', 'Timesheet'), ('PROJECT', 'Project'), ('BOUNTY', 'Bounty'), ('MISCELLANEOUS', 'Miscellaneous'), ('INTERNAL', 'Internal'), ('UNIDENTIFIED', 'Unidentified'), ('IS_FEE', 'Is Fee')], max_length=255),
        ),
    ]