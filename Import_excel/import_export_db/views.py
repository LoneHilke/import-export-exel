from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import Employee

from tablib import Dataset
from .Resources import EmployeeResource
 
# Create your views here.
 
def Import_Excel_pandas(request):
     
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(filename)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Employee.objects.create(Navn=dbframe.Navn, Gruppe=dbframe.Gruppe,
                                            Morgen=dbframe.Morgen, Eftermiddag=dbframe.Eftermiddag, Ferie=dbframe.Ferie, 
                                            Alder=dbframe.Alder )           
            obj.save()
        return render(request, 'Import_excel_db.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'Import_excel_db.html',{})

def Import_excel(request):
    if request.method == 'POST' :
        Employee =EmployeeResource()
        dataset = Dataset()
        new_employee = request.FILES['myfile']
        data_import = dataset.load(new_employee.read())
        result = EmployeeResource.import_data(dataset,dry_run=True)
        if not result.has_errors():
            EmployeeResource.import_data(dataset,dry_run=False)        
    return render(request, 'Import_excel_db.html',{})



#fra; https://labpys.com/import-data-from-excel-into-database-using-django/#Create_Django_project