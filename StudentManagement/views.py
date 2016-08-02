from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.template import loader
from django.template.context import RequestContext

from StudentManagement.models import *


def home(request):
    if request.method == 'POST':
        #print request.POST.get("roll")
        try:
            student = Student.objects.get(roll_no=request.POST.get("roll"))
            subs = student.subjectattendencetable_set.all()
        except:
            return HttpResponseRedirect("/attendance/error/"+request.POST.get("roll")+" is not a valid roll number/")
        template = loader.get_template("display_attendance.html")
        result = template.render(context = {"list":subs, "stud":student}, request=request)
        return HttpResponse(result)
    template = loader.get_template("home.html")
    result = template.render(request=request)
    return HttpResponse(result)


@login_required
def faculty_view(request):
    user = request.user
    faculty = user.faculty
    template = loader.get_template("Schedule.html")
    result = template.render(context={'schedule':faculty.period_set.all()})
    return HttpResponse(result)


@login_required
def loginhome(request):
    faculty = Faculty.objects.get(username = request.user)
    template=loader.get_template("loginhome.html")
    result=template.render(context = {"user":faculty})
    return HttpResponse(result)


def error(request,*args,**kwargs):
    template = loader.get_template("error.html")
    url = request.META.get("HTTP_REFERER")
    result = template.render({"msg":kwargs.get("msg"), "url":url})
    return HttpResponse(result)


def signup(request):
    if request.method=='POST':
        form = FacultyForm(request.POST)
        user = User()
        if form.is_valid():
            print "form is valid"
            user.username=form.cleaned_data["name"]
            user.email=form.cleaned_data["email"]
            user.set_password(form.cleaned_data["password"])
            user.save()
            faculty=Faculty.objects.get(faculty_id=form.cleaned_data["id"])
            faculty.username=user
            faculty.save()
            return HttpResponseRedirect("/attendance/login/")
        else:
            form = FacultyForm(request.POST)
            template = loader.get_template("register.html")
            result = template.render(context={'form':form},request=request)
            return HttpResponse(result)
    else:
        form = FacultyForm()
        template = loader.get_template("register.html")
        result = template.render(context={'form':form},request=request)
        return HttpResponse(result)


@login_required
def addperiods(request):
    faculty = Faculty.objects.get(username=request.user)
    if request.method=="POST":
        periods = PeriodFormSet(request.POST)
        if periods.is_valid():
            faculty.period_set.all().delete()
            for p in periods:
                cd = p.cleaned_data
                if not cd:
                    break
                per = Period()
                per.subject = cd["subject"]
                per.section = cd["section"]
                per.faculty = faculty
                per.save()
            return HttpResponseRedirect("/attendance/schedule/")
        else:
            template=loader.get_template("addperiods.html")
            result=template.render(context={"form":periods},request=request)
            return HttpResponse(result)
    else:
        form = PeriodFormSet(queryset=faculty.period_set.all())
        template=loader.get_template("addperiods.html")
        result=template.render(context = {"form":form},request=request)
        return HttpResponse(result)


@login_required
def class_view(request,cid,sid):
    if request.method=='POST':
        cls = Class.objects.get(id=cid)
        studs = cls.student_set.all()
        st_list = request.POST.getlist("students")
        print st_list
        for i in st_list:
            student = studs.get(roll_no=i)
            sub_attend = student.subjectattendencetable_set.get(subject__id = sid)
            sub_attend.attendencecount += 1
            sub_attend.save()
        return HttpResponseRedirect('/attendance/schedule/')
    else:
        cls = Class.objects.get(id=cid)
        studs = cls.student_set.all()
        template = loader.get_template("students.html")
        c = RequestContext(request,{'students':studs})
        result = template.render(c)
        return HttpResponse(result)