import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Datasets/enterprise_survey.csv")


# Graph 1: Accuracy improvement

df.plot(
    x="Company",
    y=[
        "DecisionAccuracyBefore",
        "DecisionAccuracyAfter"
    ],
    kind="bar"
)

plt.title("Decision Accuracy Improvement")
plt.ylabel("Accuracy")

plt.tight_layout()

plt.savefig(
    "Figures/accuracy_improvement.png"
)

plt.show()



# Graph 2: Decision time

df.plot(
    x="Company",
    y=[
        "DecisionTimeBefore",
        "DecisionTimeAfter"
    ],
    kind="bar"
)

plt.title("Decision Time Reduction")
plt.ylabel("Days")

plt.tight_layout()

plt.savefig(
    "Figures/time_reduction.png"
)

plt.show()



# Graph 3: Engagement

df.plot(
    x="Company",
    y=[
        "EngagementBefore",
        "EngagementAfter"
    ],
    kind="bar"
)

plt.title("User Engagement Improvement")

plt.tight_layout()

plt.savefig(
    "Figures/engagement_improvement.png"
)

plt.show()
