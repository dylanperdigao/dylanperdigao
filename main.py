import sys

from github import Github
from languagesStats import *
from commitsStats import *


def getFileInfo(path):
	is_reading = True
	content = list()
	with open(path, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			if is_reading:
				if "<!--BEGIN-->" in line:
					is_reading = False
				else:
					content.append(line)
			else:
				if "<!--END-->" in line:
					is_reading = False
	# print(content)
	return content


def updateSection(path, section, newContent):
	updated_info = ""
	content = getFileInfo(path)
	for line in content:
		if "<!--{}-->".format(section) in line:
			updated_info += newContent
		else:
			updated_info += line
	return updated_info


def updateStatsSection(usr):
	repositories = usr.get_repos(usr.login)
	repository = usr.get_repo(usr.login)
	data = getActivityPercentage(repositories)
	readme = repository.get_readme()
	# start
	string = "<!--STATS-->\n"
	string += "<!--BEGIN-->\n"
	string += "## Some Statistics\n"
	# productivity
	string += getProductivity(data)
	# activity graph
	string += getActivityGraph(repository, data)
	# languages graph
	string += getLanguagesGraph(repository, repositories)
	# end
	string += "<!--END-->\n"
	new_readme = updateSection(readme.path, 'STATS', string)
	# commit changes
	repository.update_file(path=readme.path, message="Automatically Updated", content=new_readme, sha=readme.sha, branch='main')
	print("File Automatically Updated")


if __name__ == '__main__':
	access_token = sys.argv[1]
	if access_token:
		g = Github(access_token)
		if g:
			# get user
			user = g.get_user()
			# update stats
			updateStatsSection(user)
		else:
			print("Error with login: {}".format(g))
	else:
		print("Error with args: {}".format(sys.argv[1]))

		
		

	
