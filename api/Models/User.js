//jshint esversion:6

const mongoose = require('mongoose');
mongoose.set('useCreateIndex', true);


const userSchema = mongoose.Schema({

    firstName:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true
    },
    
    password:{
        type:String,
        required:true
    }
    

    

});

module.exports = mongoose.model("Users", userSchema);