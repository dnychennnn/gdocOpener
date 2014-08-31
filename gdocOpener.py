#!/bin/python
# -*- coding: utf-8 -*-

import json,webbrowser,sys

json_file = open(sys.argv[2],'r')
json_data = json.load(json_file)
webbrowser.open(json_data['url'])
