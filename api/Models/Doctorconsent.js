//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);
const doctorconsentSchema = mongoose.Schema({
    email:{
        type:String,
        
        // unique:true
    },
    	pname:{
        type:String,
        
    },
    page:{
        type:String,
        
    },
    pethaddress:{
        type:String,
       
    },
    ptime:{
        type:String,
       
    }     
    
    

});

module.exports = mongoose.model("Doctorconsent", doctorconsentSchema);