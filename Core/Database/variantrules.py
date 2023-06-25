import pandas as pd
import numpy as np
from module import *

dict = {"O": "optional", "V": "variant", "VO": "optional-variant"}

df = pd.read_json("data/variantrules-data.json").replace({np.nan: None})
df["name"] = df["name"].where(~df.name.duplicated(), df.name + ' (D)')

path = "D:\\Archivos\\D&D 5e\\Core\\Rules\\"

check_directory(path)


for _, item in df.iterrows():
    name = item["name"]
    source = item["source"]
    page = item["page"]
    type = dict.get(item["ruleType"])
    entries = item["entries"]

    txt = \
f'''---
source: {source}
page: {page}
'''

    if type is not None:
        txt += f"type: {type}\n"
        txt += f"tag: rule/{type}\n"
    
    else:
        txt += "tag: rule\n"

    txt += "---\n\n"
    txt += read_json(entries)
    
    name = format(name)
    with open(path + name + ".md", "w") as file:
        file.write(txt)

print_missing_elements()

