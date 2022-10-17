from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import ( contactUsForm,mywork,
TechSkills,socialicons,refrences,Contactus,carosuel_info )

from django.contrib import messages
# Create your views here.
from .models import Resume

def home(request):
    resume=Resume.objects.all()
    work_links=mywork.objects.filter().order_by('-date')[0:8]
    techskill=TechSkills.objects.all()
    social_icon=socialicons.objects.all()
    referenc=refrences.objects.all()
    carosuel=carosuel_info.objects.all()

    if request.method=='POST':
        form = contactUsForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message_1 = form.cleaned_data['message']
            if not Contactus.objects.filter(email=email).exists():
                print("Trueeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                form.save()
                messages.success(request, 'Thank You! We will contact you shortly…')
            else:
                messages.warning(request, "Email already exists.")
                return HttpResponse("elsesssssspart")
        
    
    else:
        form=contactUsForm()

    context={
        "form":form,
        'resume':resume,
        'work_links':work_links,
        'techskill':techskill,
        'social_icon':social_icon,
        'referenc':referenc,
        'carosuel':carosuel,
    }
    
    return render(request,"index.html",context)
            
                

        


