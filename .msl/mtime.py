#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import re

from msl import *
from msl.mtime import *;
from time import mktime
import datetime;


try:
	import pytz
except:
	pass

_localtz = doifcan(lambda: pytz.timezone("Asia/Calcutta"));


def timenow():
	return int(mktime(datetime.datetime.now(_localtz).timetuple()));

tnow = timenow;

def timeint2obj(x):
	return datetime.datetime.fromtimestamp(x);

def time2format(formate, tat = None):#tat: TimeAt
	return datetime.datetime.fromtimestamp(rifn(tat, tnow())).strftime(formate);

t2f = time2format;

def parsetime(times, formate, errortime = None): #times: time_string
	return doifcan1(lambda: int(mktime(datetime.datetime.strptime(times.strip(), formate).timetuple())), errortime)

def str2time(times, errortime = 0): #times: time_String
	times = re.sub('\s+', ' ', times).strip()
	# formates = gen_form(['']+gen_form(['%d-%m-'], ['%y', '%Y']), [' '], ['', '%I:%M:%S %p', '%H:%M:%S', '%I:%M %p', '%H:%M' ])
	formates = ['', ' %I:%M:%S %p', ' %H:%M:%S', ' %I:%M %p', ' %H:%M', '%d-%m-%y ', '%d-%m-%y %I:%M:%S %p', '%d-%m-%y %H:%M:%S', '%d-%m-%y %I:%M %p', '%d-%m-%y %H:%M', '%d-%m-%Y ', '%d-%m-%Y %I:%M:%S %p', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %I:%M %p', '%d-%m-%Y %H:%M', '%d/%m/%y ', '%d/%m/%y %I:%M:%S %p', '%d/%m/%y %H:%M:%S', '%d/%m/%y %I:%M %p', '%d/%m/%y %H:%M', '%d/%m/%Y ', '%d/%m/%Y %I:%M:%S %p', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %I:%M %p', '%d/%m/%Y %H:%M'];
	return intf(fold(lambda x,y: parsetime(times, y.strip()) if x == None else x, formates, None), errortime)

t2f_date = lambda tat=None: time2format("%d-%m-%Y", tat);
t2f_time = lambda tat=None: time2format("%d-%m-%y %I:%M:%S %p", tat);


s2t = str2time;

def daystarttime(tat = None):
	return parsetime(t2f_date(tnow()), "%d-%m-%Y");
#	return s2t(t2f_date(tat));

def timeondate(d, m, y):
	return s2t(str(d)+"-"+str(m)+"-"+str(y));
