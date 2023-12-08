from django.shortcuts import render,redirect
from Employer.models import Jobs
from django.views.generic import CreateView,TemplateView,UpdateView,DetailView,ListView,View
from Jobseeker.models import Applications,JobseekerProfile
from django.contrib import messages
from Jobseeker.forms import JobseekerProfileForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from Employer.decorators import signin_required
from Jobseeker.filters import JobFilterCandidate
from django.db.models import Q
from datetime import date


class JobseekerHome(View):
    def get(self,request,*args,**kwargs):
        keyword = request.GET.get('keyword')
        q = Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(skills__icontains=keyword)
        context = {
            'jobs': Jobs,
            'keyword': keyword,
}
        return render(request, 'Jobse_home.html', context)


class JobsListView(ListView):
    model = Jobs  # Specify the Jobs model as the queryset source
    template_name = 'jobs_list.html'  # Define the template file to use for rendering the list view
    context_object_name = 'jobs'  # Define the context variable name for the list of jobs

    def get_queryset(self):
        # Customize the queryset to filter displayed jobs based on your requirements
        return super().get_queryset().filter(is_active=True)
    

class AddJobseekerProfile(CreateView):
    model = JobseekerProfile
    form_class = JobseekerProfileForm
    template_name = "profile.html"
    def post(self, request):
        form = self.form_class(request.POST, files=request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('jhome')
        else:
            return render(request,'profile.html', {"form": form})
        
        
class JobseekerProfileView(DetailView):
    model = JobseekerProfile
    template_name = "profiledetail.html"
    def get(self, request, *args, **kwargs):
        qs = self.model.objects.get(user=self.request.user)
        context = {"profile":qs}
        return render(request,'profiledetail.html',context)
    
    
class EditJobseekerProfileView(UpdateView):
    model = JobseekerProfile
    form_class = JobseekerProfileForm
    template_name = "editprofile.html"
    success_url = reverse_lazy('jhome')
    pk_url_kwarg = "id"



class CreateApplication(View):
    def get(self, request,*args,**kwargs):
        id = kwargs['id']
        job = Jobs.objects.get(id=id)
        candidate =JobseekerProfile.objects.get(user=request.user)
        qs=Applications.objects.filter(user=candidate,job=job)
        if qs:
            messages.success(request, "You are already applied for the job")
            return redirect("jhome")
        else:
            application = Applications(user=candidate,job=job)
            application.save()
            messages.success(request,"You are successfully applied for the job")
            return redirect("jhome")


class ViewApplications(ListView):
    model = Applications
    template_name = "applications.html"
    context_object_name = "applications"
    def get(self,request,object_list=None, **kwargs):
        candidate=JobseekerProfile.objects.get(user=request.user)
        applications=Applications.objects.filter(user=candidate).order_by("-submitted_date")
        return render(request,self.template_name,{"applications":applications})


def viewjob(request,**kwargs):
    if request.method=="GET":
        query=request.GET.get('query')
        jobs=Jobs.objects.all().order_by("-create_date")
        context = {'jobs': jobs,"today":date.today()}
        return render(request,'total_jobs.html', context)