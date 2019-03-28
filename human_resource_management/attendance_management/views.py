from django.shortcuts import render

# Create your views here.
def checkin_and_out(request):
    return render(request, "attendance_management/checkin-and-out.html", )


def ask_for_leave(request):
    return render(request, "attendance_management/ask-for-leave.html", )


def attendance_check(request):
    return render(request, "attendance_management/attendance-check.html", )


def leave_statistics(request):
    return render(request, "attendance_management/leave-statistics.html", )


def overtime_statistics(request):
    return render(request, "attendance_management/overtime-statistics.html", )