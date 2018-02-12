import os
from django.shortcuts import render
from .forms import *
from hack import fun1,predict
# Create your views here.


def home(request):
	if request.method == 'POST':
		form = InfoForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			data =  [ form.cleaned_data['name'],
			  form.cleaned_data['time_study'],
			  form.cleaned_data['time_travel'],
			  form.cleaned_data['age'],
			  form.cleaned_data['time_friends'], 
 			  form.cleaned_data['relationship'],
			  form.cleaned_data['studies_higher'],
			  form.cleaned_data['fam_ed'],
			  form.cleaned_data['G1'],
                          form.cleaned_data['G2'],
                          form.cleaned_data['failed'],
			  form.cleaned_data['gender'],
				] 
		val = predict(data)                        
		return render(request,'ai/home.html',{'info_form':form,'val':val})
	#form = InfoForm()
	#print "ere"
	#val ,val2= fun1()
	#print val2

	else:
		form = InfoForm()
		return render(request,'ai/home.html',{'info_form':form})
