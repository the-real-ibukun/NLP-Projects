/**
var http = require("http");

http.createServer(function (request, response) {
   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});
   
   // Send the response body as "Hello World"
   response.end('Hello World\n');
}).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');
 */

twitterKey = 'KSCKqJdfHfIQR4MWkObCXtgWL';
twitterSecret = 'fs2x0uS3Av3fRlKjsgrZSTxx8tLSCEVTYEasiGLclCuGTKPawG';
token = '1210057938-EOSbP3tfYxeUKAxbB6oHhfB7c7axs9BbeL5HO1b';
secret = 'hvUwOqugyft0TpOznuxBWZ2ZBAfKwwmo32AUfOEi0t3pg';


var OAuth = require('OAuth');
var oauth = new OAuth.OAuth(
  'https://api.twitter.com/oauth/request_token',
  'https://api.twitter.com/oauth/access_token',
  twitterKey,
  twitterSecret,
  '1.0A',
  null,
  'HMAC-SHA1'
);

oauth.get(
   'https://api.twitter.com/1.1/search/tweets.json?q=buhari&result_type=popular&tweet_mode=extended',
   token,
   secret,
   function (error, data, response){
     if (error) console.error(error);
     data = JSON.parse(data);
     console.log(JSON.stringify(data, 0, 2));
 });