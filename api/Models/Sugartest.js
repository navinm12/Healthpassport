//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);
const sugartestSchema = mongoose.Schema({
    email:{
        type:String,
        required:true,
        // unique:true
    },
    	beforemeal:{
        type:String,
        required:true
    },
    aftermeal:{
        type:String,
        required:true
    },
    
    
    

});

module.exports = mongoose.model("Sugartest", sugartestSchema);