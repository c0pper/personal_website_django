from django.shortcuts import render, get_object_or_404
from .models import Skill, Experience, Project, Testimonial
from datetime import date
from django.views.generic.detail import DetailView

# Common elements
now = date.today()
current_year = now.year
email = "martin.s.marotta@gmail.com"
location = "Naples, IT"
skype = "martin.s.marotta@gmail.com"

social_buttons = [
    # url, href class, i class
    ("https://github.com/c0pper/", "github", "bx bxl-github"),
    ("https://www.instagram.com/sim01110011.01101001.01101101/", "instagram", "bx bxl-instagram"),
    ("https://www.youtube.com/channel/UCtUNRX-B_j2ipkL1Lihih8w/", "youtube", "bx bxl-youtube"),
    ("https://www.facebook.com/Simooon/", "facebook", "bx bxl-facebook")
]

navmenu = [
    ("#hero", "bx bx-home", "Home"),
    ("#about", "bx bx-user", "About"),
    ("#skills", "bx bx-user", "Skills"),
    ("#resume", "bx bx-file-blank", "Resume"),
    ("#projects", "bx bx-book-content", "Projects"),
    ("#contact", "bx bx-envelope", "Contact")
]


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


# Create your views here.
def home(request):
    context = {}
    context.update({"email": email})
    context.update({"location": location})
    context.update({"skype": skype})
    context.update({"age": calculateAge(date(1993, 9, 4))})
    context.update({"social_buttons": social_buttons})
    context.update({"navmenu": navmenu})
    context.update({"lang_skills": Skill.objects.filter(category__exact="L")})
    context.update({"comp_skills": Skill.objects.filter(category__exact="IT")})
    context.update({"ed_exp": Experience.objects.filter(exp_type__exact="E")})
    context.update({"work_exp": Experience.objects.filter(exp_type__exact="W")})
    context.update({"projects": Project.objects.all().order_by('-date')})
    context.update({"testimonials": Testimonial.objects.all()})
    # print(context)

    return render(request, "index.html", context=context)


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({"social_buttons": social_buttons})
        context.update({"navmenu": navmenu})

        return context
