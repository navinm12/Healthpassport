//jshint esversion:6
const express = require('express');
const Sugartest = require('../Models/Sugartest');
const sugartestRouter = express.Router();

sugartestRouter.post('/sugartest', async (req,res) =>{
    var email=req.body.email;
    var beforemeal=req.body.beforemeal;
    var aftermeal=req.body.aftermeal;
    
    try{
  
        const sugartest =new Sugartest({
            email:email,
            beforemeal:beforemeal,
            aftermeal :aftermeal,
          
        });
        await sugartest.save();
        res.status(200).send({"message":"Sugar result Updated"});

}
    catch(err)
    {
        res.status(500).json({message:err});
    }
});


sugartestRouter.post('/getSugarresult', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const sugarresult = await Sugartest.find({email:email});
        if(sugarresult)
        {
        res.status(200).send(sugarresult);
        }
        else{
            res.status(200).send("Doesn't Exists");
        }
            
            
        
    }
    catch(err)
    {
        res.status(500).json({message:err})
    }


});





module.exports = sugartestRouter;