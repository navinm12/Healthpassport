//jshint esversion:6
const express = require('express');
const Patientconsent = require('../Models/Patientconsent');
const patientconsentRouter = express.Router();

patientconsentRouter.post('/patientconsent', async (req,res) =>{
    var email=req.body.email;
    var dname=req.body.dname;
    var dethaddress=req.body.dethaddress;
    var dhospital=req.body.dhospital;
    var dtime=req.body.dtime;
    var status1=req.body.status1;
    
    try{
  
        const patientconsent =new Patientconsent({
            email:email,
            dname:dname,
            dethaddress:dethaddress,
            dhospital:dhospital,
            dtime:dtime,
            status1:status1
          
        });
        await patientconsent.save();
        res.status(200).send({"message":"Patient consent updated"});

}
    catch(err)
    {
        res.status(500).json({message:err});
    }

});


patientconsentRouter.post('/statusupdate', async (req,res) =>{

    // var email=req.body.email;
    var dtime=req.body.dtime;
   
    try{
        console.log("1");
        const stausbymail = await Patientconsent.findOne({dtime:dtime});
        console.log(stausbymail);
        console.log(stausbymail.dtime);
        console.log(dtime);
        const mail1=stausbymail.dtime;
        const mail2=dtime;

        const num=mail1.localeCompare(mail2);
        console.log("hello");

        console.log(num);
        if(num==0)
        {
            console.log("1");
                console.log("1");
                const change=await Patientconsent.updateOne({dtime:stausbymail.dtime},{$set:{status1:"false"}});
                console.log("1");
                res.status(200).send(stausbymail);
}

    }

catch(err)
    {
        res.status(500).json({message:err});
    }});


patientconsentRouter.post('/getPatientconsent', async (req,res) =>
{
    var email=req.body.email;
    

    try{
        const patientconsent = await Patientconsent.find({email:email});
        if(patientconsent)
        {
        res.status(200).send(patientconsent);
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



module.exports = patientconsentRouter;