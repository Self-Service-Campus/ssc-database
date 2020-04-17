# Generated by Django 3.0.5 on 2020-04-17 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id_dep', models.AutoField(primary_key=True, serialize=False)),
                ('name_dep', models.CharField(max_length=150)),
                ('acron_dep', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id_port', models.AutoField(primary_key=True, serialize=False)),
                ('number_port', models.IntegerField()),
                ('ip_addr_port', models.GenericIPAddressField()),
                ('state_port', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VLAN',
            fields=[
                ('identifier_vlan', models.IntegerField(primary_key=True, serialize=False)),
                ('description_vlan', models.CharField(max_length=350)),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssc_db_app.Port')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ssc_db_app.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('identifier_switch', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('model_switch', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssc_db_app.Department')),
            ],
        ),
        migrations.AddField(
            model_name='port',
            name='switch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssc_db_app.Switch'),
        ),
        migrations.CreateModel(
            name='Audit_Log',
            fields=[
                ('id_audit', models.AutoField(primary_key=True, serialize=False)),
                ('action_audit', models.CharField(max_length=350)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssc_db_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id_acl', models.AutoField(primary_key=True, serialize=False)),
                ('access_flag_acl', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ssc_db_app.User')),
            ],
        ),
    ]
