import pandas as pd

df = pd.read_csv('results.csv')

choice = input("Press enter to show (y/n)")

print("Predictions: ")
table = df.to_string(index=False)
print(table)
input("\n Press enter to exit")
print("OK")