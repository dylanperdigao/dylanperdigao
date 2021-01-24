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
	print("Args: {}".format(len(sys.argv)))
	access_token = sys.argv[1]
	if access_token:
		g = Github(access_token)
		user = g.get_user()
		data=getActivityPercentage(user)
		#h=[100, 76, 84, 64, 24, 3, 7, 3, 4, 23, 33, 42, 24, 60, 87, 136, 159, 171, 127, 88, 100, 77, 126, 112]
		#data = [round(100*val/sum(h)) for val in h]
		updateStatsSection('README.md',data)
		
		

	
