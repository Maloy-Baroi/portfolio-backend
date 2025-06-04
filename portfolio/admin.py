from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'email', 'mobile', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['full_name', 'email', 'title']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company_name', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date', 'company_name']
    search_fields = ['job_title', 'company_name', 'profile__full_name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'major', 'institution', 'start_year', 'end_year', 'is_ongoing']
    list_filter = ['degree', 'is_ongoing', 'start_year']
    search_fields = ['major', 'institution', 'profile__full_name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(StandardizedTest)
class StandardizedTestAdmin(admin.ModelAdmin):
    list_display = ['test_type', 'test_date', 'total_score', 'profile']
    list_filter = ['test_type', 'test_date']
    search_fields = ['test_type', 'profile__full_name']


@admin.register(TestSection)
class TestSectionAdmin(admin.ModelAdmin):
    list_display = ['section_name', 'score', 'test']
    list_filter = ['test__test_type']
    search_fields = ['section_name', 'test__test_type']


@admin.register(TechnicalSkillCategory)
class TechnicalSkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'profile', 'order']
    list_filter = ['category_name']
    search_fields = ['category_name', 'profile__full_name']


@admin.register(TechnicalSkill)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'proficiency_level', 'category', 'years_of_experience']
    list_filter = ['proficiency_level', 'category__category_name']
    search_fields = ['skill_name', 'category__category_name']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language_name', 'proficiency_level', 'profile']
    list_filter = ['proficiency_level']
    search_fields = ['language_name', 'profile__full_name']


@admin.register(ExtraCurricularActivity)
class ExtraCurricularActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity_type', 'organization', 'start_date', 'end_date']
    list_filter = ['activity_type', 'start_date']
    search_fields = ['title', 'organization', 'profile__full_name']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'achievement_type', 'organization', 'date_achieved']
    list_filter = ['achievement_type', 'date_achieved']
    search_fields = ['title', 'organization', 'profile__full_name']


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'organization', 'email', 'phone']
    search_fields = ['name', 'title', 'organization', 'profile__full_name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'start_date', 'end_date', 'is_ongoing']
    list_filter = ['project_type', 'is_ongoing', 'start_date']
    search_fields = ['title', 'description', 'profile__full_name']
    readonly_fields = ['created_at', 'updated_at']
