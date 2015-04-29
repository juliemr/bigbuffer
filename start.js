var spawn = require('child_process').spawn;
 
var server;
 
var start = function() {
 
    server = spawn('python', ['server.py']);
 
    server.stderr.on('data', function(data) {
      console.log('stderr: ' + data.toString());
    });
 
    // Turning this on makes the tests pass. ???
    // server.stdout.on('data', function(data) {
    //   console.log(data.toString());
    // });
 
    server.on('close', function(code) {
      console.log('**** server has closed');
    });
};
 
process.on('SIGINT', function() {
  console.log('*** shutting down');
  server.kill();
});
 
start();
