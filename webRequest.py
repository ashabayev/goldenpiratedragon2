import urllib2
from HTMLParser import HTMLParser

#manually enter your email and password before you run it
#r = requests.get('http://game.hackdfw.com/play/puzzles',auth=('username/email','pass'))

#retrieves the html from the webpage using urllib
def readHTML():
	feed = urllib.urlopen('http://game.hackdfw.com/play/puzzles',auth=('username/email','pass'))
	html = feed.read()
	return html

#@param stream array of strings
def extractInfo(stream):
	index = stream.get('')
	

# makes a subclass of HTMLParser and uses it to 
# parse the HTML so we can get elements from the 
# hackDFW page
#@param HTMLParser class
#@param htmlText string

def parser(HTMLParser,htmlText):

	class MyHTMLParser(HTMLParser):
	  htmlStream = []
	    # create a subclass and override the handler methods

	  def handle_starttag(self, tag, attrs):
	      htmlStream.append(tag)
	  def handle_endtag(self, tag):
	      htmlStream.append(tag)
	  def handle_data(self, data):
	      htmlStream.append(data)

	    # instantiate the parser
	    parser = MyHTMLParser()
	    parser.feed(htmlText)


def caesarCiph():
  # send info through http://eliyazdi.github.io/decode/
  # yeah i know its cheating but i really dont feel like reinventing the wheel here
