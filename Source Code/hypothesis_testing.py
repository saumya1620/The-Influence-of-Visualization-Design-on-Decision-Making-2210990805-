import pandas as pd


df = pd.read_csv("Datasets/chi_square_results.csv")


print("\nHYPOTHESIS TESTING RESULTS\n")


for index, row in df.iterrows():

    print("====================================")

    print("Hypothesis:", row["Hypothesis"])

    print("Description:", row["Description"])

    print("Chi-Square Value:", row["ChiSquare"])

    print("P-Value:", row["PValue"])

    print("Status:", row["Status"])


    if float(row["PValue"]) < 0.05:

        print("Conclusion: Statistically Significant")

    else:

        print("Conclusion: Not Significant")


print("====================================")
