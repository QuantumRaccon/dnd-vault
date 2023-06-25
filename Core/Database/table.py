import json
from module import *
import pandas as pd
import numpy as np

def get_metadata(obj):
    source = obj.get("source")
    page = obj.get("page", "")
    return f"---\nsource: {source} {page}\ntag: table\n---\n\n"


def main():

    path = "D:\\Archivos\\D&D 5e\\Core\\Tables\\"
    check_directory(path)

    with open('data/tables-data.json') as f:
        data = json.load(f)

    df = pd.read_json("data/tables-data.json").replace({np.nan: None})
    df["name"] = df["name"].where(~df.name.duplicated(), df.name + ' (D)')


    for i, table in enumerate(data):
        name = format(df.iloc[i].get("name").replace("(*)", "()"))
        metadata = get_metadata(table)
        data = read_json(table)
        footnote = get_footnote()

        with open(path + name + ".md", "w") as file:
            file.write(metadata)
            file.write(data)
            file.write(footnote)
    
main()
print_missing_elements()