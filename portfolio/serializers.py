from rest_framework import serializers
from .models import *


class TestSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSection
        fields = '__all__'


class StandardizedTestSerializer(serializers.ModelSerializer):
    sections = TestSectionSerializer(many=True, read_only=True)

    class Meta:
        model = StandardizedTest
        fields = '__all__'


class TechnicalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalSkill
        fields = '__all__'


class TechnicalSkillCategorySerializer(serializers.ModelSerializer):
    skills = TechnicalSkillSerializer(many=True, read_only=True)

    class Meta:
        model = TechnicalSkillCategory
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Experience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    year_range = serializers.ReadOnlyField()
    gpa_display = serializers.ReadOnlyField()

    class Meta:
        model = Education
        fields = '__all__'


class ExtraCurricularActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCurricularActivity
        fields = '__all__'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)
    test_scores = StandardizedTestSerializer(many=True, read_only=True)
    skill_categories = TechnicalSkillCategorySerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    activities = ExtraCurricularActivitySerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)
    references = ReferenceSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSummarySerializer(serializers.ModelSerializer):
    """Lighter serializer for listing profiles"""
    class Meta:
        model = Profile
        fields = ['id', 'full_name', 'title', 'email', 'mobile', 'career_objective', 'profile_image']
