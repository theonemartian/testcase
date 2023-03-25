from django.shortcuts import render
from django.http import HttpResponse
import os
import pandas as pd
import openai
# Create your views here.
def home(request):
    return render(request,'home.html')

def generate(request):
    if request.method == 'POST':
        key = request.POST.get('api_key')
        feature  = request.POST.get('feature')
        heading = request.POST.get('heading')
        
    


    openai.api_key = key

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    
    temperature=0.5,


    messages = [
        {'role': 'system', 'content': '''Write all possible test Cases and scenarios for the feature ,
        Feature is :'''+feature}
    ],
    )
    
    data=response.choices[0].message.content
    scenario = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    
    temperature=0.5,


    messages = [
        {'role': 'user', 'content': '''Convert the following data in a list of dictionaries like this: {"Scenario": "Copying consent and refreshing report for a customer with a report generated within the last 6 months",
        "Steps": "1. Open loan booking flow\n2. Initiate session for a customer with a report generated within the last 6 months\n3. System should automatically copy consent and refresh report using ondemand API",
        "Input": "Customer ID, report generated date",
        "Expected output": "Loan manager sees refreshed report without the need to open mweb and record consent"},
        {"Scenario": "Copying consent and refreshing report for a customer with a report generated more than 6 months ago",
        "Steps": "1. Open loan booking flow\n2. Initiate session for a customer with a report generated more than 6 months ago\n3. System should prompt loan manager to open mweb and record consent\n4. After consent is recorded, system should copy it and refresh report using ondemand API",
        "Input": "Customer ID, report generated date",
        "Expected output": "Loan manager sees refreshed report after recording consent in mweb"},
        
    '''+'data is:'+data}  ],
    )
    
    
    
    testcase_sheet=scenario.choices[0].message.content
    df=pd.DataFrame(eval(testcase_sheet))
    
    
    my_dict={'df': df.to_html(),'heading': heading}
    return render(request,'generate.html',context=my_dict)   

 


     
    