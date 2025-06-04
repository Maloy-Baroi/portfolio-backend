from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Profile.objects.filter()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSummarySerializer
        return ProfileSerializer

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['get'])
    def resume_data(self, request, pk=None):
        """Get complete resume data for a profile"""
        profile = self.get_object()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return Experience.objects.filter(profile_id=profile_id)
        return Experience.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return Education.objects.filter(profile_id=profile_id)
        return Education.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class StandardizedTestViewSet(viewsets.ModelViewSet):
    serializer_class = StandardizedTestSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return StandardizedTest.objects.filter(profile_id=profile_id)
        return StandardizedTest.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class TestSectionViewSet(viewsets.ModelViewSet):
    serializer_class = TestSectionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        test_id = self.request.query_params.get('test_id')
        if test_id:
            return TestSection.objects.filter(test_id=test_id)
        return TestSection.objects.all()

    def perform_create(self, serializer):
        test_id = self.request.data.get('test')
        test = get_object_or_404(StandardizedTest, id=test_id)
        serializer.save(test=test)


class TechnicalSkillCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = TechnicalSkillCategorySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return TechnicalSkillCategory.objects.filter(profile_id=profile_id)
        return TechnicalSkillCategory.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class TechnicalSkillViewSet(viewsets.ModelViewSet):
    serializer_class = TechnicalSkillSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return TechnicalSkill.objects.filter(category_id=category_id)
        return TechnicalSkill.objects.all()

    def perform_create(self, serializer):
        category_id = self.request.data.get('category')
        category = get_object_or_404(TechnicalSkillCategory, id=category_id)
        serializer.save(category=category)


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return Language.objects.filter(profile_id=profile_id)
        return Language.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class ExtraCurricularActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ExtraCurricularActivitySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return ExtraCurricularActivity.objects.filter(profile_id=profile_id)
        return ExtraCurricularActivity.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class AchievementViewSet(viewsets.ModelViewSet):
    serializer_class = AchievementSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return Achievement.objects.filter(profile_id=profile_id)
        return Achievement.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ReferenceSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return Reference.objects.filter(profile_id=profile_id)
        return Reference.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        if profile_id:
            return Project.objects.filter(profile_id=profile_id)
        return Project.objects.all()

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile')
        profile = get_object_or_404(Profile, id=profile_id)
        serializer.save(profile=profile)
