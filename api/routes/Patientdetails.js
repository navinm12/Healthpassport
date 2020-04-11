//jshint esversion:6
const express = require('express');
const Patientdetails = require('../Models/Patientdetails');
const patientdetailsRouter = express.Router();


patientdetailsRouter.post('/patientRegistration', async (req,res) =>{
    var email=req.body.email;
    var name=req.body.name;
    var age=req.body.age;
    var gender=req.body.gender;
    var dob=req.body.dob;
    var mobileNumber=req.body.mobileNumber;
    var fatherName=req.body.fatherName;
    var address=req.body.address;
    var bloodGroup=req.body.bloodGroup;
    var ethAddress=req.body.ethAddress;


    try{
        const patientdetails =new Patientdetails({
            email:email,
            name:name,
            age :age,
            gender :gender,
            dob:dob,
            mobileNumber:mobileNumber,
            fatherName:fatherName,
            address:address,
            bloodGroup:bloodGroup,
            ethAddress:ethAddress
        });
        await patientdetails.save();
        res.status(200).send({"message":"Registration completed"});
    }
    catch (err) {
            res.status(400).send({"message":"error-occured"});
        }
});





patientdetailsRouter.post('/getPatient', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const patient = await Patientdetails.findOne({email:email});
        if(patient)
        {
        res.status(200).send(patient);
        }
        else{
            res.status(200).send("patient not exist");
        }
            
            
        
    }
    catch(err)
    {
        res.status(500).json({message:err})
    }


});






module.exports = patientdetailsRouter;