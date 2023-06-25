import re


missing_elements = []
def print_missing_elements(): # Can be used after finishing 
    print(set(missing_elements))


footnote_elements = []
def get_footnote(): # Needs to be applied at the end of the markdown file
    if len(footnote_elements) == 0:
        return ""
    else:
        footnote = "\n\n"
        for i, element in enumerate(footnote_elements):
            footnote += f"[^{i+1}]: {element}\n"
        footnote_elements.clear() 
        return footnote

name_format = {"/":" ", "\\":" ", ":":" ", "*":"", "?":"", "\"":"", "<":" ", ">":" ", "|":" "}
def format(text):
    if any(char in name_format for char in text):
        for i, j in name_format.items():
            text = text.replace(i, j)
    return text


def parse_text(data):
    '''
    Uses regex to find tags in text
    and changes them to obsdian format
    '''
    regex1 = r"{@(italic|bold|note|i |b|comic)\s*((?:(?:{)(?:(?:{)[^}]*}|[^}])*}|[^}])*)}"
    regex2 = r"\{\@(?P<tag>\w+)\s(?P<info>[^\|}]+)\|*(?P<source>(?:[^\|}]*|\0*))\|*(?P<alias>(?:[^\|}]*|\0*))\|*(?P<misc1>(?:[^\|}]*|\0*))\|*(?P<misc2>(?:[^\|}]*|\0*))\}"


    def first_parse(txt): # First looks for bold or italic characters
        txt = txt.replace("*", "* ") #So it does not bold the next text
        matches = re.finditer(regex1, txt)
        u = ""
        j = 0
        for match in matches:
            i = match.start()
            u += txt[j:i]
            groups = match.groups()
            tag, info = groups
            s = ""
            if tag in ("i ", "italic", "note", "comic"):
                s = f"_{info}_"
                
            elif tag in ("b ", "bold"):
                s = f"**{info}**"
            
            u += s
            j = match.end()
        
        u += txt[j:]
        return u
            

    def regex_search(txt): # looks for more general tags
        matches = re.finditer(regex2, txt)
        u = ""
        j = 0
        for match in matches:
            i = match.start()
            u += txt[j:i]
            group_dict = match.groupdict()
            tag = group_dict["tag"]
            info = group_dict["info"]
            source = group_dict["source"]
            alias = group_dict["alias"]
            #misc1 = group_dict["misc1"]
            #misc2 = group_dict["misc2"]

            s = ""      
            if tag in ("creature", "condition", "spell", "item", "skill",
                     "quickref", "sense", "action", "race", "disease", 
                     "language", "class", "variantrule", "trap", "hazard", 
                     "vehupgrade", "background", "feat", "vehicle"):
                info = format(info)
                if alias != "":
                    s = f"[[{info} \\|{alias}]]"
                else:
                    s = f"[[{info}]]"
            elif tag in ("filter","loader", "color", "deity", "5etools", "area", "book"):
                s = info
            elif tag in ("dice", "damage", "hit"):
                s = "**"+info+"**"
            elif tag in ("scaledamage", "scaledice"):
                s = "**"+alias+"**"
            elif tag == "chance":
                s = info + " percent" 
            elif tag == "adventure": #{@adventure Info adventure|source|chapter|chapter name}
                s = f"{info} ({source})"
            elif tag == "d20":
                s = f"+{info}"
            elif tag == "dc":
                s = f"DC {info}"
            elif tag in ("classFeature","table","subclassFeature"):
                info = format(info)
                s = f"[[{info}]]"
            elif tag == "footnote":
                footnote_elements.append(parse_text(source))
                n = len(footnote_elements)
                s = f"{info} [^{n}]"
            elif tag == "atk":
                pass
            elif tag == "link": 
                info = format(info)
                s = f"[{info}]({source})"
            elif tag == "recharge":
                if bool(info) != False:
                    s = f"(Recharge {info}-6)"
                else:
                    s = "(Recharge 6)"

            else:
                missing_elements.append(tag)
            
            u += s
            j = match.end() # {@tag text} position of j is one ahead  
        
        u += txt[j:]
        return u
        
    txt = first_parse(str(data))
    return regex_search(txt)
