from regex import *
from parse_json import *
import requests, os 

# headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36' }
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

def check_directory(path):
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print("Directory created")


def request_img(link, name):
    u = ""
    try:
        if requests.get(link + name + ".jpg", headers=headers).status_code == 200:
            u = link + name + ".jpg"
            return u

        elif requests.get(link + name + ".webp", headers=headers).status_code == 200:
            u = link + name + ".webp"
            return u

        elif requests.get(link + name + ".png", headers=headers).status_code == 200:
            u = link + name + ".png" 
            return u
    except:
        pass

    return u


def request_internal_img(link, name):
    
    if os.path.exists((link + name + ".jpg").replace("%20"," ")):
        return link + name + ".jpg"
    if os.path.exists((link + name + ".png").replace("%20"," ")):
        return link + name + ".png"
    if os.path.exists((link + name + ".webp").replace("%20"," ")):
        return link + name + ".webp"
    
    return ""