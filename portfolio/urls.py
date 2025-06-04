from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet, basename='profile')
router.register(r'experiences', views.ExperienceViewSet, basename='experience')
router.register(r'educations', views.EducationViewSet, basename='education')
router.register(r'test-scores', views.StandardizedTestViewSet, basename='test-score')
router.register(r'test-sections', views.TestSectionViewSet, basename='test-section')
router.register(r'skill-categories', views.TechnicalSkillCategoryViewSet, basename='skill-category')
router.register(r'skills', views.TechnicalSkillViewSet, basename='skill')
router.register(r'languages', views.LanguageViewSet, basename='language')
router.register(r'activities', views.ExtraCurricularActivityViewSet, basename='activity')
router.register(r'achievements', views.AchievementViewSet, basename='achievement')
router.register(r'references', views.ReferenceViewSet, basename='reference')
router.register(r'projects', views.ProjectViewSet, basename='project')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
