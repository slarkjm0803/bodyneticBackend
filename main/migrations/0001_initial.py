from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, max_length=32)),
                ('email', models.CharField(blank=True, max_length=32)),
                ('password', models.CharField(blank=True, max_length=32)),
                ('isVerified', models.BooleanField(default=False)),
                ('verification_code', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userdb_tb',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=32)),
                ('dob', models.DateField()),
                ('height', models.FloatField(blank=True)),
                ('weight', models.FloatField(blank=True)),
                ('target_weight', models.FloatField(blank=True)),
                ('pain_parts', models.IntegerField(blank=True)),
                ('daily_task', models.IntegerField(blank=True)),
                ('fitness_goal', models.IntegerField(blank=True)),
                ('favourite_type_excercise', models.IntegerField(blank=True)),
                ('equipment', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, to='main.userdata')),
            ],
            options={
                'db_table': 'profile_tb',
            },
        ),
    ]
