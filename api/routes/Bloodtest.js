//jshint esversion:6
const express = require('express');
const Bloodtest = require('../Models/Bloodtest');
const bloodtestRouter = express.Router();

bloodtestRouter.post('/bloodtest', async (req,res) =>{
    var email=req.body.email;
    var redBloodCells=req.body.redBloodCells;
    var whiteBloodCells=req.body.whiteBloodCells;
    var hemoglobin=req.body.hemoglobin;
    var platelets=req.body.platelets;


    try{
    
        const bloodtest =new Bloodtest({
            email:email,
            redBloodCells:redBloodCells,
            whiteBloodCells :whiteBloodCells,
            hemoglobin :hemoglobin,
            platelets:platelets,
        });
        await bloodtest.save();
        res.status(200).send({"message":"Bloodresult Updated"});
        
}

    catch(err)
    {
        res.status(500).json({message:err});
    }
});


bloodtestRouter.post('/getBloodresult', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const bloodresult = await Bloodtest.find({email:email});
        if(bloodresult)
        {
        res.status(200).send(bloodresult);
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





module.exports = bloodtestRouter;