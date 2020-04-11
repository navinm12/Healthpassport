//jshint esversion:6

const express = require('express');
const User = require('../Models/User');
const userRouter = express.Router();
const bcrypt = require('bcrypt');
const saltRounds = 5;



userRouter.post('/CreatePatient', async (req,res) => {
    var firstName = req.body.firstName;
    var email = req.body.email;
    var ethAddress=req.body.ethAddress;``
    var password = bcrypt.hashSync(req.body.password, saltRounds);
    try{
        const userByemail = await User.findOne({email:email});
        if(userByemail){res.status(200).send({"message":"User already exist"});}
        // else{
        //     const userByAddress=await User.findOne({ethAddress:ethAddress});
        // if(userByAddress){res.status(200).send({"message":"User already exist"})}
        else {
            const user = new User({
                firstName:firstName,
                email:email,
                password:password
            });
            await user.save();
            res.status(200).send({"message":"User Created"});
        }
    // } 
}   catch (err) {
        res.status(400).send("error-occured");
    }
});



userRouter.post('/PatientAuthetication',async (req,res) => {
    var email =req.body.email;
    var password=req.body.password;
    try{
        const user = await User.findOne({email:email});
        if(user)
        {
            if(bcrypt.compareSync(password,user.password)){
                res.status(200).send({"message":"Login Successful",user})
            }
            else{
                res.status(400).send({"message":"User not found"})
            }
        }
    }
    catch(err)
    {
        res.status(500).json({message:err})
    }
});




module.exports = userRouter;