//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);
const medicationsSchema = mongoose.Schema({
    email:{
        type:String,
        
    },
    prescription:{
        type:String,
        
    },
    suggestions	:{
        type:String,
       
    },
   
    
    

});

module.exports = mongoose.model("Medications", medicationsSchema);