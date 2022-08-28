from django.shortcuts import render 
from dashboard.models import StudentInfo
from dashboard.forms import StudentInfoForm


def home_page(request):
	fm=StudentInfoForm
	obj=StudentInfo.objects.all()
	if request.method == 'POST':
		fs=StudentInfoForm(request.POST)
		if fs.is_valid():
			name=fs.cleaned_data['name']
			email=fs.cleaned_data['email']
			reg=StudentInfo(name=name,email=email)
			reg.save()
	return render(request,'home_page.html',{'form':fm,'md':obj})