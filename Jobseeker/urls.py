from Jobseeker import views
from django.urls import path
urlpatterns = [
    path('jobs/path',views.JobseekerHome.as_view(),name="jhome"),
    path('job/<int:id>',views.JobsListView.as_view(),name="job"),
    path('profile/add',views.AddJobseekerProfile.as_view(),name="addprofile"),
    path('profile/edit/<int:id>',views.EditJobseekerProfileView.as_view(),name="editprofile"),
    path('profile/view',views.JobseekerProfileView.as_view(),name="viewprofile"),
    path('job/apply/<int:id>',views.CreateApplication.as_view(),name="createapplication"),
    path('applications/all',views.ViewApplications.as_view(),name="viewapplication"),
    path('viewjob/',views.viewjob,name="viewjob"),
    

    ]