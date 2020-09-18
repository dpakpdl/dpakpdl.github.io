from django.contrib import admin
from main.models import Person, AwardsAndHonour, Education, Experience, Contact


class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", )


class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "course")


class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "address")


class PersonalInfoAdmin(admin.ModelAdmin):
    pass


class RelationAdmin(admin.ModelAdmin):
    list_display = ['user', 'education']


admin.site.register(Person, PersonAdmin)
admin.site.register(AwardsAndHonour, PersonalInfoAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, PersonalInfoAdmin)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(UserRelation, RelationAdmin)
