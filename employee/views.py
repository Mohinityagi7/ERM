from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def index(request):
    return render(request,'index.html')


def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user= user ,empcode=ec)
            EmployeeExperience.objects.create(user=user)
            
            error = "no"
        except:
            error = "yes"
    return render(request,'registration.html',locals())

def emp_login(request):
    # username = password = ''
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(username=username, password = password)
    error = ""
    if request.method == "POST":
        U = request.POST['Email-id' ]
        p = request.POST['password']
        user = authenticate(username=U, password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.user.empcode = ec
        employee.user.empdept = dept
        employee.user.designation = designation
        employee.user.contact = contact
        employee.user.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
                
            error = "no"
        except:
            error = "yes"
    return render(request,'profile.html',locals())


def emp_base(request):
    return render(request,'emp_base.html')

def admin_login(request):
    return render(request,'admin_login.html')


def myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)

    return render(request,'myexperience.html',locals())



def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig= request.POST['company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']
        
        company2name = request.POST['company2name']
        company2desig= request.POST['company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']
        
        company3name = request.POST['company3name']
        company3desig = request.POST['company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        
       

        try:
            experience.save()
            
                
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_experience.html',locals())



def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    print(user)
    try:
        education = EmployeeEducation.objects.get(user=user)
    except EmployeeEducation.DoesNotExist:pass

    return render(request,'my_education.html',locals())



def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
    try:
        education,_ = EmployeeEducation.objects.get_or_create(user=user)
    except EmployeeEducation.DoesNotExist:pass
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassing = request.POST['yearofpassing']
        percentagepg = request.POST['percentagepg']
        
        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassingra = request.POST['yearofpassingra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingra = yearofpassingra
        education.percentagegra= percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingra = yearofpassingra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc
        
       

        try:
            education.save()
            
                
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_myeducation.html',locals())



def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = request.user
  
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_passord(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request,'change_password.html',locals())

    
def admin_login(request):
    error = ""
    if request.method == "POST":
        U = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username=U, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error="yes"
    return render(request,'admin_login.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')



def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = ""
    user = request.user
  
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            if user.check_password(c):
                user.set_passord(n)
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request,'change_passwordadmin.html',locals())

def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee = EmployeeDetail.objects.all()
    return render(request,'all_employee.html')

def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.get(id=pid)
    user.delete()
    return render(request,'delete_employee')


def edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = ""
  
    employee = EmployeeDetail.objects.get(id=pid)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.user.empcode = ec
        employee.user.empdept = dept
        employee.user.designation = designation
        employee.user.contact = contact
        employee.user.gender = gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
                
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_profile.html',locals())


def edit_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassing = request.POST['yearofpassing']
        percentagepg = request.POST['percentagepg']
        
        coursegra = request.POST['coursegra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassingra = request.POST['yearofpassingra']
        percentagegra = request.POST['percentagegra']

        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']

        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']

        education.coursepg = coursepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingra = yearofpassingra
        education.percentagegra= percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingra = yearofpassingra
        education.percentagegra = percentagegra

        education.coursessc = coursessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc

        education.coursehsc = coursehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc
        
       

        try:
            education.save()
            
                
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_education.html',locals())




def edit_mexperience(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    user = User.objects.get(id=pid)
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1desig= request.POST[' company1desig']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']
        
        company2name = request.POST['company2name']
        company2desig= request.POST[' company2desig']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']
        
        company3name = request.POST['company3name']
        company3desig= request.POST[' company3desig']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']

        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration = company1duration

        experience.company2name = company2name
        experience.company2desig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        
       

        try:
            experience.save()
            
                
            error = "no"
        except:
            error = "yes"
    return render(request,'edit_mexperience.html',locals())