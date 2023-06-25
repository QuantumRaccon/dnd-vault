import pandas as pd
import numpy as np
from parse_json import read_json, print_missing_elements, check_directory


haz_type = {'CMPX': "complex", 'ENV': "environmental hazard", 'EST': "eldritch strom", 'GEN': "generic", 'HAZ': "hazard", 
     'MAG': "magical trap", 'MECH': "mechanical trap", 'SMPL': "simple trap", 'WLD': "weather", 'WTH': "wilderness hazard"}

metadata_entries = ("source", "page", "threat")

elements = {"effect": "Effect", "eActive": "Active Elements", "eDynamic": "Dynamic Elements", 
"eConstant": "Constant Elements", "countermeasures": "Countermeasures" }

tier_lvl = {1: "level 1-4", 2: "level 5-10", 3:"level 11-16" , 4: "level 17-20"} 

def weather_or_trap_or_hazard(haz_type):
    if haz_type in ("EST", "WLD"):
        return "weather"
    if haz_type in ("ENV", "WTH", "HAZ"):
        return "hazard"
    return "trap"

def add(**kwargs): #add(**k) 
    txt = ""
    for key, value in kwargs.items():
        if value is not None:
            txt += f"{key}: {value}\n"
    return txt

def get_metadata(item):
    kwargs = dict([(a, item[a]) for a in metadata_entries])
    txt = "---\n"
    txt += add(**kwargs)

    tier = item["tier"]
    if tier is not None:
        txt += f"tier: {tier_lvl[tier]}\n"

    haz = item["trapHazType"]
    if haz is not None:
        txt += f"type: {haz_type.get(haz)}\n"
        txt += f"tag: {weather_or_trap_or_hazard(haz)}\n"

    txt += "---\n"

    return txt

def get_data(item):
    entries = item["entries"]

    txt = ""
    if entries is not None:
        txt += read_json(entries)
    
    for key, entry_name in elements.items():
        val = item[key]
        if val is not None:
            val = read_json(val)
            txt += f"**{entry_name}.** {val}"

    return txt


def main():

    df = pd.read_json("data/trapshazards-data.json").replace({np.nan: None})
    df["name"] = df["name"].where(~df.name.duplicated(), df.name + ' (D)')

    path = "D:\\Archivos\\D&D 5e\\Core\\Traps & Hazards\\"

    check_directory(path)

    for i, item in df.iterrows():
        name = item["name"].replace("(*)", "")
        metadata = get_metadata(item)
        data = get_data(item)

        with open(path + name + ".md", "w") as file:
            file.write(metadata)
            file.write(data)


if __name__ == "__main__":
    main()
    print_missing_elements()
