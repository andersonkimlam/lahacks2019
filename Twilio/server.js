const http = require('http');
const express = require('express');
const MessagingResponse = require('twilio').twiml.MessagingResponse;

const app = express();

app.post('/sms', (req, res) => {
    const twiml = new MessagingResponse();

    twiml.message('The robots are coming! The robots are coming!');
    console.log(req);
    res.writeHead(200, {'Content-Type': 'text/xml'});
    res.end(twiml.toString());
});
/*
{ ToCountry: 'US',
  ToState: 'CA',
  SmsMessageSid: 'SMa6aa2b0b15ebeb1157289c4706c8cb44',
  NumMedia: '0',
  ToCity: '',
  FromZip: '92121',
  SmsSid: 'SMa6aa2b0b15ebeb1157289c4706c8cb44',
  FromState: 'CA',
  SmsStatus: 'received',
  FromCity: 'SAN DIEGO',
  Body: 'Hggh',
  FromCountry: 'US',
  To: '+19514206701',
  ToZip: '',
  NumSegments: '1',
  MessageSid: 'SMa6aa2b0b15ebeb1157289c4706c8cb44',
  AccountSid: 'AC61513f71d9b075c17402312ac4327e3f',
  From: '+16197215277',
  ApiVersion: '2010-04-01' }
*/
http.createServer(app).listen(1337, () => {
   console.log('Express server listening on port 1337'); 
});
