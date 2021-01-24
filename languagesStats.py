#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getLanguagesGraph(repositories=None,languages=None):
	string="### Most used languages 📈\n\n"
	string+="```bash\n"
	if repositories:
		languages=getLanguages(repositories)
	percentage = getLanguagesPercentage(languages)
	for key,val in percentage.items():
		string+=generateBar(key,val)
	string+="\n```\n"
	print(string)
	return string

def generateBar(key,val):
	string=key
	if len(key)<7:
		string+="\t"
	string+="\t|"
	size = 4
	n = val*size/10
	for i in range(size*10):
		if i<n:
			string+= "🁢"
		else:
			string+= "🁣"
	string+=" {}%\n".format(val)
	return string

def getLanguagesPercentage(languages):
	languages=dict(sorted(languages.items(), key=lambda item: item[1],reverse=True))
	sumVal=sum(languages.values())
	for key,val in languages.items():
		languages[key] = round(100*val/sumVal,ndigits=2)
	return languages

def getLanguages(repositories):
	languages=dict()
	for r in repositories:
		if not r.fork:
			print(r.name)
			for key, value in r.get_languages().items():
				if key not in languages:
					languages[key] = value
				else:
					languages[key] += value 
	return languages

if __name__=='__main__':
	dicio = {'C': 2247895, 'LLVM': 618850, 'Java': 463687, 'Python': 210048, 'C++': 147358, 'Yacc': 127324, 'JavaScript': 122894, 'PHP': 103001, 'UnrealScript': 97659, 'HTML': 93647, 'Lex': 84375, 'Blade': 66429, 'MATLAB': 31060, 'Shell': 26076, 'CSS': 9023, 'Makefile': 5798, 'GLSL': 1812, 'Objective-C': 1106, 'Batchfile': 752, 'Go': 655, 'SCSS': 157, 'Dockerfile': 113}
	getLanguagesGraph(languages=dicio)
