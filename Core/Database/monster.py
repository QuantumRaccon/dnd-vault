import pandas as pd
import os
import numpy as np
from tqdm import tqdm
from module import *


homebrew = ["CCodex", "MFoV", "MotG", "MaDSS", "ToB", "ToB2"]


def name_to_link(mon):
    name = mon["name"].strip()
    name.replace("'", "")

    if mon.source in homebrew:
        link = f"https://raw.githubusercontent.com/TheGiddyLimit/homebrew/master/_img/{mon.source}/" 
        if mon.source == "ToB2":
            link = "https://raw.githubusercontent.com/TheGiddyLimit/homebrew/master/_img/ToB2/creature/"
    else:
        link = f"https://5e.tools/img/bestiary/{mon.source}/"

    head, sep, tail = name.partition('(')
    head2, sep2, trail2 = head.partition(',')

    if mon.source == "CCodex":
        if trail2 == "":
            head = head.replace(" ", "")
            head = head.lower()
            head = head.replace("'", "")
            u = request_img(link,head)
            if u == "":
                head = head.capitalize()
                u = request_img(link,head)
        else:
            name2 = head2 + trail2
            name2 = name2.replace(" ", "")
            name2 = name2.lower()
            name2 = name2.replace("'", "")
            u = request_img(link, name2)

    else:
        head3 = head2.strip()
        # head3 = head3.replace(" ", "%20")
        u = request_img(link, head3)
        if u == "":
            u = request_img(link, head3)

    if u == "" and tail != "":
        if tail != "D)":
            full_name = " ".join([head.strip(), (sep+tail).strip()]) #%20
            u = request_img(link, full_name)
            if u == "":
                u = request_img(link, full_name)

    if u == "":
        head3 = head2.split(' ', 1)[-1]
        head3 = head3.strip()
        head3 = head3.replace(" ", "%20")
        u = request_img(link, head3)
        if u == "":
            u = request_img(link, head3)

    if u == "":
        head3 = head2.split(" ")
        if len(head3) > 1:
            head4 = "%20".join(head3[:len(head3)-1])
            u = request_img(link, head4)

        if u == "" and len(head3) > 2:
            head4 = "%20".join(head3[:len(head3)-2])
            u = request_img(link, head4)

    return u




def main():

    no_img = 0

    for i in tqdm(range(df.index.size)): 
        mon = df.iloc[i]
        mon_csv = df_csv.iloc[i]
        name = mon["name"]
        size = mon_csv["Size"]
        mon_type = mon_csv["Type"]
        alignment = mon_csv["Alignment"]
        initiative = (mon["dex"]-10)//2 
        cr = mon["cr"]
        ac = mon_csv["AC"]
        environment = mon["environment"]

        has_fluff = bool(mon["fluff"])
        legendary = bool(mon["legendary"])

        tags = ["monster"]

        try:
            for i, tag in enumerate(mon["type"]["tags"]):
                if type(tag) == dict:
                    tag = tag.get("tag")
                if type(tag) == str:
                    tag = tag.replace(" ", "-")
                    mon["type"]["tags"][i] = f"monster/{tag}"

            tags.extend(mon["type"]["tags"])
        except:
            pass


        if environment != None:
            for env in environment:
                env = env.replace(" ", "-")
                tags.append(f"environment/{env}")
     

        try:
            hp = mon["hp"]["average"]
        except:
            try:
                hp = mon["hp"]["special"]
            except:
                hp = mon["hp"]

        lair = mon_csv["Lair Actions"]
        
        mythic = mon_csv["Mythic Actions"]

        regional = mon_csv["Regional Effects"]

        try:
            page = int(mon["page"])
        except:
            page = mon["page"]

        source = mon["source"]


        metadata = f'''---
hp: {hp}
ac: {ac}
cr: {cr}
initiative: {initiative}
type: '{mon_type}'    
size: '{size}'
environment: {environment}
alignment: {alignment}
legendary: {legendary}
lair: {bool(lair)}
mythic: {bool(mythic)}
regional: {bool(regional)}
tags: {tags}
source: "{source}"
page: {page}
---'''


        try:
            image = "![|600]({0})".format(mon.fluff["images"][0]["href"]["url"])
        except:
            url = name_to_link(mon)
            if url != "":
                image = "![|600]({0})".format(url)
            else:
                image = ""

        if image == "":
            no_img += 1

        try:
            token = mon.tokenUrl
        except:
            token = ""
        
        description = ""
        if has_fluff:
            try:
                data = mon.fluff["entries"]
                description = read_json(data)
            except:
                pass

        variant = mon.get("variant")
        if variant != None:
            try:
                variant = read_json(variant)
                variant = "\n" + variant

            except:
                pass
        else:
            variant = ""


        footnote = get_footnote()


        text = f'''

## {name}
---

{image}

## Stats
---

```statblock
creature: {name}
image: {token}
columnHeight: 500
columnWidth: 500
```

## Encounter
---

```encounter-table
name: {name}
creatures:
- 1: {name}
```

## Description
---
{description}
{variant}
{footnote}

'''
        name = name.replace("\"", "")
        name = name.replace("\'", "")
        name = name.replace("*", "")
        name = name.replace("/", "")
        with open(path + name + ".md", 'w') as file:
            file.write(metadata)
            file.write(text)

    print("There are {0} monsters without image".format(no_img))
    print_missing_elements()




if __name__ == "__main__":
    df = pd.read_json("data/monster-data.json")
    df = df.replace({np.nan: None})
    df_csv = pd.read_csv("data/monster-data.csv")
    df_csv = df_csv.replace({np.nan: None})

    df["name"] = df["name"].where(~df.name.duplicated(), df.name + ' (D)')
    df_csv["Name"] = df_csv["Name"].where(~df_csv.Name.duplicated(), df_csv.Name + ' (D)')

    path = "D:\\Archivos\\D&D 5e\\Core\\Monsters\\"
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)
        print("Directory created")

    main()


