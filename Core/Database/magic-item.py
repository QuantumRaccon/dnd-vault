import pandas as pd
import numpy as np
from tqdm import tqdm
from parse_json import read_json, print_missing_elements, request_img, check_directory
import re

metadata_entries = ("source", "page", "rarity", "wondrous", "weight", "lootTables", 
"dmg1", "dmg2", "dmgType", "weaponCategory", "sentient", "range", "curse", "ac", "value")

data_entries = ("bonusSpellAttack", "bonusSpellSaveDc","bonusWeapon", "bonusAc", "dmgType",
 "bonusWeaponAttack", "bonusSavingThrow", "bonusWeaponDamage","bonusSpellDamage", "bonusAbilityCheck" )

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


def get_metadata(item):    
    kwargs = dict([(a, item[a]) for a in metadata_entries])
    txt = "---\n"
    txt += add(**kwargs)

    att = item["reqAttune"]
    if att is not None:
        txt += f"attunement: {att}\n"

    types = item["Type"]
    if types is not None:
        types = types.split(", ") 
        txt += f"type: {types}\n"

    txt += "tag: item/magic\n"

    txt += "---\n\n"


    return txt
    

def get_data(item):
    properties = item["Properties"]
    inherits = item["inherits"]
    entries = item["entries"]
    image = item["hasFluffImages"]

    txt = ""
    
    if properties is not None:
        txt += "**"+ format_properties(properties)+"**" + "\n\n"

    if inherits is not None:
        entry = inherits.get("entries")
        entry = read_json(entry)
        txt += f"**Inherits**. {entry}\n"

    if entries is not None:
        entries = read_json(entries)
        txt += f"{entries}\n"


    for element in data_entries:
        a = "{=" + element + "}"
        i = item[element] 
        if type(i) == float:
            i = int(round(i,2))
        if type(i) == int:
            i = "+" + str(i)
            
        txt = txt.replace(a, str(i))


    if image == True:
        source = item["source"]
        name = item["name"]
        link = f"https://5e.tools/img/items/{source}/"
        h = name.replace(" ", "%20")
        url = request_img(link, h)
        txt += f"![|600]({url})"

    return txt


def main():
    df1 = pd.read_json("data/magic-items-data.json").replace({np.nan: None})
    df2 = pd.read_csv("data/magic-items-data.csv").replace({np.nan: None})
    df1["wondrous"] = df1["wondrous"].replace(1.0, True)
    df1["sentient"] = df1["sentient"].replace(1.0, True)
    df1["curse"] = df1["curse"].replace(1.0 , True)
    df = pd.concat([df1, df2], axis=1)
    df["name"] = df["name"].where(~df.name.duplicated(), df.name + " (D)")

    path = "D:\\Archivos\\D&D 5e\\Core\\Items\\Magic\\"
    check_directory(path)

    for i, item in tqdm(df.iterrows()):
        name = item["name"].replace("(*)", "")
        metadata = get_metadata(item)
        data = get_data(item)
        

        with open(path + name + ".md", "w") as file:
            file.write(metadata)
            file.write(data)

    

if __name__ == "__main__":
    main()
    print_missing_elements()


    






