from django.db import models
from django.core.validators import URLValidator

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    github = models.URLField()
    linkedin = models.URLField()
    website = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    career_objective = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    gpa = models.CharField(max_length=10)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    is_ongoing = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_year']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('frameworks', 'Frameworks'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    proficiency = models.IntegerField(default=1, help_text="1-5 scale")
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    created_date = models.DateField()
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"