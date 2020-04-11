"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [

    path('',views.welcome),
    path('login/',views.login),
    path('404/',views.error),
    path('profile/',views.profile),
    path('generateqrcode/',views.generateqrcode),

    

  
    path('create/patient/',views.createaccountpatient),
    path('create/doctor/',views.doctoraccount),
    path('login/patient/',views.AuthenticateU),
    path('doctorhompage/',views.doctorhompage),
    path('medicals/',views.medicals),
    path('create/medicals/',views.createaccountmedicals),
    path('medicals/homepage/',views.medicalshomepage),

    path('customfields/',views.customfields),
    
    path('uploadqrcode/',views.uploadqrcode),

    

    # path('patientrecord/',views.patienthomepage),

    path('login/doctor/',views.AuthenticateD),
    path('login/medicalslogin/',views.AuthenticateM),

    path('revoke/',views.revoke),
    path('patient/',views.patient),
    path('doctor/',views.doctor),
    path('patientaccountcreation/',views.createaccountpatient),

    # path('patient/',views.profile),
    # path('doctor/',views.forms),
    path('doctoraccount/',views.doctoraccount),

    
    # patient profile
    path('patienthomepage/',views.patienthomepage),
    path('patientpresciption/',views.patientpresciption),
    # path('statisticalreport/',views.statisticalreport),
    path('consenteddoctor/',views.consenteddoctor), 
    path('otpverify/',views. verify),
    path('userdetailsreg/',views.userdetailsreg),

    
    # doctor profile
    path('patientrecord/',views.patientrecord),
    path('registeredpatientinfo/',views.registeredpatientinfo),
    path('labprescription/',views.labprescription),
    path('Medications/',views.Medications),
    
    path('createaccountU/',views.createaccountU),
    path('createaccountD/',views.createaccountD),
    path('createaccountM/',views.createaccountM),

    # path('charts/',views.charts),


    # path('registeredpatientinfo/patientrecord/',views.patientrecord),

    # path('signup/',views.createaccount),

    # path('index/',views.home),

    # path('404page/',views.error),
    # path(r'^$',views.login),
   
    # path('index/',views.welcome),
    # path('profile/',views.profile),
   

    # path('login/',views.login),
    # path('',views.welcome),
    # path('profile/',views.profile),


    
    # path('',views.profile),

    # path('',views.charts),

    # path('form/',views.forms),
    # path('',views.tables),
    # path('',views.profile), 
    # path('adminaccount/',views.adminAccount),
    # path('User/',views.User),
    # path('homeloan/successfull/',views.successfull),
  
]
