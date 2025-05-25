from django.urls import path
from . import views

urlpatterns = [
    path('personal-info/', views.PersonalInfoView.as_view(), name='personal-info'),
    path('experience/', views.ExperienceListView.as_view(), name='experience'),
    path('education/', views.EducationListView.as_view(), name='education'),
    path('skills/', views.SkillListView.as_view(), name='skills'),
    path('skills-by-category/', views.skills_by_category, name='skills-by-category'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('achievements/', views.AchievementListView.as_view(), name='achievements'),
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
]