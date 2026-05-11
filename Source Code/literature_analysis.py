import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Datasets/literature_review.csv")


year_count = df["Year"].value_counts()

year_count = year_count.sort_index()


print("\nPUBLICATIONS BY YEAR\n")

print(year_count)


year_count.plot(
    kind="line",
    marker="o"
)

plt.title(
    "Research Trend in Visualization Studies"
)

plt.xlabel("Year")

plt.ylabel("Number of Studies")

plt.tight_layout()


plt.savefig(
    "Figures/literature_trend.png"
)


plt.show()
