//jshint esversion:6
const express = require('express');
const Doctortconsent = require('../Models/Doctorconsent');
const doctorconsentRouter = express.Router();


doctorconsentRouter.post('/doctorconsent', async (req,res) =>{
    var email=req.body.email;
    var pname=req.body.pname;
    var pethaddress=req.body.pethaddress;
    var page=req.body.page;
    var ptime=req.body.ptime;
    
    try{
  
        const doctorconsent =new Doctortconsent({
            email:email,
            pname:pname,
            pethaddress:pethaddress,
            page:page,
            ptime:ptime,
          
        });
        await doctorconsent.save();
        res.status(200).send({"message":"Doctor consent updated"});

}
    catch(err)
    {
        res.status(500).json({message:err});
    }
});


// doctorconsentRouter.post('/getDoctorconsent', async (req,res) =>
// {
//     var email=req.body.email;
    

//     try{
//         const doctorconsent = await Doctorconsent.find({email:email});
//         if(doctorconsent)
//         {
//         res.status(200).send(doctorconsent);
//         }
//         else{
//             res.status(200).send("Doesn't Exists");
//         }
            
//     }
//     catch(err)
//     {
//         res.status(500).json({message:err});
//     }


// });
doctorconsentRouter.post('/getDoctorconsent', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const doctorconsent = await Doctortconsent.find({email:email});
        if(doctorconsent)
        {
        res.status(200).send(doctorconsent);
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

module.exports = doctorconsentRouter;