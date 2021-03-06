# Generated by Django 2.2.6 on 2020-04-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anshaj', '0002_job_post_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyed_candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('candidates_givenname', models.CharField(max_length=200)),
                ('candidates_surename', models.CharField(max_length=200)),
                ('candidates_email', models.EmailField(max_length=254)),
                ('candidates_phonenumber', models.BigIntegerField()),
                ('candidates_resume', models.FileField(upload_to='CandidatesResume')),
            ],
        ),
    ]
