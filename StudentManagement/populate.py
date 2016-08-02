import sys,os
import django

sys.path.append("../AttedanceManagement")
os.environ["DJANGO_SETTINGS_MODULE"] = "AttendanceManagement.settings"
django.setup()

from StudentManagement.models import *


#create 60 students

c = Class(branch="CSE", section="A", no_of_students=60, year=4)
c.save()

c = Class(branch="CSE", section="B", no_of_students=60, year=4)
c.save()

c = Class(branch="CSE", section="C", no_of_students=60, year=4)
c.save()

c = Class(branch="CSE", section="D", no_of_students=60, year=4)
c.save()

subjects = ["LP", "DMDB", "DP", "SL", "STM", "MAD", "UNIX", "C", "JAVA", "PYTHON", "C++"]
s_ids = ["1000", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009","1010"]

for i in range(6):
    s=Subject(subject_name=subjects[i], subject_id=s_ids[i])
    s.save()

faculty = ["Ram Mohan", "Sathyanarayana", "Shiva Reddy", "Swetha", "Rohini", "Vani", "Ashwin", "Venkateshwarlu", "N V Rao", "Sameul", "Badri Narayana"]
faculty_id = ["10000", "10001", "10002", "10003", "10004", "10005", "10006", "10007", "10008", "10009", "10010"]

for i in range(6):
    s=Faculty(name=faculty[i],faculty_id=faculty_id[i])
    s.save()

for i in range(60):
    st = Student(name="madhu"+str(i),roll_no="13B81A"+str(i),section=Class.objects.get(id=1))
    st.save()
    for j in range(6):
        at_table = SubjectAttendenceTable()
        at_table.save()
        at_table.subject = Subject.objects.get(subject_id=s_ids[j])
        at_table.student = st
        at_table.save()