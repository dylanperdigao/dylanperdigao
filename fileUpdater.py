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

def updateFileInfo(path,key,newContent):
	content = getFileInfo(path)
	with open(path,'w',encoding='utf-8') as f:
		for line in content:
			if "<!--{}-->".format(key) in line:
				f.write(newContent)
			else:
				f.write(line)

if __name__=='__main__':
	test="<!--TEST-->\n"
	test+="<!--BEGIN-->\n"
	test+="test\n"
	test+="<!--END-->\n"
	updateFileInfo('README.md','TEST',test)

