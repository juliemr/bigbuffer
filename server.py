import SimpleHTTPServer
import SocketServer
import sys

def printit(length):
  for i in range(0, length):
    sys.stdout.write('0')
 
PORT = 9005
 

class LoudHttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(arg):
    printit(10000)
    return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(arg)

Handler = LoudHttpRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)
 
print "serving at port", PORT
httpd.serve_forever()
