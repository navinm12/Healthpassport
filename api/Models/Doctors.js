//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);

const doctorSchema = mongoose.Schema({
    doctorethAddress:{
        type:String,
        
    },
    doctorName:{
        type:String,
        
    },
    hospitalName:{
        type:String,
        
    },
    docEmail:{
        type:String,
        
    },
    password:{
        type:String,
        
    }
    
    

});

module.exports = mongoose.model("Doctors", doctorSchema);