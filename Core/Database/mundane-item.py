import pandas as pd
import numpy as np
from tqdm import tqdm
from parse_json import read_json, print_missing_elements, request_img, check_directory
import re

def add(**kwargs): #add(**k) 
    txt = ""
    for key, value in kwargs.items():
        if value is not None:
            txt += f"{key}: {value}\n"
    return txt

def format_properties(txt):
    txt = re.sub('([a-z])([A-Z])', "\g<1>, \g<2>", txt)
    txt = re.sub('([a-zA-Z])\s(\d)', "\g<1>: \g<2>", txt)
    txt = txt.replace(", - ", " - ")
    arr = txt.split(", ")
    if len(arr) > 4:
        return "\n".join(arr)
    return ", ".join(arr)
    
 
def get_metadata(item, item2):
    elements = ("dmg1", "dmg2", "dmgType", "weaponCategory", "weapon", "armor", "range", 
    "age", "ac", "vehHp", "vehAc", "speed", "crew", "vehDmgThresh", "capCargo", "carryingCapacity")
    
    metadata = \
f'''---
source: {item["Source"]}
page: {item2["page"]}
rarity: {item["Rarity"]}
type: {item["Type"].split(", ")}
tag: item/mundane
'''

    metadata += add(value=item["Value"], weight=item["Weight"])
    kwargs = dict([(a, item2[a]) for a in elements])
    metadata += add(**kwargs)
    if item2["stealth"] == True:
        metadata += "stealth: disadvantage\n"

    metadata += "---\n\n"
    return metadata


df = pd.read_json("data/mundane-items-data.json")
df = df.replace({np.nan: None})

df_csv = pd.read_csv("data/mundane-items-data.csv")
df_csv = df_csv.replace({np.nan: None})      
df_csv["Name"] = df_csv["Name"].where(~df_csv.Name.duplicated(), df_csv.Name + " (D)")


path = "D:\\Archivos\\D&D 5e\\Core\\Items\\Mundane"
check_directory(path)



for i, item in tqdm(df_csv.iterrows()):
    name = item["Name"]
    item2 = df.loc[i]
    metadata = get_metadata(item, item2)

    data = ""
    if item["Properties"] is not None:
        data += "**"+format_properties(item["Properties"])+"**" + "\n\n"

    inheritance = item2["inherits"]
    entries = item2["entries"] 
    additional_entries = item2["additionalEntries"]
    image = item2["hasFluffImages"]


    if inheritance is not None:
        data += "**Inherits.** " + read_json(inheritance) 
    
    if entries is not None:
        data += read_json(entries)

    if additional_entries is not None:
        data += read_json(additional_entries)

    if image == True:
        source = item2["source"]
        link = f"https://5e.tools/img/items/{source}/"
        h = name.replace(" ", "%20")
        url = request_img(link, h)
        data += f"![|600]({url})"


    with open(path + name + '.md', "w") as file:
        file.write(metadata)
        file.write(data)
    

print_missing_elements()

