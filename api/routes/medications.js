//jshint esversion:6
const express = require('express');
const Medication = require('../Models/medications');
const medicationRouter = express.Router();

medicationRouter.post('/prescription', async (req,res) =>{
    var email=req.body.email;
    var prescription=req.body.prescription;
    var suggestions=req.body.suggestions;


    try{
  
        const medication =new Medication({
            email:email,
            prescription:prescription,
            suggestions :suggestions,
          
        });
        await medication.save();
        res.status(200).send({"message":"Medication Updated"});

}
    catch(err)
    {
        res.status(500).json({message:err});
    }



});


medicationRouter.post('/getPrescription', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const medicationresult = await Medication.find({email:email});
        if(medicationresult)
        {
        res.status(200).send(medicationresult);
        }
        else{
            res.status(200).send("Doesn't Exists");
        }
            
            
        
    }
    catch(err)
    {
        res.status(500).json({message:err});
    }


});





module.exports = medicationRouter;