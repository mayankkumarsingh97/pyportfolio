from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contactUsForm,mywork,TechSkills,socialicons
from django.contrib import messages
# Create your views here.
from .models import Resume
def home(request):
    resume=Resume.objects.all()
    work_links=mywork.objects.all()
    techskill=TechSkills.objects.all()
    social_icon=socialicons.objects.all()
    if request.method=='POST':
        form = contactUsForm(request.POST or None)
        try:
            if form.is_valid():
                name = form.cleaned_data.get('name')
                lastname = form.cleaned_data.get('lastname')
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data['phone']
                message_1 = form.cleaned_data['message']
                print(name,"namenamenamenamenamename")
                print(lastname,"lastttttttttttname")
                print(email,'emailllllllllllllllllllll')
                print(phone,'phoneeeeeeeeeeeeeee')
                print(message_1,'message_1message_1message_1message_1')
                form.save()
                messages.success(request, 'Thank You! We will contact you shortly…')
                return redirect("home")
        except:
            print("db validation error")
        
    else:
        form=contactUsForm()
    context={
        "form":form,
        'resume':resume,
        'work_links':work_links,
        'techskill':techskill,
        'social_icon':social_icon
    }
    
    return render(request,"index.html",context)


