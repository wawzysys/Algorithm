import pandas as pd

# Creating a DataFrame to present the GDP and population data for China from 1993 to 2021 in a table format
data = {
    "Year": list(range(1993, 2022)),
    "GDP (in Billion USD)": [444.73, 564.32, 734.55, 863.75, 961.60, 1029, 1094, 1211, 1339, 1471, 1660, 1955, 2286, 2752, 3550, 4594, 5102, 6087, 7552, 8532, 9570, 10480, 11060, 11230, 12310, 13890, 14280, 14690, 17820],
    "Population (in Millions)": [1178.4, 1189.7, 1204.9, 1217.6, 1230.1, 1241.9, 1252.8, 1262.7, 1271.7, 1280.4, 1288.4, 1293.3, 1303.7, 1309.3, 1316.3, 1324.7, 1331.3, 1337.7, 1351.4, 1353.9, 1361.1, 1368.0, 1373.1, 1377.5, 1383.1, 1389.5, 1395.1, 1400.7, 1411.9]
}

# Creating the DataFrame
df = pd.DataFrame(data)

print(df)