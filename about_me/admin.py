from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Facts_Scils)
admin.site.register(Testimonials)
admin.site.register(Contact)

class Portfolio_ImagesAdmin(admin.StackedInline):
	model =  Portfolio_Images


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
	inlines = [Portfolio_ImagesAdmin]
	list_display = ['title', 'client']
	list_display_links = ['title' ]
	#prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = Portfolio


class ExperiencesAdmin(admin.StackedInline):
	model =  Experiences


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
	inlines = [ExperiencesAdmin]
	list_display = ['title', 'date']
	list_display_links = ['title' ]
	#prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = Resume

