import pandas as pd
import numpy as np
from module import *


# source page
# _fSkills
# _fLangs
# _fTools
# _fOtherBenifits
# tag

# entries


def get_metadata(obj):
    source = obj.get("source")
    page = obj.get("page", "")
    skills = obj.get("_fSkills")
    langs = obj.get("_fLangs")
    tools = obj.get("_fTools")
    other_benifits = obj.get("_fOtherBenifits")
    misc = obj.get("_fMisc")

    str = f"""---
source: {source} {page}
tag: background
---\n\n"""
    return str


def main():
    df = pd.read_json("data/backgrounds-data.json").replace({np.nan: None})
    df["name"] = df["name"].where(~df.name.duplicated(), df.name + ' (D)')

    path = "D:\\Archivos\\D&D 5e\\Core\\Backgrounds\\"
    check_directory(path)
    
    for _, item in df.iterrows():
        name = format(item["name"])
        entries = item.get("entries")
        fluff = item.get("fluff")


        metadata = get_metadata(item)
        data = read_json(fluff)
        data += read_json(entries)
        footnote = get_footnote()
    
        with open(path + name + ".md", "w") as file:
            file.write(metadata)
            file.write(data)
            file.write(footnote)

main()
print_missing_elements()
