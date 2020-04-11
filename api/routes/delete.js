//jshint esversion:6
const express = require('express');
const Bloodtest = require('../Models/Bloodtest');
const Sugartest = require('../Models/Sugartest');
const Cmptest = require('../Models/Cmptest');
const Patientdetails = require('../Models/Patientdetails');
const Medications = require('../Models/medications');
const User = require('../Models/User');
const Patientconsent = require('../Models/Patientconsent');



const deletepatientRouter = express.Router();

deletepatientRouter.post('/patientdelete', async (req,res) =>
{
    var email=req.body.email;
    console.log("1");
    try{
        console.log("1");
        const blood = await Bloodtest.deleteMany({email:email});
        console.log("1");
        const cmp = await Cmptest.deleteMany({email:email});
        const medication = await Medications.deleteMany({email:email});
        console.log("1");
        const patient = await Patientdetails.findOneAndDelete({email:email});
        const sugar = await Sugartest.findOneAndDelete({email:email});
        const user = await User.findOneAndDelete({email:email});
        console.log("1");
        const patientconsent = await Patientconsent.deleteMany({email:email});


        console.log("1");
        if(blood,patient,cmp,medication,sugar,user,patientconsent)
        {
            console.log("7");
            res.status(200).send({"message":"Deleted successfull"});
        }
        else{
            res.status(404).send("Patient does not exist");
        }
            
            
        
    }
    catch(err)
    {
        res.status(500).json({message:err});
    }


});


module.exports = deletepatientRouter;