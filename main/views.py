from django.shortcuts import render
from main.models import Person, Education, Contact, Experience, AwardsAndHonour


def personal_info(request):
    user = Person.objects.get(pk=1)
    educations = Education.objects.filter(user=user)
    contacts = Contact.objects.filter(user=user)
    experiences = Experience.objects.filter(user=user)
    awards = AwardsAndHonour.objects.filter(user=user)
    context = {
        'user': user,
        'educations': educations,
        'contacts': contacts,
        'experiences': experiences,
        'awards': awards
    }
    return render(request, 'personal_info.html', context)
