//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);

const medicalloginSchema = mongoose.Schema({
    shopname:{
        type:String,
        
    },
    ownername:{
        type:String,
        
    },
    email:{
        type:String,
        
    },
    password:{
        type:String,
        
    }
    
    

});

module.exports = mongoose.model("Medicallogin", medicalloginSchema);