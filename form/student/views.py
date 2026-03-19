from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def student_form(request):
    message=""

    if request.method=='POST':
        form=StudentForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            age=form.cleaned_data['age']

            message=f"Submitted:{name},{email},{age}"

    else:
        form=StudentForm()

    return render(request,'form.html',{'form':form, 'message':message})