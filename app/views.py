from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import teacher
from django.contrib import messages
from app.models  import student
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import course
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request,'attendance.html')

def login(request):
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password']
       x=auth.authenticate(username=username,password=password)
       if x is None:
             return redirect('/')   
             print(hi)
       else:
            return render(request,'profile1.html')
            print(hello)
    else:
        return render(request,'attendance.html')
        print(hii)



def t_details(request):
    t=''
    # id=none
    data={}
    if request.method=="POST":
        id = request.POST.get("id")
        print("id")
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        DOB=request.POST.get('DOB')
        gender=request.POST.get('gender')
        ocuupation=request.POST.get('ocuupation')
        id_name=request.POST.get('id_name')
        id_no=request.POST.get('id_no')
        issue_date=request.POST.get('issue_date')
        post=request.POST.get('post')
        branch=request.POST.get('branch')
        # if id is none:
            # id=0
        data=teacher(t_id = id,t_name=name,t_mail=email,t_phno=phno,t_DOB=DOB,t_Gender=gender,t_Occupation=ocuupation,tid_name=id_name,tid_no=id_no,t_post=post,t_branch=branch)
        # data=teacher(tid_name=id_name,tid_no=id_no,t_id = id)
        # id = int(id)
        # print(id)
        data.save()
        t='Data Inserted'
        # profileobj = get_object_or_404(teacher, pk=id)
        # print(profileobj)
        # id = int(id)
        
        return redirect("/teacher_info/%s/"%(id))
    return render(request,"Registration1.html",{'data':data})


def teacher_info(request,id):
    profileobj = get_object_or_404(teacher, pk=id)
    if request.method =="GET":
        return render(request,"profile1.html",{"data":profileobj})
    else:
        return HttpResponse("DATA NOT FOUND")

def logout(request):
    auth.logout(request)
    # messages.info(request,'logout succesfull')
    return redirect('/')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        confirm_password = request.POST['confirm_password']
        try:
            user = User.objects.create_user(username,password,email)
            user.save()
            # messaage.success(request,"User created")
            print("user created")
        except:
            return HttpResponse("user already exist.")
        # myuser = User.objects.create_user(username,email,password)
        # myuser.save()
        # user.save()
       
        return redirect('/t_details')
    else:  
        return render(request,'sign_up.html')


# def fy_cform(request):
#     t=''
#     data={}
#     if request.method=="POST":

def fy_cform(request):
    # print("hii2")
    t=''
    cdata={ }
    if request.method == "POST":
        
        code=request.POST.get('code')
        print("code")
        name=request.POST.get('name')
        # print("hi")
        credit=request.POST.get('credit')
        semester=request.POST.get('semester')
        # id=request.POST.get('id')
        cdata=course(c_name=name,c_code=code,c_credit=credit,c_semester=semester)
        print("hi")
        cdata.save()
        print("hello")
            
        t='Data Inserted'
        return redirect("fy_cdetails")
        # print(hi)
    return render(request,"1stYear.html",{'cdata':cdata})
    # print(hello)


def fy_cdetails(request):
    c_detail = course.objects.filter( c_teacher= c_teacher,c_code=c_code)
    cdata ={
         'c_detail' : c_detail
           }
    return render(request,"table1.html",cdata)


def sy_form(request):
    # print("hii2")
    t=''
    cdata={ }
    if request.method == "POST":
        code=request.POST.get('code')
        print("code")
        name=request.POST.get('name')
        # print("hi")
        credit=request.POST.get('credit')
        semester=request.POST.get('semester')
        cdata=course(c_name=name,c_code=code,c_credit=credit,c_semester=semester)
        cdata.save()
        t='Data Inserted'
        return redirect("sy_details")
        # print(hi)
    return render(request,"2ndYear.html",{'cdata':cdata})
    # print(hello)



def sy_details(request):
    # c_detail = course.objects.all()
    # cdata ={
    #      'c_detail' : c_detail
    #        }
    return render(request,"table2.html")



def ty_form(request):
    # print("hii2")
    t=''
    cdata={ }
    if request.method == "POST":
        code=request.POST.get('code')
      
        name=request.POST.get('name')
        # print("hi")
        credit=request.POST.get('credit')
       
        semester=request.POST.get('semester')
       
        cdata=course(c_name=name,c_code=code,c_credit=credit,c_semester=semester)
        cdata.save()
        t='Data Inserted'
        return redirect("ty_details")
        # print(hi)
    return render(request,"3rdYear.html",{'cdata':cdata})
    # print(hello)

def ty_details(request):
    # c_detail = course.objects.all()
    # cdata ={
    #      'c_detail' : c_detail
    #        }
    return render(request,"table3.html")



def ly_form(request):
    # print("hii2")
    t=''
    cdata={ }
    if request.method == "POST":
        code=request.POST.get('code')
      
        name=request.POST.get('name')
        # print("hi")
        credit=request.POST.get('credit')
       
        semester=request.POST.get('semester')
       
        cdata=course(c_name=name,c_code=code,c_credit=credit,c_semester=semester)
        cdata.save()
        t='Data Inserted'
        return redirect("ly_details")
        # print(hi)
    return render(request,"4thYear.html",{'cdata':cdata})
    # print(hello)


def ly_details(request):
    # c_detail = course.objects.all()
    # cdata ={
    #      'c_detail' : c_detail
    #        }
    return render(request,"table4.html")