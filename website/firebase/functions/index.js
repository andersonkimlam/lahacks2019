/**
 * Copyright 2017 Google Inc. All Rights Reserved.
 * ...
 */

// Import the Firebase SDK for Google Cloud Functions.
const functions = require('firebase-functions');
// Import and initialize the Firebase Admin SDK.
const admin = require('firebase-admin');
admin.initializeApp();

const spawn = require('child_process').spawn;
const ls = spawn('python', ['findStockChanges.py']);
ls.stdout.on('data', (data) => {
  res.sendData
});
ls.on('exit', code => {
  console.log(`Exit code is: ${code}`);
});
