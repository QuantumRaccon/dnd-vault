import pandas as pd
from module import *
from tqdm import tqdm


schools = {"N":"Necromancy" , "A":"Abjuration", "C":"Conjuration", "V":"Evocation", "T":"Transmutation", "E":"Enchantment", "D":"Divination", "I":"Illusion" }
levels = {1: "st", 2: "nd", 3:"rd"}
times = {1: ""}
areas = {"Q": "square", "ST": "single-target", "MT": "multi-target", "C":"cube", "S":"sphere", "Y":"cylinder", "N": "cone", "L": "line", "H": "dome", "W": "wall", "R": "radius" }


def get_first_header(level, school):
    ''' 
    recives level as int and school as str
    returns header of spell at the top
    for example: 5th level conjuration
    '''
    if level == 0:
        school = school.capitalize()
        return f"_{school} cantrip_"
    
    prefix = levels.get(level, "th")
    return f"_{level}{prefix}-level {school}_"


def get_casting_time(time_json):
    '''
    recives spell["time"] element in json
    returns time for casting
    for example: 1 action
    
    '''
    
    if isinstance(time_json, dict):
        time = time_json
        number = time.get("number")
        unit = time.get("unit") + times.get(number, "s")
        return f"{number} {unit}"
    
    if isinstance(time_json, list):
        add = ""
        u = ""
        for time in time_json:
            u += add
            number = time.get("number")
            unit = time.get("unit") + times.get(number, "s")
            u += f"{number} {unit}"
            add = " or "
        return u        
    
    
def get_range(range_json):
    '''
    recives spells["range"] json
    returns range of the spell
    example: self (15-foot cone) or 150 miles
    
    '''
    
    type = range_json.get("type")
    if type == "point":
        distance = range_json.get("distance")
        amount = distance.get("amount", "")
        unit = distance.get("type", "")
        if amount == "":
            return f"{unit}".capitalize()
        return f"{amount} {unit}".capitalize()
    
    else:
        type = range_json.get("type")
        distance = range_json.get("distance", "")
        if distance == "":
            return f"{type}".capitalize()
        amount = distance.get("amount", "")
        unit = distance.get("type", "")
        
        return f"self ({amount}-{unit} {type})".replace("feet", "foot").capitalize()

    
def get_components(json):
    '''
    recives spell["components"] 
    returns the components 
    example: V, S, M (A bit of dust)
    '''
    
    u = []
    if json.get("v") == True:
        u.append("V")
    if json.get("s") == True:
        u.append("S")
    if json.get("m", "") != "":
        txt = json.get("m", "")
        if isinstance(txt, dict):
            txt = txt.get("text",txt)
        u.append(f"M ({txt})")        
    u = ", ".join(u)

    return u


def get_duration(json):
    '''
    recives spell["duration"] 
    returns the duration of the spell
    example: Concentration, up to 1 hour 
    
    Also returns if its concentration as a bool
    '''
    
    u = ""
    add = ""
    concentration = False
    upTo = False
    for element in json:
        u += add
        if element.get("type") == 'timed':
            concentration = element.get("concentration", False)
            if concentration:
                u += "concentration, "    
            duration = element.get("duration")
            upTo = duration.get("upTo", False)
            if upTo:
                u += "up to "
                
            amount = duration.get("amount", "")
            unit = duration.get("type", "") + times.get(amount, "s")
            
            u += f"{amount} {unit}"
            
        elif element.get("type") == 'permanent':
            addd = ""
            u += "Until "
            for end in element.get("ends"):
                u += addd
                if end == "dispel":
                    u += "dispelled"
                elif end == "trigger":
                    u+= "triggered"
                addd = " or "
                
        elif element.get("type") == "instant":
            u += "instantaneous"
        
        elif element.get("type") == "special":
            u += "special"
        
        add = " or "
    u = u.capitalize()
    return u, concentration
            

def get_area(lst):
    '''
    recives spell["areaTags"]
    returns its area effects or tags
    '''
    
    u = []
    if str(lst) != "nan": 
        for x in lst:
            u.append(areas.get(x,x))    
        u = ", ".join(u)
        u = "[" + u + "]"
        return u
    return ""

def get_classes(json):
    '''
    recives spell["classes"]
    returns list of classes reducted.
    it does not include subclases
    '''
    try:
        classes = json["fromClassList"]
    except:
        return ""
    

    u = json_extract(classes, "name")
    u = list(dict.fromkeys(u)) # Remove duplicates
    
    if 'Artificer (Revisited)' in u:
        u.remove('Artificer (Revisited)')
        u.append("Artificer")

    u = list(set(u))

    return u 

def get_ritual(json):
    if str(json) != "nan":
        return json.get("ritual", False)
    return False

def get_entries_higher_level(json):
    if str(json) != "nan":
        return read_json(json)
    return ""



def main(df, path):
    for i in tqdm(range(df.index.size)):
        
        spell = df.loc[i] 
        name = spell.get("name").replace("/", " ")
        level = spell.get("level")
        school = schools[spell.get("school").upper()]
        time = spell.get("time")
        spell_range = spell.get("range")
        components = spell.get("components")
        duration = spell.get("duration")
        entries = spell.get("entries")
        classes = spell.get("classes")
        entries_h_l = spell.get("entriesHigherLevel")
        ritual = get_ritual(spell.get("meta"))
        area = get_area(spell.get("areaTags"))

        metadata = "---\n"
        metadata += f"level: {level}\n"
        metadata += f"school: \"{school}\"\n"
        metadata += f"casting_time: {get_casting_time(time)}\n"
        metadata += f"classes: {get_classes(classes)}\n"
        metadata += f"concentration: {get_duration(duration)[1]}\n"
        metadata += f"ritual: {ritual}\n"
        metadata += f"areaTags: {area}\n"
        metadata += "tags: spell\n"
        metadata += "---\n\n"

        text = ""

        text += get_first_header(level, school) + '\n'
        text += f"**Casting Time**:: {get_casting_time(time)}\n"
        text += f"**Range**:: {get_range(spell_range)}\n"
        text += f"**Components**:: {get_components(components)}\n"
        text += f"**Duration**:: {get_duration(duration)[0]}\n"
        text += "\n---\n\n"
        text += read_json(entries)
        text += get_entries_higher_level(entries_h_l) + "\n\n"
        
        with open(path + name + ".md", 'w') as file:
            file.write(metadata)
            file.write(text)



if __name__ == "__main__":

    import os

    path = "D:\\Archivos\\D&D 5e\\Core\\Spells\\"
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)
        print("Directory created")

    df = pd.read_json("data/spells-data.json")

    main(df, path)

    
