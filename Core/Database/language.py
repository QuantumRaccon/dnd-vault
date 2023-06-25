import pandas as pd
import numpy as np
from tqdm import tqdm
from parse_json import read_json, print_missing_elements, request_img, check_directory, parse_text

df = pd.read_json("data/languages-data.json")
df = df.replace({np.nan: None})
df["name"] = df["name"].where(~df.name.duplicated(), df.name + " (D)")

path = "D:\\Archivos\\D&D 5e\\Core\\Languages\\"
check_directory(path)           

for i in tqdm(range(df.index.size)):

    lan = df.iloc[i]
    metadata = "---\n"
    data = "\n"

    name = lan["name"]
    metadata += f"source: {lan.source}\npage: {lan.page}\n"

    if lan.type != None:
        metadata += f"type: {lan.type}\n"
    if lan.script != None:
        metadata += f"script: {lan.script}\n"
    if lan.dialects != None:
        metadata += f"dialect: {lan.dialects}\n"

    metadata += "tag: language\n"

    metadata += "---\n"
        
    if lan.typicalSpeakers != None:
        data += "speakers:: " + ", ".join([parse_text(k) for k in lan.typicalSpeakers]) + "\n\n"
        
    if lan.entries != None:
        data += read_json(lan.entries)

    if lan.hasFluffImages != None:
        link = f"https://5e.tools/img/languages/{lan.source}/"
        image = request_img(link, name)
        image = f"![|600]({image})"
        data += image

    with open(path+name+".md", "w") as file:
        file.write(metadata)
        file.write(data)
        
print_missing_elements()


