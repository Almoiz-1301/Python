# Two types of modules in Python: 
# - Built in Modules 
# - External Modules
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html
import math 
import os 
import mymodules
import requests

print(math.sqrt(16))
mymodules.hello()
r = requests.get("https://confluencetest.mermaidchart.com")
print(r.text)