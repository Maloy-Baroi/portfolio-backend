from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class Profile(models.Model):
    """Main profile model for user basic information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    medium = models.URLField(blank=True, null=True)
    career_objective = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.full_name} - {self.title}"


class Experience(models.Model):
    """Work experience model"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    technologies_used = models.TextField(blank=True, null=True, help_text="Comma separated technologies")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', '-order']

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    @property
    def duration(self):
        if self.is_current:
            return f"{self.start_date.strftime('%B %Y')} to Present"
        elif self.end_date:
            return f"{self.start_date.strftime('%B %Y')} to {self.end_date.strftime('%B %Y')}"
        return f"{self.start_date.strftime('%B %Y')}"


class Education(models.Model):
    """Education model"""
    DEGREE_CHOICES = [
        ('PhD', 'Doctor of Philosophy'),
        ('Masters', 'Master of Science'),
        ('Bachelors', 'Bachelor of Science'),
        ('HSC', 'Higher Secondary Certificate'),
        ('SSC', 'Secondary School Certificate'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    major = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True)
    is_ongoing = models.BooleanField(default=False)
    gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    max_gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    subjects = models.TextField(blank=True, null=True, help_text="Comma separated subjects")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_year', '-order']

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.institution}"

    @property
    def year_range(self):
        if self.is_ongoing:
            return f"{self.start_year} - Ongoing"
        elif self.end_year:
            return f"{self.start_year} - {self.end_year}"
        return str(self.start_year)

    @property
    def gpa_display(self):
        if self.gpa and self.max_gpa:
            return f"{self.gpa}/{self.max_gpa}"
        return None


class StandardizedTest(models.Model):
    """Standardized test scores model"""
    TEST_TYPES = [
        ('GRE', 'Graduate Record Examinations'),
        ('TOEFL', 'Test of English as a Foreign Language'),
        ('IELTS', 'International English Language Testing System'),
        ('DUOLINGO', 'Duolingo English Test'),
        ('SAT', 'Scholastic Assessment Test'),
        ('GMAT', 'Graduate Management Admission Test'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='test_scores')
    test_type = models.CharField(max_length=20, choices=TEST_TYPES)
    test_date = models.DateField()
    total_score = models.PositiveIntegerField()
    max_score = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-test_date']

    def __str__(self):
        return f"{self.test_type} - {self.total_score}"


class TestSection(models.Model):
    """Individual sections of standardized tests"""
    test = models.ForeignKey(StandardizedTest, on_delete=models.CASCADE, related_name='sections')
    section_name = models.CharField(max_length=50)
    score = models.PositiveIntegerField()
    max_score = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.test.test_type} - {self.section_name}: {self.score}"


class TechnicalSkillCategory(models.Model):
    """Categories for technical skills"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skill_categories')
    category_name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.category_name


class TechnicalSkill(models.Model):
    """Individual technical skills"""
    PROFICIENCY_LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]

    category = models.ForeignKey(TechnicalSkillCategory, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS, default='Intermediate')
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.skill_name} ({self.proficiency_level})"


class Language(models.Model):
    """Languages spoken"""
    PROFICIENCY_LEVELS = [
        ('Native', 'Native'),
        ('Fluent', 'Fluent'),
        ('Conversational', 'Conversational'),
        ('Basic', 'Basic'),
        ('Understandable', 'Understandable'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    language_name = models.CharField(max_length=50)
    proficiency_level = models.CharField(max_length=20, choices=PROFICIENCY_LEVELS)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.language_name} ({self.proficiency_level})"


class ExtraCurricularActivity(models.Model):
    """Extra-curricular and co-curricular activities"""
    ACTIVITY_TYPES = [
        ('Leadership', 'Leadership'),
        ('Competition', 'Competition'),
        ('Club', 'Club'),
        ('Volunteering', 'Volunteering'),
        ('Sports', 'Sports'),
        ('Arts', 'Arts'),
        ('Other', 'Other'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Achievement(models.Model):
    """Achievements and awards"""
    ACHIEVEMENT_TYPES = [
        ('Award', 'Award'),
        ('Competition', 'Competition'),
        ('Publication', 'Publication'),
        ('Project', 'Project'),
        ('Certification', 'Certification'),
        ('Other', 'Other'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='achievements')
    achievement_type = models.CharField(max_length=20, choices=ACHIEVEMENT_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    organization = models.CharField(max_length=100, blank=True, null=True)
    date_achieved = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Reference(models.Model):
    """Professional references"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    relationship = models.CharField(max_length=100, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.title}"


class Project(models.Model):
    """Personal or professional projects"""
    PROJECT_TYPES = [
        ('Personal', 'Personal'),
        ('Professional', 'Professional'),
        ('Academic', 'Academic'),
        ('Open Source', 'Open Source'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies_used = models.TextField(help_text="Comma separated technologies")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_ongoing = models.BooleanField(default=False)
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    demo_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return self.title
