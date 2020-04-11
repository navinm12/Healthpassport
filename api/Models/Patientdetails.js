//jshint esversion:6
const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);

const patientdetailsSchema = mongoose.Schema({
    email:{
        type:String,
        required:true,
        unique:true
    },
    ethAddress:{
        type:String,
        required:true
    },
    
    name:{
        type:String,
        required:true
    },
    
    age:{
        type:String,
        required:true
        
    },
    gender:{
        type:String,
        required:true
    },
    dob:{
        type:String,
        required:true
    },
    mobileNumber:{
        type:String,
        required:true
    },
    fatherName:{
        type:String,
        required:true
    },
    address:{
        type:String,
        required:true
    },
    bloodGroup:{
        type:String,
        required:true
    }

});

module.exports = mongoose.model("Patientdetails", patientdetailsSchema);