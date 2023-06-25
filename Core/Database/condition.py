import pandas as pd
import numpy as np
from tqdm import tqdm
from parse_json import read_json, print_missing_elements, request_img, check_directory

df_con = pd.read_json("data/conditions-data.json")
df_dis = pd.read_json("data/diseases-data.json")

df_con = df_con.assign(type = "condition")
df_dis = df_dis.assign(type = "disease")

frames = [df_con, df_dis]
df = pd.concat(frames)
df = df.replace({np.nan: None})
df = df.reset_index()

print(df["type"])


for i in tqdm(range(df.index.size)):
    con = df.iloc[i]
    name = con.get("name")
    source = con.get("source")
    page = con.get("page")
    tag = con.get("type")
    has_fluff = con.get("hasFluffImages")

    if has_fluff != None:
        link = f"https://5e.tools/img/conditionsdiseases/{source}/"
        image = request_img(link, name.lower())
        image = f"![|600]({image})"
    else:
        image = ""

    path = "D:\\Archivos\\D&D 5e\\Core\\Conditions\\"
    check_directory(path)
    data = read_json(con["entries"])


    metadata = \
f'''---
tag: {tag}
source: {source}
page: {page}
---
'''

    data = \
f'''
{data}

{image}
'''

    with open(path+name+".md", "w") as file:
        file.write(metadata)
        file.write(data)
        
print_missing_elements()