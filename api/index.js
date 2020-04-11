//jshint esversion:6
const express = require('express');
const mongoose = require('mongoose');
const app = express();
const userRouter = require('./routes/User');
const doctorRouter = require('./routes/Doctors');
const patientdetailsRouter = require('./routes/Patientdetails');
const bloodtestRouter = require('./routes/Bloodtest');
const sugartestRouter = require('./routes/Sugartest');
const cmptestRouter = require('./routes/Cmptest');
const medicationRouter = require('./routes/medications');
const patientconsentRouter = require('./routes/Patientconsent');
const doctorconsentRouter = require('./routes/Doctorconsent');
const medicalshopRouter = require('./routes/Medicalshop');
const medicalloginRouter = require('./routes/medicallogin');
const deletepatientRouter = require('./routes/delete');


const port = process.env.port || 8080;
const ConnectionString = "mongodb+srv://navin:navin@cluster0-eo210.mongodb.net/test?retryWrites=true&w=majority";

app.use(express.urlencoded({extended:true}));
app.use(express.json());


app.use('/api/User', userRouter);
app.use('/api/Doctor', doctorRouter);
app.use('/api/Patientdetails', patientdetailsRouter);
app.use('/api/Bloodtest', bloodtestRouter);
app.use('/api/Sugartest', sugartestRouter);
app.use('/api/Cmptest', cmptestRouter);
app.use('/api/Medication', medicationRouter);
app.use('/api/Patientconsent', patientconsentRouter);
app.use('/api/Doctorconsent', doctorconsentRouter);
app.use('/api/medicalshop', medicalshopRouter);
app.use('/api/medicallogin', medicalloginRouter);

app.use('/api/deleteone', deletepatientRouter);




mongoose.connect(ConnectionString,{useUnifiedTopology:true,useNewUrlParser:true}, () => { console.log("mongo db connected");});

app.listen(port, () => { console.log("App listening to the port: "+port); });