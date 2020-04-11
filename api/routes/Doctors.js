//jshint esversion:6
const express = require('express');
const Doctor = require('../Models/Doctors');
const doctorRouter = express.Router();
const bcrypt = require('bcrypt');
const saltRounds = 5;


doctorRouter.post('/doctorRegistration', async (req,res) =>{
    var doctorName=req.body.doctorName;
    var doctorethAddress = req.body.doctorethAddress;
    var hospitalName = req.body.hospitalName;
    var docEmail = req.body.docEmail;
    var password = bcrypt.hashSync(req.body.password, saltRounds);

    try{
        const doctorByemail = await Doctor.findOne({docEmail:docEmail});
        if(doctorByemail){res.status(200).send({"message":"Doctor already exist"});}
        else {
            
            const doctor = new Doctor ({
                doctorName:doctorName,
                doctorethAddress:doctorethAddress,
                hospitalName:hospitalName,
                docEmail:docEmail,
                password:password
            });
            await doctor.save();
            res.status(200).send({"message":"Doctor Created"});
        }
    } 
   catch (error) {
        res.status(400).send("error-occured");
    }
});


doctorRouter.post('/doctorAuthetication',async (req,res) => {
    var docEmail =req.body.docEmail;
    var password=req.body.password;
    try{
        const doctor = await Doctor.findOne({docEmail:docEmail});
        if(doctor)
        {
            if(bcrypt.compareSync(password,doctor.password)){
                res.status(200).send({"message":"Login successful",doctor})
            }
            else{
                res.status(400).send({"message":"Doctor Not Found"})
            }
        }
        else
        {
            res.status(404).send({"message":"Invalid Crediential"})
        }
    }
    catch(err)
    {
        res.status(500).json({message:err})
    }
});

module.exports =doctorRouter;