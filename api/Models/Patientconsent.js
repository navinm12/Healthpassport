//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);
const patientconsentSchema = mongoose.Schema({
    email:{
        type:String,
        
        // unique:true
    },
    	dname:{
        type:String,
        
    },
    dethaddress:{
        type:String,
        
    },
    dhospital:{
        type:String,
       
    } ,
    dtime:{
        type:String,
       
    },

    status1:
    {
        type:String,
    }

    
    

});

module.exports = mongoose.model("Patientconsent", patientconsentSchema);