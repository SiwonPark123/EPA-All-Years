import statbotics
import pandas as pd

sb = statbotics.Statbotics()

START_YEAR = 2002
END_YEAR   = 2025

all_data = []

for year in range(START_YEAR, END_YEAR + 1):
    if(year != 2021):
        print(f"Fetching {year}...")
        offset = 0
        while True:
            batch = sb.get_team_years(year=year, limit=1000, offset=offset)
            if not batch:
                break
            all_data.extend(batch)
            if len(batch) < 1000:
                break
            offset += 1000

df = pd.json_normalize(all_data)
df.to_csv("epa_all_teams_all_years.csv", index=False)
print(f"Saved {len(df):,} rows to epa_all_teams_all_years.csv")