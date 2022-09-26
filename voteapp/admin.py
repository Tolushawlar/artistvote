from django.contrib import admin
from .models import  Award, Choice, Triva

# changing the interface of the admin panel of the application
admin.site.site_header = "Artistvote Admin"
admin.site.site_title = "Artistvote Admin Panel"
admin.site.index_title = "Welcome to the Artistvote Admin Panel"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class AwardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['award_name', 'artistNum']}),
        ('Date Information', {'fields': ['created_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Award, AwardAdmin)
admin.site.register(Triva)