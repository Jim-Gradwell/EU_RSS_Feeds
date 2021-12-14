import re
from datetime import datetime


CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext


def generate_timestamp():
	now = datetime.now()
	timestamp = now.strftime("%Y%m%d%H%M%S")

	return timestamp