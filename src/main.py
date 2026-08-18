import pandas

# dataset
df_dataset = pandas.read_csv("dataset/dataset.csv")

# text
text_columns = "|"
text_divider = "|"
for column in df_dataset.columns:
    text_columns += f" {column} |" # ADD COLUMN
    text_divider += f" --- |" # ADD DIVIDER

text_rows = "|"
for i in range(len(df_dataset.index)):
    for row_entry in df_dataset.loc[i]:
        text_rows += f" {row_entry} |" # ADD ROWENTRY
    text_rows += "\n|"
text_rows = text_rows[0:len(text_rows)-2]

# print and create file
print(f"{text_columns}\n{text_divider}\n{text_rows}")
with open("dataset/markdown-table.txt", "w") as file:
    file.write(f"{text_columns}\n{text_divider}\n{text_rows}")