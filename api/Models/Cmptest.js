//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);
const cmptestSchema = mongoose.Schema({
    email:{
        type:String,
        
        // unique:true
    },
    	glucose:{
        type:String,
        
    },
    sodium:{
        type:String,
        
    },
    potassium:{
        type:String,
       
    },
    chloride:{
        type:String,
       
    }
    
    
    

});

module.exports = mongoose.model("Cmptest", cmptestSchema);