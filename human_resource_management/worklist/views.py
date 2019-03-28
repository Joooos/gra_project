from django.shortcuts import render

# Create your views here.
def new_job_list(request):
    return render(request, "worklist/new-job-list.html", )

def worklist_summary(request):
    return render(request, "worklist/worklist-summary.html", )