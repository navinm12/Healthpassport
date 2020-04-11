//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);
const bloodtestSchema = mongoose.Schema({
    email:{
        type:String,
        
    },
    redBloodCells	:{
        type:String,
        
    },
    whiteBloodCells	:{
        type:String,
       
    },
    hemoglobin:{
        type:String,
        
    },
    platelets:{
        type:String,
        
    }
    
    

});

module.exports = mongoose.model("Bloodtest", bloodtestSchema);