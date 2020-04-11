//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);
const medicalshopSchema = mongoose.Schema({
    email:{
        type:String,
        
    },
    prescription:{
        type:String,
        
    },
    
    

});

module.exports = mongoose.model("Medicalshop", medicalshopSchema);