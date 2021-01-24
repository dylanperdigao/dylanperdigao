#!/usr/bin/env python
# -*- coding: utf-8 -*-
from github import Github
import numpy as np
import os
import sys

from languagesStats import *
from commitsStats import *

def getFileInfo(path):
	isReading=True
	content=list()
	with open(path,'r',encoding='utf-8') as f:
		for line in f.readlines():
			if isReading:
				if "<!--BEGIN-->" in line:
					isReading=False
				else:
					content.append(line)
			else:
				if "<!--END-->" in line:
					isReading = False
	#print(content)
	return content

def updateSection(path,section,newContent):
	updatedInfo=""
	content = getFileInfo(path)
	for line in content:
		if "<!--{}-->".format(section) in line:
			updatedInfo+=newContent
		else:
			updatedInfo+=line
	return updatedInfo

def updateStatsSection(user):
	repositories = user.get_repos(user.login)
	repository = user.get_repo(user.login)
	data=getActivityPercentage(repositories)
	readme=repository.get_readme()
	#start
	string="<!--STATS-->\n"
	string+="<!--BEGIN-->\n"
	string+="## Some Statistics\n"
	#productivity
	string+=getProductivity(data)
	#activity graph
	string+=getActivityGraph(data)
	#languages graph
	string+=getLanguagesGraph(repositories)
	#end
	string+="<!--END-->\n"
	newReadme=updateSection(readme.path,'STATS',string)
	#commit changes
	repository.update_file(path=readme.path, message="Automatically Updated", content=newReadme, sha=readme.sha, branch='main')
	print("File Automatically Updated")

if __name__=='__main__':
	access_token = sys.argv[1]
	if access_token:
		g = Github(access_token)
		if g:
			#get user
			user = g.get_user()
			#update stats
			updateStatsSection(user)
		else:
			print("Error with login: {}".format(g))
	else:
		print("Error with args: {}".format(sys.argv[1]))

		
		

	
