#!/usr/bin/python
# -*- coding:utf-8 -*-

# in some threads people post their emails in their post
# it is hard for the OP to collect all the emails manually
# this script will grab all the emails via re
# and print email, date time of post, author
import codecs
import datetime
import re
from cchstrip import *

def findemail(post):
  """ match an email addr, if no match return empty string
      post is an xml element
  """
  r = post.xpath('div')
  allstr = r[0].text_content()
  # print allstr
  patn = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
  match = re.search(patn, allstr)
  if match:
    # print match.group()
    return match.group()
  else:
    # print "not match!"
    return '' 
def buildEmailList(allposts):
  """ build a list of (email, author, time)
  """
  l = []
  sortByDate(allposts)
  for post in allposts:
    e = findemail(post)
    if (e != ''):
      au = getAuthor(post)
      dt = getDateTime(post)
      l.append((e, au, dt))
  return l

if __name__ == '__main__':
  
  maxpage = 26 
  
  baseurl = "http://www.ccthere.com"

  postlist = []
  # read in all posts to one list
  for i in range(1, maxpage+1):
    postlist = postlist + onefile(i, baseurl)
 
  l = buildEmailList(postlist)
  print len(l)
  fmt = u'{0:<35}{2:^20}{1:<20}'
  for it in l:
    print fmt.format(it[0], it[1], it[2].strftime("%Y-%m-%d %H:%M:%S"))

