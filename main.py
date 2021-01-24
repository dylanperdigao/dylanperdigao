#!/usr/bin/env python
# -*- coding: utf-8 -*-
from github import Github
import numpy as np
import os
import sys

from commitsStats import *
from fileUpdater import *

def updateStatsSection(path, data):
	string="<!--STATS-->\n"
	string+="<!--BEGIN-->\n"
	string+=getProductivity(data)
	string+=getActivityGraph(data)
	string+="<!--END-->\n"
	updateFileInfo(path,'STATS',string)

if __name__=='__main__':
	access_token = sys.argv[1]
	if access_token:
		g = Github(access_token)
		if g:
			user = g.get_user()
			data=getActivityPercentage(user)
			updateStatsSection('README.md',data)
		else:
			print("Error with login: {}".format(g))
	else:
		print("Error with args: {}".format(sys.argv[1]))

		
		

	
