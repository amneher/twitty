#!/usr/bin/env python3

# process twitter JSON data
try:
	import requests
except ImportError:
	print("Module 'requests' not installed")

tl = requests.get('https://api.twitter.com/1.1
