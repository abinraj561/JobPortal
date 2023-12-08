from django.shortcuts import render
from .models import Jobs

def JobFilterCandidate(request):
    location = request.GET.get('location')
    designation = request.GET.get('Designation')
    skills = request.GET.get('skills')

    jobs = Jobs.objects.all()

    if location:
        jobs = jobs.filter(location__icontains=location)
    if designation:
        jobs = jobs.filter(Designation__icontains=designation)
    if skills:
        jobs = jobs.filter(skills__icontains=skills)

    context = {'jobs': jobs}
    return render(request, 'job_list.html', context)
