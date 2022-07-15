# Generated by Django 3.2.7 on 2021-11-14 03:23

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment_date',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('timeslot_id', models.IntegerField(blank=True, null=True)),
                ('taken', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('madeon', models.DateField()),
                ('aptdatetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='doctorstaff',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('discipline', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='patients',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ssn', models.PositiveIntegerField()),
                ('dob', models.DateField()),
                ('height', models.FloatField()),
                ('gender', models.CharField(max_length=1)),
                ('ethnicity', models.CharField(blank=True, max_length=20, null=True)),
                ('job', models.CharField(blank=True, max_length=50, null=True)),
                ('smoking', models.BooleanField(blank=True, null=True)),
                ('familyhistory', models.TextField(blank=True, null=True)),
                ('address1', models.CharField(blank=True, max_length=50, null=True)),
                ('address2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('weight', models.FloatField()),
                ('doctorID', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='slots',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('start_time', models.TextField()),
                ('end_time', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(default=0)),
                ('symptom', models.TextField(max_length=200)),
                ('condition', models.TextField(max_length=200)),
                ('notes', models.TextField(max_length=500)),
                ('followupbool', models.BooleanField(default=False)),
                ('appointmentno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telemedicine.appointments')),
            ],
        ),
        migrations.CreateModel(
            name='recordings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoURL', models.URLField()),
                ('messageURL', models.URLField()),
                ('visitno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telemedicine.visits')),
            ],
        ),
        migrations.CreateModel(
            name='prescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicinename', models.TextField(max_length=200)),
                ('dosage', models.CharField(max_length=200)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('patientno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telemedicine.patients')),
            ],
        ),
        migrations.CreateModel(
            name='medicationsallergies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medications', models.TextField(max_length=200)),
                ('enddatemedications', models.DateField()),
                ('allergies', models.TextField(max_length=200)),
                ('patientno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telemedicine.patients')),
            ],
        ),
        migrations.CreateModel(
            name='immunizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immunizations', models.TextField(max_length=200)),
                ('dateimmunization', models.DateField()),
                ('patientno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telemedicine.patients')),
            ],
        ),
        migrations.CreateModel(
            name='chartreports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('notes', models.TextField(max_length=250)),
                ('fileurl', models.URLField()),
                ('date', models.DateField()),
                ('patientno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telemedicine.patients')),
            ],
        ),
        migrations.AddField(
            model_name='appointments',
            name='patientno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telemedicine.patients'),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_patient', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]