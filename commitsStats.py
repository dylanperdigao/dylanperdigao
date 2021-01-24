def getActivityGraph(data):
	string="### Activity Graph 📈\n\n"
	string+="```bash\n"
	size = max(data)
	for i in range(size-1,0,-1):
		for val in data:
			if i<=val:
				string += " |"
			else:
				string += "  "
		string += "\n"
	string += len(data)*"=="+"\n "
	for i in range(0,len(data),4):
		if i<8:
			string += str(i)+"h      "
		elif i==8:
			string += str(i)+"h     "
		else:
			string += str(i)+"h     "
	string+="\n```\n"
	#print(string)
	return string

def getProductivity(data):
	data = data[4:] + data[:4]
	x = [sum(data[i:i+8]) for i in range(0,len(data),8)]
	index = x.index(max(x))
	string="### I'm more productive "
	if index==0:
		string += "in the Morning 🌅\n"
	elif index==1:
		string += "in the Afternoon 🌇\n"
	else:
		string += "at Night 🌌\n"
	string += "({}% of my commits)\n\n".format(max(x))
	#print(string)
	return string

def getActivityPercentage(user):
	hours = [ 0 for _ in range(24)]
	for r in user.get_repos():
		for c in r.get_commits():
			hours[c.commit.author.date.hour] += 1
	percentage = [round(100*val/sum(hours)) for val in hours]
	#print("Percentage: {}".format(percentage))
	return percentage