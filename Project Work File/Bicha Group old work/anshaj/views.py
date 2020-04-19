from django.shortcuts import render,redirect
from .models import job_post,applyed_candidates,imp_messages
from django.db.models import Q
from django.contrib import messages
# Create your views here.


def index(request):
    jobpost        =   job_post.objects.all()
    return render(request,'anshaj/index.html',{'jobpost':jobpost})


def aboutus(request):
    return render(request,'anshaj/about-us.html')


def contact(request):
    return render(request,'anshaj/contact.html')


def category(request):
    return render(request,'anshaj/category.html')


def postjob(request):
    
    if request.method   ==  'POST':
        
        title       = request.POST.get("title")
        company_name= request.POST.get("company_name")
        des         = request.POST.get("des")
        job_nature  = request.POST.get("job_nature")
        location    = request.POST.get("location")
        salary      = request.POST.get("salary")
        tag_1       = request.POST.get("tag_1")
        tag_2       = request.POST.get("tag_2")
        tag_3       = request.POST.get("tag_3")
        img         = request.FILES.get("img")
        datetime    = request.POST.get("datetime")
        code        = request.POST.get("code")

        postjob                 = job_post()
        postjob.img             = img
        postjob.title           = title
        postjob.company_name    = company_name
        postjob.des             = des
        postjob.job_nature      = job_nature
        postjob.location        = location
        postjob.salary          = salary
        postjob.tag_1           = tag_1
        postjob.tag_2           = tag_2
        postjob.tag_3           = tag_3
        postjob.datetime        = datetime
        postjob.code            = code
        
        postjob.save()
        messages.info(request,'Job Posting Successful')
        return redirect('postjob')

    else:

        applyed_candi     =   applyed_candidates.objects.all()

        return render(request,'anshaj/postjob.html',{'applyed_candidates':applyed_candi})


def search(request):
    
    if request.method       ==  'POST':

        search_title       = request.POST['title']
        
        if search_title:
            print('/////////////////////////////////////////')
            match       = job_post.objects.filter(Q(title__icontains=search_title))

            if match:
                return render(request,'anshaj/search.html',{'match':match})
                
            else:
                messages.info(request,'Search was not found')
                return redirect('index')

        else:
            messages.info(request,'Please enter any value')
            return redirect('index')
    
    else:
        return render(request,'anshaj/search.html')


def apply(request):

    if request.method == 'POST':

        title   = request.POST.get("apply_title")
        job     = job_post.objects.get(code=title)
        print(title,'---------------')
        return render(request,'anshaj/apply.html',{'job':job})


    else:

        return render(request,'anshaj/apply.html')


def applying(request):
    
    if request.method  ==  'POST':

        givenname       = request.POST.get("givenname")
        surename        = request.POST.get("surename")
        email           = request.POST.get("email")
        phonenumber     = request.POST.get("phonenumber")
        file            = request.FILES.get("file")
        code            = request.POST.get("code")

        applying                            = applyed_candidates()
        applying.candidates_givenname       = givenname
        applying.candidates_surename        = surename
        applying.candidates_email           = email
        applying.candidates_phonenumber     = phonenumber
        applying.code                       = code
        applying.candidates_resume          = file
        
        applying.save()
        return redirect('index')

    else:

        return render(request,'anshaj/apply.html')



def impmessage(request):

    if request.method   == 'POST':
        imp_message     = request.POST.get("imp_message")
        imp_datetime    = request.POST.get("datetime")
        
        imp             = imp_messages()
        imp.message     = imp_message
        imp.datetime    = imp_datetime

        imp.save()
        return redirect('postjob')

    else :
        imp             = imp_messages.objects.all()
        return render(request,'anshaj/postjob.html',{'imp':imp})
