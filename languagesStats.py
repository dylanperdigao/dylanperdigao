import numpy as np
import pandas as pd
import plotly.express as px


def getLanguagesGraph(repositories=None, languages=None):
	d = {'Language': list(), 'Percentage': list()}
	string = "### Most used languages 📈\n\n"
	if repositories:
		languages = getLanguages(repositories)
	percentage = getLanguagesPercentage(languages)
	string += "![Languages Graph](images/languages_graph.png)\n\n"
	for key, val in languages.items():
		d["Language"].append(key)
		d["Percentage"].append(val)
	d["Language"].reverse()
	d["Percentage"].reverse()
	d["Percentage"] = [x / sum(d["Percentage"]) for x in d["Percentage"]]
	df = pd.DataFrame(data=d)
	fig = px.bar(df, x='Percentage', y='Language', color='Percentage', template='plotly_dark', log_x=True)
	fig.write_image("images/languages_graph.png")
	return string


def getLanguagesPercentage(languages):
	languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))
	sumVal = sum(languages.values())
	for key, val in languages.items():
		languages[key] = round(100 * val / sumVal, ndigits=2)
	return languages


def getLanguages(repositories):
	languages = dict()
	for r in repositories:
		if not r.fork:
			print(r.name)
			for key, value in r.get_languages().items():
				if key not in languages:
					languages[key] = value
				else:
					languages[key] += value
	return languages


def main():
	dicio = {'C': 2247895, 'LLVM': 618850, 'Java': 463687, 'Python': 210048, 'C++': 147358, 'Yacc': 127324,
			 'JavaScript': 122894, 'PHP': 103001, 'UnrealScript': 97659, 'HTML': 93647, 'Lex': 84375, 'Blade': 66429,
			 'MATLAB': 31060, 'Shell': 26076, 'CSS': 9023, 'Makefile': 5798, 'GLSL': 1812, 'Objective-C': 1106,
			 'Batchfile': 752, 'Go': 655, 'SCSS': 157, 'Dockerfile': 113}
	getLanguagesGraph(languages=dicio)


if __name__ == '__main__':
	main()
