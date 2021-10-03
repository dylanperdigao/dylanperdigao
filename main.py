from github import Github
import numpy as np
import os
import sys

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


def commitImg(usr):
	repo = usr.get_repo('dylanperdigao')
	file_list = [
		'images/activity_graph.png',
		'images/languages_graph.png'
	]
	commit_message = 'Updated Image'
	master_ref = repo.get_git_ref('heads/main')
	master_sha = master_ref.object.sha
	base_tree = repo.get_git_tree(master_sha)
	element_list = list()
	for entry in file_list:
		with open(entry, 'rb') as input_file:
			data = input_file.read()
		if entry.endswith('.png'):
			data = base64.b64encode(data)
		element = InputGitTreeElement(entry, '100644', 'blob', data)
		element_list.append(element)
	tree = repo.create_git_tree(element_list, base_tree)
	parent = repo.get_git_commit(master_sha)
	commit = repo.create_git_commit(commit_message, tree, [parent])
	master_ref.edit(commit.sha)


def updateStatsSection(usr):
	commitImg(usr)
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
	string += getActivityGraph(data)
	# languages graph
	string += getLanguagesGraph(repositories)
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

		
		

	
