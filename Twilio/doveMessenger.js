var accountSid = 'AC61513f71d9b075c17402312ac4327e3f'; // Your Account SID from www.twilio.com/console
var authToken = '808fdce0ed22fded7448465ab9ee4399';   // Your Auth Token from www.twilio.com/console

var twilio = require('twilio');
var client = new twilio(accountSid, authToken);

client.messages.create({
    body: 'wydwya',
    to: '+19519567927',  // Text this number
    from: '+19514206701' // From a valid Twilio number
})
// .then(function(message) {
//     console.log(message.sid);
// });
// .then( message => {
//     console.log(message.sid);
// });

// .then(message => console.log(message.sid));
.then(function(message) { return console.log(message.sid); });