import urllib2
import requests
from HTMLParser import HTMLParser
def main():
	email= "uremail"
	passwd= "urpass"
	allhtml = readHTML(email,passwd)
	codehtml = parser(HTMLParser, allhtml)
	caesarCiph()
#manually enter your email and password before you run it
#r = requests.get('http://game.hackdfw.com/play/puzzles',auth=('username/email','pass'))

#retrieves the html from the webpage using urllib
def readHTML(email,passwd):
	feed = urllib.urlopen('http://game.hackdfw.com/play/puzzles',auth=(email,passwd))
	html = feed.read()
	return html

#@param stream array of strings
#**********might not need this anymore
def extractInfo(stream):
	info = []
	index = stream.get('b') #get bolded text; the codes are bolded
	for i in range(0,b.length,i=i+2): #get every other index
		info.append(stream[index+1]) #appends all bolded content
	

# makes a subclass of HTMLParser and uses it to 
# parse the HTML so we can get elements from the 
# hackDFW page
#@param HTMLParser class
#@param htmlText string

def parser(HTMLParser,htmlText):

	class MyHTMLParser(HTMLParser):
	  htmlStream = []
	    # create a subclass and override the handler methods
	  def handle_data(self, data):
	  	if class=='code' and tag=='b': #the tag thing might throw an error here
	  		htmlStream.append(data) #should theoretically append all the codes

	    # instantiate the parser
	    parser = MyHTMLParser()
	    parser.feed(htmlText)
	    return htmlStream
	

def caesarCiph(key,email,counter):
  # send info through http://eliyazdi.github.io/decode/
  # yeah i know its cheating but i really dont feel like reinventing the wheel here
  payload = payload{'key':key,'email':email,'dabutton':click}
  r = request('http://eliyazdi.github.io/decode/',params=payload)
  print "Request %s sent" % counter #assuming python 2
