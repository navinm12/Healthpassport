//jshint esversion:6
const express = require('express');
const Medicallogin = require('../Models/medicallogin');
const medicalloginRouter = express.Router();
const bcrypt = require('bcrypt');
const saltRounds = 5;


medicalloginRouter.post('/medicalregister', async (req,res) =>{
    var shopname=req.body.shopname;
    var ownername = req.body.ownername;
    var email = req.body.email;
    var password = bcrypt.hashSync(req.body.password, saltRounds);

    try{
        console.log("1");
        const medicalByemail = await Medicallogin.findOne({email:email});
        if(medicalByemail){res.status(200).send({"message":"Medicalshop already exist"});}
        else {
            console.log("1");
            
            const medicallogin = new Medicallogin ({
                shopname:shopname,
                ownername:ownername,
                email:email,
                password:password
            });
            await medicallogin.save();
            res.status(200).send({"message":"Medical login Created"});
        }
    } 
   catch (error) {
        res.status(400).send("error-occured");
    }
});



medicalloginRouter.post('/medicalAuthetication',async (req,res) => {
    var email =req.body.email;
    var password=req.body.password;
    try{
        const medical = await Medicallogin.findOne({email:email});
        if(medical)
        {
            console.log("2");
            if(bcrypt.compareSync(password,medical.password)){
                console.log("2");
                res.status(200).send({"message":"Login successful",medical})
            }
            else{
                res.status(400).send({"message":"shop Not Found"})
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

module.exports =medicalloginRouter;