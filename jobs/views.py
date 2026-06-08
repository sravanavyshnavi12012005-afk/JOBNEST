from django.shortcuts import render, redirect, get_object_or_404
from .models import JobSeeker, Employer, Job, Application

# ---------------- HOME ----------------
def home(request):
    return render(request, 'home.html')


# ---------------- REGISTRATION ----------------
def jobseeker(request):
    return render(request, 'jobseeker.html')


def seeker_register(request):
    if request.method == 'POST':
        JobSeeker.objects.create(
            full_name=request.POST['fullname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            skills=request.POST['skills'],
            password=request.POST['password']
        )
        return render(request, 'registration_success.html')

    return render(request, 'seeker_register.html')


def employer_register(request):
    if request.method == 'POST':
        Employer.objects.create(
            company_name=request.POST['company_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            location=request.POST['location'],
            password=request.POST['password']
        )
        return render(request, 'registration_success.html')

    return render(request, 'employer_register.html')


# ---------------- LOGIN ----------------
def seeker_login(request):
    if request.method == 'POST':
        user = JobSeeker.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']
        ).first()

        if user:
            request.session['seeker_id'] = user.id
            return render(request, 'seeker_dashboard.html')

    return render(request, 'seeker_login.html')


def employer_login(request):
    if request.method == 'POST':
        employer = Employer.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']
        ).first()

        if employer:
            request.session['employer_id'] = employer.id
            return render(request, 'employer_dashboard.html')

    return render(request, 'employer_login.html')


# ---------------- POST JOB ----------------
def post_job(request):

    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        salary = request.POST['salary']

        Job.objects.create(
            title=title,
            description=description,
            location=location,
            salary=salary
        )

        return render(request, 'job_post_success.html')

    return render(request, 'post_job.html')

# ---------------- VIEW JOBS ----------------
def employer_dashboard(request):
    return render(request, 'employer_dashboard.html')


def view_jobs(request):

    title_search = request.GET.get('title')
    location_search = request.GET.get('location')

    jobs = Job.objects.all()

    if title_search:
        jobs = jobs.filter(title__icontains=title_search)

    if location_search:
        jobs = jobs.filter(location__icontains=location_search)

    return render(
        request,
        'view_jobs.html',
        {
            'jobs': jobs,
            'title_search': title_search,
            'location_search': location_search,
        }
    )

        # ---------------- APPLY JOB ----------------
def apply_job(request, job_id):

    # Check if seeker is logged in
    seeker_id = request.session.get('seeker_id')

    if not seeker_id:
        return redirect('/seeker-login/')

    job = get_object_or_404(Job, id=job_id)

    jobseeker = JobSeeker.objects.get(id=seeker_id)

    # Check duplicate application
    already_applied = Application.objects.filter(
        job=job,
        jobseeker=jobseeker
    ).exists()

    if already_applied:
        return render(request, 'already_applied.html')

    if request.method == 'POST':

        resume = request.FILES.get('resume')

        Application.objects.create(
            job=job,
            jobseeker=jobseeker,
            resume=resume
        )

        return render(request, 'application_success.html')

    return render(
        request,
        'apply_job.html',
        {
            'job': job
        }
    )
# ---------------- VIEW APPLICANTS ----------------
def view_applicants(request):

    applications = Application.objects.all()

    return render(
        request,
        'view_applicants.html',
        {'applications': applications}
    )
# ---------------- SHORTLIST ----------------
def shortlist_applicant(request, application_id):

    application = Application.objects.get(id=application_id)

    application.status = "Shortlisted"

    application.save()

    return redirect('/view-applicants/')


def reject_applicant(request, application_id):

    application = Application.objects.get(id=application_id)

    application.status = "Rejected"

    application.save()

    return redirect('/view-applicants/')

def admin_dashboard(request):

    seekers_count = JobSeeker.objects.count()

    employers_count = Employer.objects.count()

    jobs_count = Job.objects.count()

    applications_count = Application.objects.count()

    return render(
        request,
        'admin_dashboard.html',
        {
            'seekers_count': seekers_count,
            'employers_count': employers_count,
            'jobs_count': jobs_count,
            'applications_count': applications_count,
        }
    )
def logout_user(request):
    return redirect('/')
def applied_jobs(request):

    seeker_id = request.session.get('seeker_id')

    applications = Application.objects.filter(
        jobseeker_id=seeker_id
    )

    return render(
        request,
        'applied_jobs.html',
        {
            'applications': applications
        }
    )
def manage_jobs(request):

    jobs = Job.objects.all()

    return render(
        request,
        'manage_jobs.html',
        {
            'jobs': jobs
        }
    )
def delete_job(request, job_id):

    job = Job.objects.get(id=job_id)

    job.delete()

    return redirect('/manage-jobs/')
def edit_job(request, job_id):

    job = Job.objects.get(id=job_id)

    if request.method == 'POST':

        job.title = request.POST['title']
        job.description = request.POST['description']
        job.location = request.POST['location']
        job.salary = request.POST['salary']

        job.save()

        return redirect('/manage-jobs/')

    return render(
        request,
        'edit_job.html',
        {
            'job': job
        }
    )
def view_seekers(request):

    seekers = JobSeeker.objects.all()

    return render(
        request,
        'view_seekers.html',
        {
            'seekers': seekers
        }
    )
def view_employers(request):

    employers = Employer.objects.all()

    return render(
        request,
        'view_employers.html',
        {
            'employers': employers
        }
    )
def view_all_jobs(request):

    jobs = Job.objects.all()

    return render(
        request,
        'view_all_jobs.html',
        {
            'jobs': jobs
        }
    )
def view_applications(request):

    applications = Application.objects.all()

    return render(
        request,
        'view_applications.html',
        {
            'applications': applications
        }
    )