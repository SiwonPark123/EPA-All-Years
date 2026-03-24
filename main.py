import pandas as pd

df = pd.read_csv("epa_all_teams_all_years.csv")

team = 3928

def main():
    listOfRank = df[df["team"] == team]["epaRanksTotalRank"].tolist()
    average = sum(listOfRank)/len(listOfRank)
    print(average)

if __name__ == "__main__":
    main()