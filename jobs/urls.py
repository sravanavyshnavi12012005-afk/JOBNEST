from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobseeker/', views.jobseeker, name='jobseeker'),
    path('seeker-register/', views.seeker_register, name='seeker_register'),
    path('employer-register/', views.employer_register, name='employer_register'),
    path('seeker-login/', views.seeker_login, name='seeker_login'),
    path('employer-login/', views.employer_login, name='employer_login'),
    path('post-job/', views.post_job, name='post_job'),
    path('view-jobs/',views.view_jobs, name='view_jobs'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('view-applicants/', views.view_applicants,name='view_applicants'),
    path('shortlist/<int:application_id>/',views.shortlist_applicant,name='shortlist_applicant'),
    path('reject/<int:application_id>/',views.reject_applicant,name='reject_applicant'),
    path('employer-dashboard/',views.employer_dashboard, name='employer_dashboard'),
    path( 'admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path(  'logout/',views.logout_user,name='logout'),
    path('applied-jobs/',views.applied_jobs,name='applied_jobs'),
    path( 'manage-jobs/', views.manage_jobs,name='manage_jobs'),
    path('delete-job/<int:job_id>/',views.delete_job,name='delete_job'),
    path('edit-job/<int:job_id>/',views.edit_job,name='edit_job'),
    path('view-seekers/', views.view_seekers, name='view_seekers'),
    path(  'view-employers/',views.view_employers,name='view_employers'),
    path('view-all-jobs/',views.view_all_jobs,name='view_all_jobs'),
    path( 'view-applications/',views.view_applications,name='view_applications'),
]