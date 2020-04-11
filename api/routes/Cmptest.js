//jshint esversion:6
const express = require('express');
const Cmptest = require('../Models/Cmptest');
const cmptestRouter = express.Router();

cmptestRouter.post('/cmptest', async (req,res) =>{
    var email=req.body.email;
    var glucose=req.body.glucose;
    var sodium=req.body.sodium;
    var potassium=req.body.potassium;
    var chloride=req.body.chloride;

    try{
        const cmptest =new Cmptest({
            email:email,
            glucose:glucose,
            sodium :sodium,
            potassium :potassium,
            chloride:chloride,
        });
        await cmptest.save();
        res.status(200).send({"message":"CMP result Updated"});
    }

    catch(err)
    {
        res.status(500).json({message:err});
    }
    
});

cmptestRouter.post('/getCmpresult', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const cmpresult = await Cmptest.find({email:email});
        if(cmpresult)
        {
        res.status(200).send(cmpresult);
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
module.exports = cmptestRouter;
