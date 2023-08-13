# Generated by Django 4.1.7 on 2023-08-13 10:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csr', '0006_alter_gasutilservicerequest_resolved_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasutilservicerequest',
            name='resolved_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 10, 42, 14, 996701, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='gasutilservicerequest',
            name='service_paid_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 10, 42, 14, 996701, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='GasUtilServiceRequestAttachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='attachments')),
                ('gas_util_service_request_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csr.gasutilservicerequest')),
            ],
            options={
                'db_table': 'gas_util_service_request_attachments',
            },
        ),
    ]
