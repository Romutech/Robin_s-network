# Generated by Django 4.0 on 2021-12-28 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to='auth.user')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('profession', models.CharField(max_length=50, null=True)),
                ('residence', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
