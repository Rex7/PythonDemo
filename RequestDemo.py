"""
Requests Run Check
Its just a simple demo for http handling
"""

import requests


r = requests
s = r.get("http://google.com")
file = open("new.html", "w")
file.write(s.text)
file.flush()
file.close()