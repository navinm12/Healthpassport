from django.shortcuts import render
from django.shortcuts import redirect
from .mailacknowledgement import emailit
from .state_management import User_state_creation,get_state_user,doctor_state_creation,get_state_doctor,Patient_state_creation,get_state_patient,Medical_state_creation,get_state_Medical
import requests
import time
import json
from datetime import datetime
from twilio.rest import Client

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from web3 import Web3
from pyzbar.pyzbar import decode
from PIL import Image

import qrcode
import json
import os


baseurl='http://127.0.0.1:8080/api'
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi=json.loads('[{"constant":true,"inputs":[{"name":"doctor","type":"address"}],"name":"getDoctorsPermissions","outputs":[{"name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"doctor","type":"address"}],"name":"giveAccessToDoctor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"doctorsPermissions","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"doctor","type":"address"},{"name":"index","type":"uint256"}],"name":"revokeAccessFromDoctor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
address= "0x9181e120A9B4A27Cc620b965966d133fB9d7DCD8"
contract= web3.eth.contract(address=address, abi=abi)



def AuthenticateD(request):
    if(request.method=='POST'):
        email=request.POST.get('username')
        password=request.POST.get('passowrd')

        print(email,password) 
    
        try:
            data={'docEmail':email,'password':password}
            url=baseurl+'/Doctor/doctorAuthetication/' 
            response = requests.post(url, data=data)
            print(response)
            res=response.json()
            print(res)
            if(res["message"] == "Login successful"):
                print("Doctor login")
                
                print(res['doctor']['doctorName'])
                print(res['doctor']['doctorethAddress'])
                print(res['doctor']['hospitalName'])
                print(res['doctor']['docEmail'])

                doctor_state_creation(email,res['doctor']['doctorName'],res['doctor']['hospitalName'],res['doctor']['doctorethAddress'],'Doctor')
                res=redirect('/patientrecord/')
            else:
                res=redirect('/404/')  
        except:
            res=render(request,'404page.html')
    return res

def medicals(request):
    return render(request,'medicals.html',{'typeofuser':'medicalslogin/','image':'medicalshop.png','message':'Medicals','createaccounttype':'/create/medicals/'})

def createaccountmedicals(request):
    details={'urlmap':'/createaccountM/',}
    print('Medical_account_created')
    return render(request,'createmedicalaccount.html',details)

def medicalshomepage(request):
    user_detail=get_state_Medical()
    print(user_detail)
    email = user_detail[0]
    medname =user_detail[1]
    ownername = user_detail[2]
    print(email,medname,ownername)
    details={'status':'approved','medicalname':medname,'Ownername':ownername,'status':'fail',}

    return render(request,'medicalhomepage.html',details)


def generateqrcode(request):
    user_detail=get_state_user()
    print(user_detail)
    email = user_detail[0]
    name =user_detail[1]
    typeofuser = user_detail[2]
    msg= name + ' ' + email
    topic='Profile'

    print(msg)
    img = qrcode.make(msg)
    print(type(img))
    print(img.size)

    # img.save(filename)
    # path='/SIP/2nd new/HealthpassportV5.17/Healthpassportv'+"'//"+ name+'.jpg'
    # img.save('static/' + name+ '.png')
    img.save('responseapp/static/img/' + name+ '.png')
    # filename='responseapp/static/img/' + name+ '.png'
    filename= name+ '.png'
    print(filename)

    
    # print(path)
    # filename=path
    # img.save(path)
    # print(filename)
  
    # print('imgsaved')
    # a = os.path.abspath('/responseapp/static/img/')
    # syspath='/responseapp/static/img/'+filename
    # print(syspath)

    details={'Patientqrcode':topic,'username':name,'type':typeofuser,'nameRegistered':name,'filename':filename,}
    return render(request,'qrcodepage.html',details)






def uploadqrcode(request):
    if(request.method=='POST'):
        user_detail=get_state_Medical()
        print(user_detail)
        email = user_detail[0]
        medname =user_detail[1]
        ownername = user_detail[2]
        print(email,medname,ownername)
        myFile=request.POST.get('myFile')
        path=os.path.abspath(myFile)
        d = decode(Image.open(path))
        # print(d)
        print('decoded')
        qrmsg= d[0][0]
        print(qrmsg)
        # # print(type(qrmsg))
        q = str(qrmsg)
        # print(q)
        q =q.replace('b', '')
        q =q.split(' ')
        print(q)
        name=q[0]
        name=name.replace("'", '')
        address=q[1]
        address=address.replace("'", '')
        print(name)
        print(address)

        
        
        try:
            data={'email':address}
            url=baseurl+'/Medication/getPrescription/' 
            responseM = requests.post(url, data=data)
            print(responseM)
            resM=responseM.json()
            print(resM)
            print(len(resM))
            last=len(resM)-1
            print(last)
            Prescription=resM[last]['prescription']       
            # Suggestions=resM[0]['suggestions']

        
        except:
                res=render(request,'404page.html')

    details={'status':'approved','medicalname':medname,'Ownername':ownername,'Prescription':Prescription,'patientname':name,}
    return render(request,'medicalhomepage.html',details)


def AuthenticateM(request):
    if(request.method=='POST'):
        email=request.POST.get('username')
        password=request.POST.get('passowrd')
        print('medicalsathentication')
        print(email,password) 
    
        try:
            data={'email':email,'password':password}
            url=baseurl+'/medicallogin/medicalAuthetication/' 
            response = requests.post(url, data=data)
            print(response)
            res=response.json()
            print(res)
            if(res["message"] == "Login successful"):
                print("Doctor login")
                print(res['medical']['shopname'])
                print(res['medical']['ownername'])
                print(res['medical']['email'])
                Medical_state_creation(res['medical']['email'],res['medical']['shopname'],res['medical']['ownername'])
                user_detail=get_state_Medical()
                print(user_detail)
                email = user_detail[0]
                medname =user_detail[1]
                ownername = user_detail[2]
                print(email,medname,ownername)
                res=redirect('/medicals/homepage')
            else:
                res=redirect('/404/')                
               
                

        except:
            res=render(request,'404page.html')
    return res



def profile(request):
    if(request.method=='POST'):
        user_detail=get_state_user()
        print(user_detail)
        email = user_detail[0]
        name =user_detail[1]
        typeofuser = user_detail[2]
        res=''
        try:
            data={'email':email,}
            url=baseurl+'/deleteone/patientdelete/' 
            response = requests.post(url, data=data)
            print(response)
            res=response.json()
            print(res['message'])
            if res['message'] == "Deleted successfull":
                print('yes')
                red=redirect('/patient/')

            # else:
            #     res=redirect('/404/')  
        except:
            red=render(request,'404page.html')
    return red

    # return render(request,'index.html')
 
def AuthenticateU(request):
    if(request.method=='POST'):
        email=request.POST.get('username')
        password=request.POST.get('passowrd')
        print(email,password) 

        try:
            data={'email':email,'password':password,}
            url=baseurl+'/User/PatientAuthetication/' 
            response = requests.post(url, data=data)
            print(response)
            res=response.json()
            print(res)
            if(res['message'] =='Login Successful'):
                print(res['user']['firstName'])
                User_state_creation(res['user']['email'],res['user']['firstName'],'patient')
                user_detail=get_state_user()
                print(user_detail)
                email = user_detail[0]
                name =user_detail[1]
                typeofuser = user_detail[2]
                print(email,name,typeofuser)
                res=redirect('/patienthomepage/')
            elif (res['message'] =='User not found'):
                res=redirect('/404/') 
            else:
                res=redirect('/404/')  
        except:
            res=render(request,'404page.html')
    return res

def error(request):
    return render(request,'404page.html')





# def revoke(request):
def revoke(request):
    if(request.method=='POST'):
        dtime=request.POST.get('dtime')
        dtime =dtime.replace('+', ' ')
        print(dtime)
        user_detail=get_state_user()
        print(user_detail)
        email = user_detail[0]
        name =user_detail[1]
        typeofuser = user_detail[2]
        print(dtime)

        doctortinfo=[]
        zipped=[]
        doctorrevokeinfo=[]
        revokezipped=[]

        try:
            data={'dtime':dtime,}
            url=baseurl+'/Patientconsent/statusupdate/' 
            response = requests.post(url, data=data)
            print(response)
            ress=response.json()
            print('doctor address')
            print(ress)
            print(ress['dethaddress'])
            docethaddress=ress['dethaddress']



            data={'email':email,}
            url=baseurl+'/Patientconsent/getPatientconsent/' 
            response = requests.post(url, data=data)
            print(response)
            resB=response.json()
            print(resB)

            print(len(resB))
            lengthofresponse=len(resB)
            print(lengthofresponse)

            data={'email':email}
            url=baseurl+'/Patientdetails/getPatient/'
            response = requests.post(url, data=data)
            print(response)
            txtres=response.json()
            print(txtres)
            userethaddress = txtres['ethAddress']
            print(userethaddress)

            




            # Revoke permission from doctor
            print("sadsfffffffffffffffffffffffffffffff")
            # ind=allpatient.index(userethaddress)
            # print(ind)
            
            web3.eth.defaultAccount=userethaddress
            revoke=contract.functions.revokeAccessFromDoctor(docethaddress,0).transact()
            print("s")
            
            # allpatient=contract.functions.getDoctorsPermissions(docethaddress).call()
            # print(allpatient)



            for x in range(0,lengthofresponse):
                doctortinfo=[]
                print('finished')

                dname=resB[x]['dname']
                dethaddress=resB[x]['dethaddress']
                dhospital=resB[x]['dhospital']
                dtime=resB[x]['dtime']
                rstatus=resB[x]['status1']
                # print(x,rstatus)
                Date,Time= dtime.split(" ")
                # print(Date,Time)

                if rstatus =='true':
                    # print('revoked')
                    doctortinfo.append(dname)
                    doctortinfo.append(dethaddress)
                    doctortinfo.append(dhospital)
                    doctortinfo.append(x+1)
                    doctortinfo.append(Date)
                    doctortinfo.append(Time)
                    zipped.append(doctortinfo)
                    

                # print(zipped)
                else:
                    # print('not_revoked')

                    doctorrevokeinfo.append(dname)
                    doctorrevokeinfo.append(dethaddress)
                    doctorrevokeinfo.append(dhospital)
                    doctorrevokeinfo.append(x+1)
                    doctorrevokeinfo.append(Date)
                    doctorrevokeinfo.append(Time)
                    revokezipped.append(doctorrevokeinfo)

                


        except:
            res=render(request,'404page.html')

    details={'username':'barathraj','type':'patient','username':'barath','type':'patient','zipped':zipped,'revokezipped':revokezipped,}

    # details={'username':'barathraj','type':'patient','username':name,'type':'patient','zipped':zipped,}
    return render(request,'consenteddoctor.html',details)


    # return render(request,'consenteddoctor.html')

def customfields(request):
    if(request.method=='POST'):
        field=request.POST.get('Schoolname[]')
        val=request.POST.get('Major[]')
        print(field)
        print(val)
  
    details={'doctorname':'barathsample','status':'approved','Bstatus':'notupdated','doctype':'doctor','statusP':'updatedP',}  
    return render(request,'patientrecord.html',details)








def createaccountM(request):
    if(request.method=='POST'):
        MedicalName=request.POST.get('Mname')
        shopowner=request.POST.get('shopOwner')
        MedEmail=request.POST.get('email')
        password=request.POST.get('password')
        # Medical_state_creation(MedEmail,MedicalName,shopowner)
        # print(MedicalName,shopowner,MedEmail,password) 
    
        try:
            data={'shopname':MedicalName,'ownername':shopowner,'email':MedEmail,'password':password}
            url=baseurl+'/medicallogin/medicalregister/'
            response = requests.post(url, data=data)
            print(response) 
            res=response.json()
            print(res)
            Medical_state_creation(MedEmail,MedicalName,shopowner)
            print(MedicalName,shopowner,MedEmail,password)
            details={'status':'fail','medicalname':MedicalName,'Ownername':shopowner,}
            res =render(request,'medicalhomepage.html',details)
             
            # if(res["message"] == "Medical login Created"):
            #     print('medicalshop account created')
        #         res=redirect('/patientrecord/')
        #     else:
        #         res=redirect('/404/')
        except:
            res=render(request,'404page.html')
    return res



def patient(request):
    # emailit()
    # print('doneemail')
    return render(request,'login.html',{'typeofuser':'patient/','image':'patientprofilepic.png','message':'Patient','createaccounttype':'/create/patient/'})

def doctor(request):
    return render(request,'login.html',{'typeofuser':'doctor/','image':'logincrpimg.jpg','message':'Doctor','createaccounttype':'/create/doctor/'})

def login(request):
    if(request.method=='POST'):
        email=request.POST.get('username')
        password=request.POST.get('passowrd')
    return render(request,'login.html')


def welcome(request):
    return render(request,'index.html')


def patienthomepage(request):
    user_detail = get_state_user()
    email = user_detail[0]
    name =user_detail[1]
    typeofuser = user_detail[2]
    print(email,name,typeofuser)  

    details={'PatientRegistration':'Patient Registration','username':name,'type':typeofuser,'nameRegistered':name}
    return render(request,'patienthomepage.html',details)

def userdetailsreg(request):
    user_detail=get_state_user()
    print('in')
    email = user_detail[0]
    pname =user_detail[1]
    print('end')

    if(request.method=='POST'):
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        mobileNumber=request.POST.get('mobileNumber')
        fatherName=request.POST.get('fatherName')
        address=request.POST.get('address')
        bloodGroup=request.POST.get('bloodGroup')
        ethAddress=request.POST.get('ethAddress')
        print(email,pname,age,gender,dob,mobileNumber,fatherName,address,bloodGroup,ethAddress)

        try:
            data={'email':email,'ethAddress':ethAddress,'name':pname,'age':age,'gender':gender,'dob':dob,'mobileNumber':mobileNumber,'fatherName':fatherName,'address':address,'bloodGroup':bloodGroup,}
            url=baseurl+'/Patientdetails/patientRegistration/' 
            response = requests.post(url, data=data)
            print(response)
            res=response.json()
            print(res)
                
            if(res['message'] =="Registration complete"):
                # block ='activated'
                print('activated')
                res=redirect('/patienthomepage/')

            elif (res['message'] =='error-occured'):
                print('in')
                block ='activatefail'
                res=redirect('/404/') 
            else:
                res=redirect('/404/')  
        except:
            res=render(request,'404page.html')

    details={'PatientRegistration':'Patient Registration','username':'barathraj','type':'patient','regblock':'activated','nameRegistered':pname}
    return render(request,'patienthomepage.html',details)
    
def patientpresciption(request):
    results=[]
    user_detail=get_state_user()
    print(user_detail)
    email = user_detail[0]
    name =user_detail[1]
    typeofuser = user_detail[2]
    report={}
    records=[]
    zipped=[]
    age=''
    dob=''
    bloodGroup=''
    try:
        data={'email':email}
        url=baseurl+'/Patientdetails/getPatient/'
        response = requests.post(url, data=data)
        print(response)
        txtres=response.json()
        print(txtres)
        number = txtres['mobileNumber']
        userethaddress = txtres['ethAddress']
        age=txtres['age']
        dob=txtres['dob']
        bloodGroup=txtres['bloodGroup']
        print(age,dob,bloodGroup)


        data={'email':email,}
        url=baseurl+'/Bloodtest/getBloodresult/' 
        response = requests.post(url, data=data)
        print(response)
        resB=response.json()
        print(resB)


        url=baseurl+'/Sugartest/getSugarresult/' 
        responseS = requests.post(url, data=data)
        print(responseS)
        resS=responseS.json()
        print(resS)



        url=baseurl+'/Cmptest/getCmpresult/' 
        responseC = requests.post(url, data=data)
        print(responseC)
        resC=responseC.json()
        print(resC)


        url=baseurl+'/Medication/getPrescription/' 
        responseM = requests.post(url, data=data)
        print(responseM)
        resM=responseM.json()
        print(resM)
        print(report)
        print(len(resB))
        lengthofresponse=len(resB)
        print(lengthofresponse)
        for x in range(0,lengthofresponse+1):
            records=[]
            print('finished')

            Haemoglobin=resB[x]['hemoglobin']
            WBC_count=resB[x]['whiteBloodCells']
            RBC_count=resB[x]['redBloodCells']
            Platelets_count=resB[x]['platelets']

            Before_meal=resS[x]['beforemeal']
            After_meal=resS[x]['aftermeal']


            Glucose=resC[x]['glucose']
            Sodium=resC[x]['sodium']
            Potassium=resC[x]['potassium']
            Chloride=resC[x]['chloride']

            
            Prescription=resM[x]['prescription']       
            Suggestions=resM[x]['suggestions']


            print(Prescription,Suggestions,Potassium,Chloride)
            
            records.append(x+1)
            records.append(Haemoglobin)
            records.append(WBC_count)
            records.append(RBC_count)
            records.append(Platelets_count)

            records.append(Before_meal)
            records.append(After_meal)


            records.append(Glucose)
            records.append(Sodium)
            records.append(Potassium)
            records.append(Chloride)

            records.append(Prescription)
            records.append(Suggestions)


            zipped.append(records)
        print(records)        
        zipped.append(records)
        print(zipped)
        
        
    except:
        res=render(request,'404page.html')
    details={'PatientRegistration':'Patient Prescription','username':name,'type':'patient','records':'2','results':report,'zipped':zipped,'username':name,'age':age,'DOB':dob,'bloodGrp':bloodGroup,}
    return render(request,'patientpresciption.html',details)


def consenteddoctor(request):
    user_detail=get_state_user()
    print(user_detail)
    email = user_detail[0]
    name =user_detail[1]
    typeofuser = user_detail[2]
    doctortinfo=[]
    zipped=[]
    doctorrevokeinfo=[]
    revokezipped=[]

    

    try:
        data={'email':email,}
        url=baseurl+'/Patientconsent/getPatientconsent/' 
        response = requests.post(url, data=data)
        print(response)
        resB=response.json()
        print(resB)

        print(len(resB))
        lengthofresponse=len(resB)
        print(lengthofresponse)

        for x in range(0,lengthofresponse):
            doctortinfo=[]
            print('finished')

            dname=resB[x]['dname']
            dethaddress=resB[x]['dethaddress']
            dhospital=resB[x]['dhospital']
            dtime=resB[x]['dtime']
            rstatus=resB[x]['status1']
            print(x,rstatus)
            Date,Time= dtime.split(" ")
            print(Date,Time)

            if rstatus =="true":
                print('not_revoked')
                doctortinfo.append(dname)
                doctortinfo.append(dethaddress)
                doctortinfo.append(dhospital)
                doctortinfo.append(x+1)
                doctortinfo.append(Date)
                doctortinfo.append(Time)
                zipped.append(doctortinfo)
                

            # print(zipped)
            else:
                print('revoked')

            
                doctorrevokeinfo.append(dname)
                doctorrevokeinfo.append(dethaddress)
                doctorrevokeinfo.append(dhospital)
                doctorrevokeinfo.append(x+1)
                doctorrevokeinfo.append(Date)
                doctorrevokeinfo.append(Time)
                revokezipped.append(doctorrevokeinfo)


    except:
        res=render(request,'404page.html')

    details={'username':'barathraj','type':'patient','username':name,'type':'patient','zipped':zipped,'revokezipped':revokezipped,}
    return render(request,'consenteddoctor.html',details)


# def statisticalreport(request):
#     user_detail=get_state_user()
#     # print('in')
#     print(user_detail)
#     email = user_detail[0]
#     name =user_detail[1]
#     typeofuser = user_detail[2]

#     age =''
#     dob=''

#     lineChart1values = '[20,30,20,30,30,20,50,10,50]'
#     pie1values='[50,50]'
#     pie2values='[100,50]'

#     try:

#         data={'email':email}
#         url=baseurl+'/Patientdetails/getPatient/'
#         response = requests.post(url, data=data)
#         print(response)
#         txt=response.json()
#         print(txt)
#         number = txt['mobileNumber']
#         userethaddress = txt['ethAddress']
#         age=txt['age']
#         dob=txt['dob']
#         bloodGroup=txt['bloodGroup']
#         print(age,dob,bloodGroup)
#         print(number,userethaddress)
#         details={'username':name,'type':'patient','age':age,'DOB':dob,'bloodGrp':bloodGroup,'lineChart1values':lineChart1values,'pie1values':pie1values,'pie2values':pie2values,}

           
#     except:
#         res=render(request,'404page.html')


#     # details={'username':name,'type':'patient','age':age+" - "+dob,'height':height,'BMI':BMI,'bloodGrp':bloodGrp,'weight':weight,'lineChart1values':lineChart1values,}
#     return render(request,'statisticalreport.html',details)



def otpverification(number):
    account_sid = 'ACc39ed28679a00d17fa022c2b5dec689b'
    auth_token = 'ff31459a9dc17b8d80384c5f9a14c837'
    client = Client(account_sid, auth_token)

    verification = client.verify \
                        .services('VA76d3826907bf8bb27095e0e233d4e8c1') \
                        .verifications \
                        .create(to=number, channel='sms')
    print(verification.status)
    return verification.status



def statusverification(statuscode,number):
    print('functionstatus '+statuscode)
    print('number '+number)
    account_sid = 'ACc39ed28679a00d17fa022c2b5dec689b'
    auth_token = 'ff31459a9dc17b8d80384c5f9a14c837'
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
                            .services('VA76d3826907bf8bb27095e0e233d4e8c1') \
                            .verification_checks \
                            .create(to=number, code=statuscode)

    print(verification_check.status)
    return verification_check.status

def patientrecord(request):
    doctor_detail=get_state_doctor()
    docname=doctor_detail[1]
    docEmail=doctor_detail[0]
    docethaddress=doctor_detail[3]
    dochospitalname=doctor_detail[2]
    doctype=doctor_detail[4]

    print(doctor_detail[0])
    print(doctor_detail[1])
    print(doctor_detail[2])
    print(doctor_detail[3])
    print(doctor_detail[4])


    if(request.method =='POST'):
        mailaddress=request.POST.get('mailaddress')
        Username=request.POST.get('patientname')
        request.session['mailaddress'] = mailaddress
        print(mailaddress,Username)

        try:
            print('in')
            data={'email':mailaddress}
            print('done')
            url=baseurl+'/Patientdetails/getPatient/'
            response = requests.post(url, data=data)
            print('finallll')

            print(response)
            txt=response.json()
            print(txt)
            number = txt['mobileNumber']
            puserethaddress = txt['ethAddress']
            pname = txt['name']
            page = txt['age']
            print('out')

            Patient_state_creation(mailaddress,pname,puserethaddress,number)
            patient_detail=get_state_patient()
            patientmail=patient_detail[0]
            patientname=patient_detail[1]
            patientethaddress=patient_detail[2]
            patientnumber=patient_detail[3]
            print(patientmail,patientethaddress,patientname,patientnumber)

            status =otpverification(number)
            print(status)

            

            now = datetime.now()
            ptime = now.strftime("%d/%m/%Y %H:%M:%S")
            print(number,puserethaddress,pname,page,ptime)



           

        #Doctor can see who are they concented
            # #Revoke permission from doctor
            # ind=allpatient.index(userethaddress)
            # print(ind)
            # print("s")
            # web3.eth.defaultAccount=userethaddress
            # revoke=contract.functions.revokeAccessFromDoctor(docethaddress,ind).transact()
            
            # allpatient=contract.functions.getDoctorsPermissions(docethaddress).call()
            # print(allpatient)
       
           
            # request.session['number'] = number
            # print(mailaddress,Username)
            # status =otpverification(number)
            # print(status)


        except:
            res=render(request,'404page.html')
    
    # if approve =='approved'
    details={'doctorname': docname,'doctype':doctype,'status':'fail','Bstatus':'notupdated','statusP':'notupdated',}
    return render(request,'patientrecord.html',details)



def verify(request):
    doctor_detail=get_state_doctor()
    docname=doctor_detail[1]
    docEmail=doctor_detail[0]
    docethaddress=doctor_detail[3]
    dochospitalname=doctor_detail[2]
    doctype=doctor_detail[4]


    patient_detail=get_state_patient()
    patientmail=patient_detail[0]
    patientname=patient_detail[1]
    patientethaddress=patient_detail[2]
    patientnumber=patient_detail[3]
    
    if(request.method =='POST'):
        statuscode = request.POST.get('statuscode')
        print(patientmail)

        try:
            data={'email':patientmail}
            url=baseurl+'/Patientdetails/getPatient/'
            response = requests.post(url, data=data)
            print(response)
            txt=response.json()
            print(txt)
            number = txt['mobileNumber']
            page=txt['age']
            print(number,page)
        
            vstatus = statusverification(statuscode,number)   
            print(vstatus)
            # vstatus="approved"
            if(vstatus == "approved"):
                # trypatientrecorddisplay
                results=[]              
                report=[]
                records=[]
                zipped=[]             
                val=''  

                data={'email':patientmail,}
                url=baseurl+'/Bloodtest/getBloodresult/' 
                responseB = requests.post(url, data=data)
                print(responseB)
                resB=responseB.json()
                print(resB)

                # print(resB[0]['redBloodCells'])
                # print(resB[0]['whiteBloodCells'])
                # print(resB[0]['hemoglobin'])
                # print(resB[0]['platelets'])

                # report['redBloodCells'] = resB[0]['redBloodCells']
                # report['whiteBloodCells']=resB[0]['whiteBloodCells']
                # report['hemoglobin']=resB[0]['hemoglobin']
                # report['platelets']=resB[0]['platelets']

                url=baseurl+'/Sugartest/getSugarresult/' 
                responseS = requests.post(url, data=data)
                print(responseS)
                resS=responseS.json()
                print(resS)

                # print(resS[0]['beforemeal'])
                # print(resS[0]['aftermeal'])

                url=baseurl+'/Cmptest/getCmpresult/' 
                responseC = requests.post(url, data=data)
                print(responseC)
                resC=responseC.json()
                print(resC)

                # print(resC[0]['glucose'])
                # print(resC[0]['sodium'])
                # print(resC[0]['potassium'])
                # print(resC[0]['chloride'])

                url=baseurl+'/Medication/getPrescription/' 
                responseM = requests.post(url, data=data)
                print(responseM)
                resM=responseM.json()
                print(resM)
                # print(report)
                print(len(resM))


                lengthofresponseM=len(resM)
                print(lengthofresponseM)
                now = datetime.now()
                ptime = now.strftime("%d/%m/%Y %H:%M:%S")
                

                if (len(resB) and len(resC) and len(resM) and len(resS) and len(resM)) != 0:
                    if (lengthofresponseM !=0):
                        val=0
                        print('the val is 0')

                    
                    else:
                        val=1
                        print('the val is 1')

                    for x in range(0,lengthofresponseM+val):
                        records=[]
                        print('finished')
                        print(x)

                        Haemoglobin=resB[x]['hemoglobin']
                        WBC_count=resB[x]['whiteBloodCells']
                        RBC_count=resB[x]['redBloodCells']
                        Platelets_count=resB[x]['platelets']
                        print('in1')
                        Before_meal=resS[x]['beforemeal']
                        After_meal=resS[x]['aftermeal']
                        print('in2')

                        Glucose=resC[x]['glucose']
                        Sodium=resC[x]['sodium']
                        Potassium=resC[x]['potassium']
                        Chloride=resC[x]['chloride']
                        print('in3')
                        
                        Prescription=resM[x]['prescription']       
                        Suggestions=resM[x]['suggestions']
                        print('in4')

                        # print(Prescription,Suggestions,Potassium,Chloride)
                        
                        records.append(x+1)
                        records.append(Haemoglobin)
                        records.append(WBC_count)
                        records.append(RBC_count)
                        records.append(Platelets_count)

                        records.append(Before_meal)
                        records.append(After_meal)


                        records.append(Glucose)
                        records.append(Sodium)
                        records.append(Potassium)
                        records.append(Chloride)

                        records.append(Prescription)
                        records.append(Suggestions)


                        zipped.append(records)
                        print('done')

                    print(records)        
                    # zipped.append(records)
                    print(zipped)
                    # recordszip='sb'



                    
                    
                    #   Give permission to doctor
                    print("in")
                    web3.eth.defaultAccount=patientethaddress
                    print("out")
                    print(docethaddress)
                    contract.functions.giveAccessToDoctor(docethaddress).transact()
                    print("inout")

                    # web3.eth.defaultAccount=docethaddress
                    # allpatient=contract.functions.getDoctorsPermissions(docethaddress).call()
                    # print(allpatient)

                    

                    data={'email':docEmail,'pname':patientname,'page':page,'pethaddress':patientethaddress,'ptime':ptime}
                    url=baseurl+'/Doctorconsent/doctorconsent/'
                    response = requests.post(url, data=data)
                    print(response)
                    txt=response.json()
                    print(txt)



                    data={'email':patientmail,'dname':docname,'dhospital':dochospitalname,'dethaddress':docethaddress,'dtime':ptime,'status1':"true",}
                    url=baseurl+'/Patientconsent/patientconsent/'
                    response = requests.post(url, data=data)
                    print(response)
                    txt=response.json()
                    print(txt)
                    
                    emailit(patientmail,docname,ptime)

                    details={'doctorname':docname,'status':'approved','Bstatus':'notupdated','doctorname': docname,'doctype':doctype,'recordszip':zipped,'statusP':'updatedP',}

                else:
                    print('newuser so no prescriptions')

                    print("in")
                    web3.eth.defaultAccount=patientethaddress
                    print("out")
                    print(docethaddress)
                    contract.functions.giveAccessToDoctor(docethaddress).transact()
                    print("inout")

                    # web3.eth.defaultAccount=docethaddress
                    # allpatient=contract.functions.getDoctorsPermissions(docethaddress).call()
                    # print(allpatient)

                    

                    data={'email':docEmail,'pname':patientname,'page':page,'pethaddress':patientethaddress,'ptime':ptime}
                    url=baseurl+'/Doctorconsent/doctorconsent/'
                    response = requests.post(url, data=data)
                    print(response)
                    txt=response.json()
                    print(txt)



                    data={'email':patientmail,'dname':docname,'dhospital':dochospitalname,'dethaddress':docethaddress,'dtime':ptime,'status1':"true",}
                    url=baseurl+'/Patientconsent/patientconsent/'
                    response = requests.post(url, data=data)
                    print(response)
                    txt=response.json()
                    print(txt)
                    
                    emailit(patientmail,docname,ptime)


                    details={'doctorname':docname,'status':'approved','Bstatus':'notupdated','doctorname': docname,'doctype':doctype,'statusP':'notupdatedP'}

            else:
                details={'doctorname':docname,'status':'failed','Bstatus':'notupdated','doctorname': docname,'doctype':doctype,'statusP':'failed'}
        except:
            res=render(request,'404page.html')
    return render(request,'patientrecord.html',details)



def registeredpatientinfo(request):
    doctor_detail=get_state_doctor()
    docname=doctor_detail[1]
    docEmail=doctor_detail[0]
    docethaddress=doctor_detail[3]
    dochospitalname=doctor_detail[2]
    doctype=doctor_detail[4]
    patientinfo=[]
    zipped=[]


    try:
        data={'email':docEmail}
        url=baseurl+'/Doctorconsent/getDoctorconsent/'
        response = requests.post(url, data=data)
        print(response)
        txt=response.json()
        print(txt,len(txt))
        if(len(txt)):
            print('yes')
            print(len(txt))
            lengthofresponse=len(txt)
            print(lengthofresponse)
            for x in range(0,lengthofresponse):
                patientinfo=[]
                print('finished')
                pname=txt[x]['pname']
                pethaddress=txt[x]['pethaddress']
                page=txt[x]['page']
                ptime=txt[x]['ptime']

                patientinfo.append(pname)
                patientinfo.append(page)
                patientinfo.append(pethaddress)
                patientinfo.append(ptime)
                patientinfo.append(x+1)

                zipped.append(patientinfo)

                print(pname,pethaddress,page,ptime)
                print(patientinfo)
                print(zipped)

            details={'doctorname':docname,'doctype':doctype,'zipped':zipped,'patientinfo':patientinfo,'pname':pname,'pethaddress':pethaddress,'page':page,'ptime':ptime,}

        else:
            details={'doctorname':docname,'doctype':doctype}
    except:
        res=render(request,'404page.html')
    return render(request,'registeredpatientinfo.html',details)


# def tables(request):
#     return render(request,'tables.html')

def home(request):
    return render(request,'index.html')

def doctorhompage(request):
    doctor_detail=get_state_doctor()
    docname=doctor_detail[1]
    docEmail=doctor_detail[0]
    # docethaddress=doctor_detail[3]
    # dochospitalname=doctor_detail[2]
    doctype=doctor_detail[4]
    details={'doctorname':docname,'doctype':doctype,}
    return render(request,'doctorhompage.html',details)
    



def createaccountpatient(request):
    details={'urlmap':'/createaccountU/',}
    print('accountcreated')
    return render(request,'createaccount.html',details)

def createaccountU(request):
    if(request.method=='POST'):
        Uname=request.POST.get('Uname')
        email=request.POST.get('email')
        password=request.POST.get('password')

        print(Uname,email,password)
        User_state_creation(email,Uname,'patient')
    
        try:
            data={'firstName':Uname,'email':email,'password':password,}
            url=baseurl+'/User/CreatePatient/'
            response = requests.post(url, data=data)
            print(response)
            txt=response.json()
            print(txt)

            if(txt["message"] == "User Created"):
                print("Created and logedin")
                res=redirect('/patienthomepage/')

            elif (res["messaage"] =="User already exist"):
                print("user already exist")
                res=redirect('/404/')
            else:
                res=redirect('/404/')  
        except:
            res=render(request,'404page.html')
    return res

def doctoraccount(request):
    details={'urlmap':'/createaccountD/',}
    print('accountcreatedDoctor')
    return render(request,'doctoraccount.html',details)

def createaccountD(request):
    if(request.method=='POST'):
        doctorethAddress=request.POST.get('dethereumaddress')
        doctorName=request.POST.get('Uname')
        hospitalName=request.POST.get('hospitalName')
        docEmail=request.POST.get('email')
        password=request.POST.get('password')
        doctor_state_creation(docEmail,doctorName,hospitalName,doctorethAddress,'Doctor')
        print(doctorName)

        print(doctorethAddress,doctorName,hospitalName,docEmail,password) 
    
        try:
            data={'doctorethAddress':doctorethAddress,'doctorName':doctorName,'hospitalName':hospitalName,'docEmail':docEmail,'password':password,}
            url=baseurl+'/Doctor/doctorRegistration/'
            response = requests.post(url, data=data)
            print(response) 
            res=response.json()
            print(res)
            if(res["message"] == "Doctor Created"):
                print('Doc created')
                res=redirect('/patientrecord/')
            else:
                res=redirect('/404/')  
        except:
            res=render(request,'404page.html')
    
    return res




def labprescription(request):
    # print(user_detail)
    # print(get_state_user[0])
    # email = user_detail[0]
    # name =user_detail[1]
    # typeofuser = user_detail[2]

    doctor_detail=get_state_doctor()
    docname=doctor_detail[1]
    docEmail=doctor_detail[0]
    docethaddress=doctor_detail[3]
    dochospitalname=doctor_detail[2]
    doctype=doctor_detail[4]


    patient_detail=get_state_patient()
    patientmail=patient_detail[0]
    patientname=patient_detail[1]
    patientethaddress=patient_detail[2]
    patientnumber=patient_detail[3]
    print(patientmail,patientethaddress,patientname,patientnumber)

    if(request.method=='POST'):
        haemoglobin=request.POST.get('haemo')
        WBCcount=request.POST.get('WBC')
        RBCcount=request.POST.get('RBC')
        Plateletscount=request.POST.get('Platelets')
        Beforemeal=request.POST.get('Beforemeal')
        aftermeal=request.POST.get('aftermeal')
        Glucose=request.POST.get('Glucose')
        Sodium=request.POST.get('Sodium')
        Potassium=request.POST.get('Potassium')
        Chloride=request.POST.get('Chloride')
 
        print(haemoglobin,WBCcount,RBCcount,Plateletscount)
        print(Beforemeal,aftermeal)
        print(Glucose,Sodium,Potassium,Chloride)

        try:
            print('start')
            dataB={'email':patientmail,'redBloodCells':RBCcount,'whiteBloodCells':WBCcount,'hemoglobin':haemoglobin,'platelets':Plateletscount,}
            url=baseurl+'/Bloodtest/bloodtest'
            response = requests.post(url, data=dataB)
            print(response)
            res=response.json()
            print(res)

            if(res["message"] == "Bloodresult Updated"):
                print('Bloodtest updated')
            dataS={'email':patientmail,'beforemeal':Beforemeal,'aftermeal':aftermeal,}
            url=baseurl+'/Sugartest/sugartest'
            responseS = requests.post(url, data=dataS)
            print(responseS)
            resS=responseS.json()
            print(resS)
            if(resS["message"] == "Sugar result Updated"):
                print('Sugar result Updated')
            

            dataC={'email':patientmail,'glucose':Glucose,'sodium':Sodium,'potassium':Potassium,'chloride':Chloride,}
            url=baseurl+'/Cmptest/cmptest'
            responseC = requests.post(url, data=dataC)
            print(responseC)
            resC=responseC.json()
            print(resC)

            if(resC["message"] == "CMP result Updated"):
                print('CMP result Updated')

            else:
                res=redirect('/404/')  

        except:
            res=render(request,'404page.html')
    details={'doctorname':docname,'status':'approved','Bstatus':'notupdated','doctype':doctype,'statusP':'updatedP',}
    return render(request,'patientrecord.html',details)



def Medications(request):
    doctor_detail=get_state_doctor()
    docname=doctor_detail[1]
    docEmail=doctor_detail[0]
    docethaddress=doctor_detail[3]
    dochospitalname=doctor_detail[2]

    doctype=doctor_detail[4]
    patient_detail=get_state_patient()
    patientmail=patient_detail[0]
    patientname=patient_detail[1]
    patientethaddress=patient_detail[2]
    patientnumber=patient_detail[3]
    print(patientmail,patientethaddress,patientname,patientnumber)


    if(request.method=='POST'):
        Prescription=request.POST.get('Prescription')
        Suggestions=request.POST.get('Suggestions')
        print(Prescription)
        print(Suggestions)


        try:
            data={'email':patientmail,'prescription':Prescription,'suggestions':Suggestions,}
            url=baseurl+'/Medication/prescription'
            response = requests.post(url, data=data)
            print(response)
            res=response.json()
            print(res)
            if(res["message"] == "Bloodresult Updated"):
                print('Bloodtest updated')
            else:
                res=redirect('/404/')

            details={'doctorname':docname,'status':'approved','Bstatus':'notupdated','doctype':doctype,'statusP':'updatedP',}  
            
        except:
            res=render(request,'404page.html')

    return render(request,'patientrecord.html')




        