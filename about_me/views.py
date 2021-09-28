from django.shortcuts import render
from .models import *
import telepot
from django.views.generic.base import View
from django.shortcuts import get_object_or_404

# Create your views here.

bot = telepot.Bot('1368490503:AAHXGKIzJVqVsV-3IBAy7R3XvtGzL1KA7Vg')
my_id = 834592754


def index(request):
	author = Author.objects.all()
	portfolio = Portfolio.objects.all()
	facts_scils = Facts_Scils.objects.all()
	testimonials = Testimonials.objects.all()
	resume_summary = Resume.objects.filter(theme='Sumary')
	resume_education = Resume.objects.filter(theme='Education')
	resume_professional_experience = Resume.objects.filter(theme='Professional_Experience')

	context = {
				'author':author,
				'portfolio':portfolio,
				'facts_scils':facts_scils,
				'testimonials':testimonials,
				'resume_summary':resume_summary,
				'resume_education':resume_education,
				'resume_professional_experience':resume_professional_experience,
			  }
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']

		Contact.objects.create(
			name=name,
			email=email,
			subject=subject,
			message=message,
			),
		bot.sendMessage(my_id,f"{name}\n\n{email}\n\n{subject}\n\n{message}")

	return render(request, 'index.html', context)

class PortfolioViewDetail(View):
    def get(self,request,portfolio_slug):
        portfolio = get_object_or_404(Portfolio, slug=portfolio_slug)
        author = Author.objects.all()
        context = {'portfolio':portfolio,'author':author,}
        return render(request, 'portfolio-details.html', context)
