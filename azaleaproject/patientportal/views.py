from django.shortcuts import render
from . import apihelper

def home(request):

    # patient_data = apihelper.get_all_patients()
    patient_data = apihelper.get_patient(390671)
    context = {'patient_data': patient_data}

    return render(request, 'patientportal/home.html', context=context)