# Run this script with: python manage.py shell < seed_data.py

from portfolio.models import *
from datetime import date

# Clear existing data (optional)
PersonalInfo.objects.all().delete()
Experience.objects.all().delete()
Education.objects.all().delete()
Skill.objects.all().delete()
Project.objects.all().delete()
Achievement.objects.all().delete()

print("Creating Personal Info...")
personal_info = PersonalInfo.objects.create(
    name="Maloy Baroi",
    title="Software Engineer",
    email="maloybaroi1996@gmail.com",
    phone="+88 01303 838 765",
    address="Road 9, Middle Badda, Dhaka, Bangladesh",
    github="https://github.com/Maloy-Baroi",
    linkedin="https://bd.linkedin.com/in/maloy-baroi-745915163",
    website="https://maloy-baroi.github.io/Portfolio-Maloy-Baroi/",
    medium="https://medium.com/@maloybaroi1996",
    career_objective="To profoundly influence and enrich the lives of millions by harnessing the transformative power of learning and development. Aspire to cultivate a culture of continuous growth, innovation, and excellence, empowering individuals to unlock their fullest potential. Dedicated to designing scalable, impactful educational solutions that drive societal progress and foster enduring change."
)

print("Creating Experience...")
experiences = [
    {
        "title": "Software Developer",
        "company": "TechnoNext Ltd (US Bangla Group)",
        "location": "Dhaka, Bangladesh",
        "start_date": date(2023, 5, 1),
        "end_date": None,
        "is_current": True,
        "description": "Working on software's backend with Django & DRF and frontend with NextJs. Running projects are PropetaCRM, ERP system for the US-Bangla Group, ERP system for Reports (Microservice, Data Analysis), US Bangla Airlines recruitment system, Analytical Dashboard Application(Backend Lead)."
    },
    {
        "title": "Python Developer",
        "company": "Rokomari.com",
        "location": "Dhaka, Bangladesh",
        "start_date": date(2022, 12, 1),
        "end_date": date(2023, 5, 1),
        "is_current": False,
        "description": "Worked as a Machine Learning Engineer at Bangladesh's leading E-commerce site, focusing on developing an advanced recommendation system for online book sales."
    },
    {
        "title": "Software Developer",
        "company": "SkillJobs (skill.jobs)",
        "location": "Dhaka, Bangladesh",
        "start_date": date(2022, 7, 1),
        "end_date": date(2022, 11, 1),
        "is_current": False,
        "description": "Contributed to both front-end and back-end development as an intern software engineer, enhancing the platform's functionality and user experience for Bangladesh's leading job site."
    },
    {
        "title": "Software Developer (Contractual)",
        "company": "Smart Garage BD",
        "location": "Dhaka, Bangladesh",
        "start_date": date(2021, 1, 1),
        "end_date": date(2022, 3, 1),
        "is_current": False,
        "description": "Developed and enhanced a smart garage management system designed specifically for the maintenance and service of bikes and cars."
    }
]

for exp_data in experiences:
    Experience.objects.create(**exp_data)

print("Creating Education...")
education_data = [
    {
        "degree": "Master of Science",
        "institution": "North South University",
        "major": "Computer Science and Engineering",
        "gpa": "On Going",
        "start_year": 2025,
        "end_year": None,
        "is_ongoing": True
    },
    {
        "degree": "Bachelor of Science",
        "institution": "Daffodil Institute of IT",
        "major": "Computer Science and Engineering",
        "gpa": "3.16/4.0",
        "start_year": 2017,
        "end_year": 2020,
        "is_ongoing": False
    },
    {
        "degree": "Higher Secondary Certificate",
        "institution": "Tejgaon College",
        "major": "Physics, Chemistry, Higher Math, ICT",
        "gpa": "4.42/5.0",
        "start_year": 2014,
        "end_year": 2016,
        "is_ongoing": False
    },
    {
        "degree": "Secondary School Certificate",
        "institution": "Bhaluka Pilot High School",
        "major": "Physics, Chemistry, Pure Math, Higher Math",
        "gpa": "5.0/5.0",
        "start_year": 2012,
        "end_year": 2014,
        "is_ongoing": False
    }
]

for edu_data in education_data:
    Education.objects.create(**edu_data)

print("Creating Skills...")
skills_data = [
    # Programming Languages
    {"name": "Python", "category": "programming", "proficiency": 5},
    {"name": "JavaScript", "category": "programming", "proficiency": 4},
    {"name": "TypeScript", "category": "programming", "proficiency": 4},
    {"name": "R Programming", "category": "programming", "proficiency": 3},
    {"name": "GoLang", "category": "programming", "proficiency": 3},
    
    # Frameworks
    {"name": "Django", "category": "frameworks", "proficiency": 5},
    {"name": "Django Rest Framework", "category": "frameworks", "proficiency": 5},
    {"name": "FastAPI", "category": "frameworks", "proficiency": 4},
    {"name": "ReactJs", "category": "frameworks", "proficiency": 4},
    {"name": "NextJs", "category": "frameworks", "proficiency": 4},
    {"name": "Odoo", "category": "frameworks", "proficiency": 3},
    
    # Database
    {"name": "PostgreSQL", "category": "database", "proficiency": 4},
    {"name": "MongoDB", "category": "database", "proficiency": 4},
    {"name": "RedisDB", "category": "database", "proficiency": 3},
    
    # Tools
    {"name": "Docker", "category": "tools", "proficiency": 4},
    {"name": "Grafana Loki", "category": "tools", "proficiency": 3},
    {"name": "Git", "category": "tools", "proficiency": 4},
]

for skill_data in skills_data:
    Skill.objects.create(**skill_data)

print("Creating Projects...")
projects_data = [
    {
        "title": "PropetaCRM",
        "description": "Customer Relationship Management system for US-Bangla Group with advanced analytics and reporting features.",
        "technologies": "Django, DRF, NextJs, PostgreSQL, Redis",
        "github_url": "",
        "live_url": "",
        "created_date": date(2023, 6, 1)
    },
    {
        "title": "US Bangla Airlines Recruitment System",
        "description": "Comprehensive recruitment management system to streamline hiring processes for the airline industry.",
        "technologies": "Django, DRF, NextJs, PostgreSQL",
        "github_url": "",
        "live_url": "",
        "created_date": date(2023, 8, 1)
    },
    {
        "title": "Analytical Dashboard Application",
        "description": "Real-time analytics dashboard with microservices architecture for data analysis and reporting.",
        "technologies": "Django, DRF, NextJs, PostgreSQL, Redis, Grafana",
        "github_url": "",
        "live_url": "",
        "created_date": date(2023, 10, 1)
    },
    {
        "title": "Rokomari Recommendation System",
        "description": "Advanced machine learning-based recommendation system for Bangladesh's leading e-commerce book platform.",
        "technologies": "Python, Machine Learning, Django, PostgreSQL",
        "github_url": "",
        "live_url": "",
        "created_date": date(2023, 1, 1)
    },
    {
        "title": "Bangla Interactive Robot (BIR)",
        "description": "Humanoid robot capable of interactive communication in Bengali language with advanced AI capabilities.",
        "technologies": "Python, Machine Learning, Robotics, NLP",
        "github_url": "",
        "live_url": "",
        "created_date": date(2019, 6, 1)
    },
    {
        "title": "Butterfly-JWT",
        "description": "Published Python library for JSON Web Token handling with enhanced security features.",
        "technologies": "Python, JWT, Security",
        "github_url": "https://github.com/Maloy-Baroi/butterfly-jwt",
        "live_url": "",
        "created_date": date(2022, 3, 1)
    }
]

for project_data in projects_data:
    Project.objects.create(**project_data)

print("Creating Achievements...")
achievements_data = [
    {
        "title": "Champion in DIIT Annual Debate Competition-2019",
        "description": "First place winner in the annual debate competition",
        "date": date(2019, 12, 1)
    },
    {
        "title": "Runners-up in DIIT Annual Debate Competition-2018",
        "description": "Second place winner in the annual debate competition",
        "date": date(2018, 12, 1)
    },
    {
        "title": "Published Python Library: Butterfly-JWT",
        "description": "Successfully published and maintained a Python library for JWT token management",
        "date": date(2022, 3, 1)
    },
    {
        "title": "Built Humanoid Robot (BIR)",
        "description": "Developed Bangla Interactive Robot with advanced AI capabilities",
        "date": date(2019, 6, 1)
    },
    {
        "title": "President of Team Explorer (2017-2020)",
        "description": "Led the Team Explorer group and participated in various competitions",
        "date": date(2020, 1, 1)
    },
    {
        "title": "General Secretary of DIIT Robotics Club (2018-2019)",
        "description": "Served as General Secretary for the robotics club",
        "date": date(2019, 1, 1)
    }
]

for achievement_data in achievements_data:
    Achievement.objects.create(**achievement_data)

print("Data seeding completed successfully!")
print(f"Created:")
print(f"- Personal Info: {PersonalInfo.objects.count()}")
print(f"- Experience: {Experience.objects.count()}")
print(f"- Education: {Education.objects.count()}")
print(f"- Skills: {Skill.objects.count()}")
print(f"- Projects: {Project.objects.count()}")
print(f"- Achievements: {Achievement.objects.count()}")