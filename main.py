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
			#get file
			user = g.get_user()
			readme_repo = user.get_repo(user.login)
			readme = readme_repo.get_readme()
			#get stats
			data=getActivityPercentage(user)
			newReadme=updateStatsSection(readme.path,data)
			#commit changes
			readme_repo.update_file(path=readme.path, message="Automatically Updated", content=newReadme, sha=readme.sha, branch='main')
			print("File Automatically Updated")
		else:
			print("Error with login: {}".format(g))
	else:
		print("Error with args: {}".format(sys.argv[1]))

		
		

	
