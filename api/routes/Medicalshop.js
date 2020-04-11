//jshint esversion:6
const express = require('express');
const Medicalshop = require('../Models/Medicalshop');
const medicalshopRouter = express.Router();

medicalshopRouter.post('/medicalprescription', async (req,res) =>{
    var email=req.body.email;
    var prescription=req.body.prescription;

    try{
  
        const medicalshop =new Medicalshop({
            email:email,
            prescription:prescription,
           
          
        });
        await medicalshop.save();
        res.status(200).send({"message":"updated the details"});

}
    catch(err)
    {
        res.status(500).json({message:err});
    }



});


medicalshopRouter.post('/getmedicalprescription', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const medicalresult = await Medicalshop.find({email:email});
        if(medicalresult)
        {
        res.status(200).send(medicalresult);
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


module.exports = medicalshopRouter;