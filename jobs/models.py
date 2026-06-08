from django.db import models


# ---------------- JOB SEEKER ----------------
class JobSeeker(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


# ---------------- EMPLOYER ----------------
class Employer(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


# ---------------- JOB ----------------
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.title

# ---------------- APPLICATION ----------------
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)

    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    status = models.CharField(max_length=50, default="Applied")
    applied_on = models.DateTimeField(auto_now_add=True)