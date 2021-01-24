#!/usr/bin/env python
# -*- coding: utf-8 -*-
from github import Github
import numpy as np
import os
import sys

from commitsStats import *
from fileUpdater import *

def updateStatsSection(repository, data):
	readme=repository.get_readme()
	string="<!--STATS-->\n"
	string+="<!--BEGIN-->\n"
	string+=getProductivity(data)
	string+=getActivityGraph(data)
	string+="<!--END-->\n"
	newReadme=updateFileInfo(readme.path,'STATS',string)
	#commit changes
	repository.update_file(path=readme.path, message="Automatically Updated", content=newReadme, sha=readme.sha, branch='main')
	print("File Automatically Updated")

if __name__=='__main__':
	access_token = sys.argv[1]
	if access_token:
		g = Github(access_token)
		if g:
			#get file
			user = g.get_user()
			repository = user.get_repo(user.login)
			#update stats
			data=getActivityPercentage(user)
			newReadme=updateStatsSection(repository,data)
		else:
			print("Error with login: {}".format(g))
	else:
		print("Error with args: {}".format(sys.argv[1]))

		
		

	
