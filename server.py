import SimpleHTTPServer
import SocketServer
import threading
 
def printit():
  threading.Timer(0.001, printit).start()
  print("lotsa text lotsa text lotsa text lotsa text");
printit()
 
PORT = 8000
 
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
 
httpd = SocketServer.TCPServer(("", PORT), Handler)
 
print "serving at port", PORT
httpd.serve_forever()
