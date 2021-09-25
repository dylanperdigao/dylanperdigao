import numpy as np
import pandas as pd
import plotly.express as px


def getActivityGraph(data):
    string = "### Activity Graph 📈\n\n"
    string += "![Activity Graph](images/activity_graph.png)"
    d = {'Hours': [x for x in range(24)], 'Commits': data}
    df = pd.DataFrame(data=d)
    fig = px.bar(df, x='Hours', y='Commits', color='Commits', template='plotly_dark')
    fig.write_image("images/activity_graph.png")
    return string


def getProductivity(data):
    data = data[4:] + data[:4]
    x = [sum(data[i:i + 8]) for i in range(0, len(data), 8)]
    index = x.index(max(x))
    string = "### I'm more productive "
    if index == 0:
        string += "in the Morning 🌅\n"
    elif index == 1:
        string += "in the Afternoon 🌇\n"
    else:
        string += "at Night 🌌\n"
    string += "({}% of my commits)\n\n".format(max(x))
    # print(string)
    return string


def getActivityPercentage(repositories):
    hours = [0 for _ in range(24)]
    for r in repositories:
        if not r.fork:
            for c in r.get_commits():
                hours[c.commit.author.date.hour] += 1
    percentage = [round(100 * val / sum(hours)) for val in hours]
    # print("Percentage: {}".format(percentage))
    return percentage


def main():
    d = {'hours': [x for x in range(24)], 'commits': [np.random.randint(100) for _ in range(24)]}
    getActivityGraph(d)


if __name__ == '__main__':
    main()
