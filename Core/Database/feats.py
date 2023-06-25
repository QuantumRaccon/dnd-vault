import pandas as pd
import numpy as np
from sympy import fu
from module import *

df = pd.read_json("data/feats-data.json").replace({np.nan: None})
df["name"] = df["name"].where(~df.name.duplicated(), df.name + ' (D)')




def get_metadata(obj):
    source = obj.get("source")
    page = obj.get("page", "")
    req = obj.get("_slPrereq")
    return f"---\nsource: {source} {page}\nrequisites: {req}\ntag: feat\n---\n\n"

def get_data(obj):
    entries = obj.get("entries")
    full_entries = obj.get("_fullEntries")
    if full_entries is not None:
        return read_json(full_entries)
    return read_json(entries)


def main():
    df = pd.read_json("data/feats-data.json").replace({np.nan: None})
    df["name"] = df["name"].where(~df.name.duplicated(), df.name + ' (D)') 

    path = "D:\\Archivos\\D&D 5e\\Core\\Feats & Skills\\"
    check_directory(path)
    
    for _, item in df.iterrows():
        name = format(item["name"])

        metadata = get_metadata(item)
        data = get_data(item)
        footnote = get_footnote()
    
        with open(path + name + ".md", "w") as file:
            file.write(metadata)
            file.write(data)
            file.write(footnote)

main()
print_missing_elements()

