from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PersonalInfo, Experience, Education, Skill, Project, Achievement, Contact
from .serializers import (
    PersonalInfoSerializer, 
    ExperienceSerializer, 
    EducationSerializer, 
    SkillSerializer, 
    ProjectSerializer, 
    AchievementSerializer, 
    ContactSerializer
)

class PersonalInfoView(generics.RetrieveAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    
    def get_object(self):
        return PersonalInfo.objects.first()

class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AchievementListView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Thank you for your message! I'll get back to you soon."},
            status=status.HTTP_201_CREATED
        )

@api_view(['GET'])
def skills_by_category(request):
    skills = Skill.objects.all()
    skills_dict = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_dict:
            skills_dict[category] = []
        skills_dict[category].append(SkillSerializer(skill).data)
    return Response(skills_dict)