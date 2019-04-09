from .forms import RegistrationForm
from .models import CSVUpload
from django.shortcuts import render, redirect


def welcome(request):
	csv_list = CSVUpload.import_data(data = open(request.csv))
	return render(request, 'exercisetry/base.html')


def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login.html')
	else:
		form = RegistrationForm()
	return render(request, 'registration/registration.html', {'form' : form})