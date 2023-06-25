from regex import parse_text, footnote_elements
import re 

text = ('', '')
esc = ('', '\n')
esc_2 = ('', '\n\n')
quote = ('>', '')
by = (">\n> \\- _","_\n\n")
entry_name = ('\n**_', '_**. ')
inset_name = ('> [!INFO] ', '\n')
inset_entries = ('>', '')
items = ('- ', '')
item_name = ('- **', '**: ')
itemSub_name = ('\t- ', ': ')
table_caption = ("### ", "\n---\n")
table_element = ("|", "")
table_esc = ("","|\n")


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)


def read_json(obj):
    
    '''
    Reads recursively the entries of a json structure.
    Appends them into a list and formats it

    Recieves json object and returns a parsed text in obsidian format 

    p1 stands for the prefix and suffix of each string element
    p2 stands for the prefix and suffic of each line in list

    '''

    if obj is None:
        return ""

    arr = []
    
    def read(obj, p2=text, **kwargs):
        for key, p1 in kwargs.items():
            extract(obj.get(key), p1=p1, p2=p2)
    
    def read_table(obj):
        read(obj, caption=table_caption)
        read(obj, p2=table_element, colLabels=text)
        arr.append("|\n")
        read_colStyles(obj)
        read(obj, p2=table_esc, rows=table_element)
        footnotes = obj.get("footnotes")
        if footnotes is not None:
            for footnote in footnotes:
                footnote_elements.append(parse_text(footnote).replace("*","").strip())
                n = len(footnote_elements)
                arr.append(f"[^{n}] ")
            

    def read_colStyles(obj):
        styles = obj.get("colStyles")
        if styles is not None:
            for style in styles:
                nums = [int(x) for x in re.findall(r'col-(\d*)', style)]
                arr.append(f"|--{'-'*sum(nums)}")
            arr.append("|\n")
        else:
            for _ in obj.get("colLabels"):
                arr.append("|----")
            arr.append("|\n")

    def read_cell(obj):
        roll = obj.get("roll")
        if roll != None:
            min = roll.get("min")
            max = roll.get("max")
            exact = roll.get("exact")
            if exact != None:
                arr.append(f"|{exact} ")
            elif min and max != None:
                arr.append(f"|{min}-{max} ")        

    def extract(obj, p1=text, p2=text):

        if obj == None:
            return None

        if isinstance(obj, dict):
            type = obj.get("type")

            if type == "entries":
                return read(obj, p2=esc, name=entry_name, entries=text)
            if type == "inset":
                return read(obj, p2=esc, name=inset_name, entries=inset_entries)                
            if type == "quote":
                return read(obj, p2=esc, entries=quote, by=by)
            if type == "inline":
                return read(obj, name=entry_name, entries=text)
            if type == "list":
                arr.append("\n")
                read(obj, p2=esc, items=items)
                return arr.append("\n")
            if type == "item":
                return read(obj, name=item_name, entries=text, entry=text)
            if type == "itemSub":
                return read(obj, name=itemSub_name, entries=text, entry=text)
            if type == "table" or obj.get("__prop") == "table":
                return read_table(obj)
            if type == "tableGroup":
                return read(obj, p2=esc, tables=text)
            if type == "row":
                return read(obj, row=table_element)
            if type == "cell": 
                return read_cell(obj)

            extract(obj.get("entries"), p1)
            extract(obj.get("text"), p1)

        elif isinstance(obj, list):
            for x in obj:
                arr.append(p2[0])
                extract(x, p1=p1)
                arr.append(p2[1])

        else:
            obj = parse_text(obj)
            arr.extend([p1[0], obj, p1[1]])
                        
        return None

    extract(obj, esc_2)
    return "".join(arr)