from django import forms


class InfoForm(forms.Form):
	
	name = forms.CharField(max_length = 100)
	time_study = forms.IntegerField()
	time_travel = forms.IntegerField()
	age = forms.IntegerField()
	time_friends = forms.IntegerField()
	relationship = forms.CharField(max_length = 10)
	studies_higher = forms.CharField(max_length = 10)
	fam_ed = forms.IntegerField()
	G1 = forms.IntegerField()
	G2 = forms.IntegerField()
	failed = forms.IntegerField()
	gender = forms.CharField(max_length = 100)



	#fiel = ('name','time_study','time_travel','age','time_friends','relationship','studies_higher','fam_ed','G1','G2','failed','gender')
