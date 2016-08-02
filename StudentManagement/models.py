from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django import forms
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.forms.widgets import PasswordInput


class Class(models.Model):
    branch = models.CharField(max_length=5,default="")
    section = models.CharField(max_length=1,default="")
    year = models.IntegerField(default=1)
    no_of_students = models.IntegerField(default=60)

    def __unicode__(self):
        return self.branch+" "+str(self.year)+"-"+str(self.section)


class Subject(models.Model):
    subject_id = models.CharField(max_length=10,default="")
    subject_name = models.CharField(max_length=32,default="")

    def __unicode__(self):
        return str(self.subject_name)


class Faculty(models.Model):
    username = models.OneToOneField(User, blank=True, null=True)
    faculty_id = models.CharField(max_length=10,default="")
    name = models.CharField(max_length=32,default="")

    def __unicode__(self):
        return self.name


class Period(models.Model):
    subject = models.ForeignKey(Subject, null=True, blank=True)
    section = models.ForeignKey(Class,null=True, blank=True)
    faculty = models.ForeignKey(Faculty,null=True,blank=True)

    def __unicode__(self):
        return str(self.section)+"-"+str(self.subject)


class Student(models.Model):
    roll_no = models.CharField(max_length=10,default="")
    name = models.CharField(max_length=32,default="")
    section = models.ForeignKey(Class)

    def __unicode__(self):
        return self.name


class SubjectAttendenceTable(models.Model):
    subject = models.ForeignKey(Subject, null=True)
    attendencecount = models.IntegerField(default=0)
    student = models.ForeignKey(Student, null=True, blank=True)


class FacultyForm(forms.Form):
    name = forms.CharField(max_length=30)
    id = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=PasswordInput())

    def clean(self):
        #print "In clean"
        cleaned_data=super(FacultyForm,self).clean()
        id=cleaned_data.get("id")
        flag = 0
        try:
            faculty = Faculty.objects.get(faculty_id=id)
            if faculty.username:
                flag=1
                raise Exception
        except:
            if flag==1:
                raise forms.ValidationError("Faculty already is exist")
            raise forms.ValidationError("Please Enter a valid faculty id")
        return cleaned_data


class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = ["subject", "section"]

    #
    # def __init__(self,*args,**kwargs):
    #     self.subject_id = kwargs.get("subject_id")

    def clean(self):
        cleaned_data = super(PeriodForm, self).clean()
        try:
            subject = cleaned_data["subject"]
            section = cleaned_data["section"]
        except:
            raise forms.ValidationError("Please verify that the number of periods entered and matching the number of period details")
        return cleaned_data


PeriodFormSet = modelformset_factory(Period, form = PeriodForm, extra=5)