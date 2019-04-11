from django.shortcuts import render, redirect

from .forms import RegistrationForm, PersonCreationForm

from django.contrib.auth.decorators import login_required
from .models import PersonDetail
import csv
from django.http import HttpResponse

import os

def welcome(request):
	return render(request, 'exercisetry/welcome.html')


def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegistrationForm()
	return render(request, 'registration/registration.html', {'form':form})


@login_required
def person_creation(request):
	if "csv_export" in request.GET:
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
		writer = csv.writer(response)
		holderquery = PersonDetail.objects.filter(user_id=request.user.pk)
		writer.writerow([PersonDetail.firstname])
		for x in holderquery:
			writer.writerow([x.firstname, x.lastname, x.address])
		return response

	# if request.method == 'POST':
	# 	form = PersonCreationForm(request.POST)
	# 	if form.is_valid():
	# 		form = form.save(commit=False)
	# 		form.user = request.user
	# 		form.save()
	# 		return redirect('person_creation')

	
	if request.method == 'POST':
		uploadedcsvfile = request.FILES['csv_file'].name
		with open(uploadedcsvfile) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				ukulele = PersonDetail(firstname=row['firstname'], lastname=row['lastname'], phone_number=row['phone_number'])
				gitar = PersonCreationForm(ukulele)
				if gitar.is_valid():
					gitar.save()
			# if form.is_valid():
			# 	form = form.save(commit=False)
			# 	form.user = request.user
			# 	form.save()

	form = PersonCreationForm()
	return render(request, 'exercisetry/person_creation.html', {'form':form})