# Generated by Django 5.2.1 on 2025-06-04 02:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
                ('github', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('medium', models.URLField(blank=True, null=True)),
                ('career_objective', models.TextField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=50)),
                ('proficiency_level', models.CharField(choices=[('Native', 'Native'), ('Fluent', 'Fluent'), ('Conversational', 'Conversational'), ('Basic', 'Basic'), ('Understandable', 'Understandable')], max_length=20)),
                ('order', models.PositiveIntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='portfolio.profile')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ExtraCurricularActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('Leadership', 'Leadership'), ('Competition', 'Competition'), ('Club', 'Club'), ('Volunteering', 'Volunteering'), ('Sports', 'Sports'), ('Arts', 'Arts'), ('Other', 'Other')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='portfolio.profile')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('company_location', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('technologies_used', models.TextField(blank=True, help_text='Comma separated technologies', null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='portfolio.profile')),
            ],
            options={
                'ordering': ['-start_date', '-order'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('PhD', 'Doctor of Philosophy'), ('Masters', 'Master of Science'), ('Bachelors', 'Bachelor of Science'), ('HSC', 'Higher Secondary Certificate'), ('SSC', 'Secondary School Certificate'), ('Diploma', 'Diploma'), ('Certificate', 'Certificate')], max_length=50)),
                ('major', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('start_year', models.PositiveIntegerField()),
                ('end_year', models.PositiveIntegerField(blank=True, null=True)),
                ('is_ongoing', models.BooleanField(default=False)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('max_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('subjects', models.TextField(blank=True, help_text='Comma separated subjects', null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='portfolio.profile')),
            ],
            options={
                'ordering': ['-start_year', '-order'],
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_type', models.CharField(choices=[('Award', 'Award'), ('Competition', 'Competition'), ('Publication', 'Publication'), ('Project', 'Project'), ('Certification', 'Certification'), ('Other', 'Other')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('date_achieved', models.DateField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='portfolio.profile')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(choices=[('Personal', 'Personal'), ('Professional', 'Professional'), ('Academic', 'Academic'), ('Open Source', 'Open Source')], max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technologies_used', models.TextField(help_text='Comma separated technologies')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_ongoing', models.BooleanField(default=False)),
                ('project_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('demo_url', models.URLField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.profile')),
            ],
            options={
                'ordering': ['-start_date', 'order'],
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('relationship', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='portfolio.profile')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='StandardizedTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(choices=[('GRE', 'Graduate Record Examinations'), ('TOEFL', 'Test of English as a Foreign Language'), ('IELTS', 'International English Language Testing System'), ('DUOLINGO', 'Duolingo English Test'), ('SAT', 'Scholastic Assessment Test'), ('GMAT', 'Graduate Management Admission Test')], max_length=20)),
                ('test_date', models.DateField()),
                ('total_score', models.PositiveIntegerField()),
                ('max_score', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_scores', to='portfolio.profile')),
            ],
            options={
                'ordering': ['-test_date'],
            },
        ),
        migrations.CreateModel(
            name='TechnicalSkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_categories', to='portfolio.profile')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TechnicalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('proficiency_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], default='Intermediate', max_length=20)),
                ('years_of_experience', models.PositiveIntegerField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='portfolio.technicalskillcategory')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TestSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=50)),
                ('score', models.PositiveIntegerField()),
                ('max_score', models.PositiveIntegerField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='portfolio.standardizedtest')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
