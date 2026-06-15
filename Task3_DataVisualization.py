import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

avg_scores = [
    df['math score'].mean(),
    df['reading score'].mean(),
    df['writing score'].mean()
]

subjects = ['Math', 'Reading', 'Writing']

plt.bar(subjects, avg_scores)
plt.title("Average Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Score")

plt.show()
plt.savefig("graph.png")
print("Graph Saved")