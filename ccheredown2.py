#!/usr/bin/python
# -*- coding:utf-8 -*-

# the function is pretty much the same with ccheredown.py
# the difference here is that I deciphered the javascript code
# in the ccthere original data transmission
# As a result, I manually construct the content without the need
# of a javascript engine, and therefore do not need selenium any more
# The purpose is still download all the pages (but this time only the 
# central part with all posts) and save them into local html files.
# The files are consistent with the files created by ccheredown.py
# and thus cchstrip.py can work on it without any change

# download all the data from one ccthere thread
# input: maxpage for page number
#        threadnum for the thread
# output: each page is a single html file with everything except image

import codecs
import time 
import mechanize
import urllib2
from lxml import html

def zJ_PE(alltext):
  """ from the entire source, get the meaningful center part
      and decoded it as in the javascript function zJ_PE
      return a unicode version of the center part
  """
  # get the center part of the page, encrypted
  texts = alltext.partition('ls=\"')
  alltext = texts[2][3:]

  texts2 = alltext.partition('\";')
  alltext = texts2[0]

  # decode, re-implement of js zJ_PE function
  list1 = ['~','#','<','@','>','!','&','*','(',')',':',';','=',',','|','+']
  list2 = ['%1', '%2', '%3', '%4', '%5', '%6', '%7', '%8', '%9', '%A', '%B', '%C', '%D', '%E', 'e','%20']
  for i in range(0, len(list1)):
    alltext = alltext.replace(list1[i], list2[i])

  decodedtext = urllib2.unquote(alltext) # decoded text is in utf8, but still a str
  decodedtext = unicode(decodedtext, 'utf8')  # change it to unicode

  return decodedtext

def saveOnefile(decodedtext, filename, enc = 'utf8'):
  """ save them with the original header
      the header is just for the completeness, not really necessary
  """
  headstr =  '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="zh" xml:lang="zh" xmlns="http://www.w3.org/1999/xhtml"><head>
<meta content="text/html;charset=utf-8" http-equiv="content-type" /> <body>\n'''
  tailstr = '\n</body></html>'
  f = codecs.open(filename, 'w', enc)
  f.write(headstr)
  f.write(decodedtext)
  f.write(tailstr)
  f.close()

if __name__ == '__main__':
  maxpage = 5
  threadnum = "3653131"
  linkaddr = "http://www.ccthere.com/thread/"

  b = mechanize.Browser()
  b._factory.encoding = "utf8"
  b.set_handle_robots(False)
  b.addheaders = [('User-Agent','Mozilla/4.0(compatible; MSIE 6.0; Windows 98;)')]

  for i in range(1, maxpage+1):
    # connect
    response = b.open(linkaddr+threadnum+'/'+str(i))
    alltext = response.read()
    decodedtext = zJ_PE(alltext)
    saveOnefile(decodedtext, str(i)+'.html')
