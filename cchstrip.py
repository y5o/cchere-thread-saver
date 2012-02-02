#!/usr/bin/python
# -*- coding:utf-8 -*-

import codecs
import datetime
from lxml import html
import re

def getAuthor(ele):
  """ get author from element
  """
  r = ele.xpath('div/div/a')
  return r[0].text
  

def onefile(i, baseurl, enc = "utf-8"):
  """ get element list from file
  """
  f = codecs.open(str(i)+".html", 'r', enc)
  fulltext = f.read()
  doc = html.fromstring(fulltext) 
  doc.make_links_absolute(baseurl)
  alllist = doc.find_class("pContent")  # list of posts
  # next remove all those recycled (not shown) posts
  alllist = [ele for ele in alllist if len(ele.xpath('div/div/a')) > 0]
  f.close()
  return alllist

def getDateTime(ele):
  """ get a datetime obj from element
  """
  r = ele.xpath('div/div')
  timestr = r[0].text_content()
  patn = "\d\d\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d"
  match = re.search(patn, timestr)
  if match:
    timestr = match.group()
    ret = datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    return ret
  else:
    print "datetime extract error!"

def generateHTML(allposts, outfilename = "all.html", enc = "utf-8"):
  """ put all posts in the given list in to a simple 
      html file.
  """
  begstr = "<html><body>"
  allstr = ""
  for p in allposts:
    allstr = allstr + html.tostring(p)
  endstr = "</body></html>"
  f = codecs.open(outfilename, 'w', enc)
  f.write(begstr + allstr + endstr)
  f.close()

def sortByDate(allposts):
  allposts.sort(key = getDateTime)

if __name__ == '__main__':
  
  maxpage = 243 
  authorToPick = u"Emyn"
  
  baseurl = "http://www.ccthere.com"
  postlist = []
  # read in all posts to one list
  for i in range(1, maxpage+1):
    postlist = postlist + onefile(i, baseurl)
  
  sameauthorlist = [ele for ele in postlist if authorToPick == getAuthor(ele)]
#  print len(sameauthorlist)
#  for ele in postlist:
#    print getDateTime(ele)
#  for ele in sameauthorlist:
#    print getDateTime(ele)
  
  sortByDate(sameauthorlist)
  generateHTML(sameauthorlist) 
#  for ele in sameauthorlist:
#    print getDateTime(ele)

