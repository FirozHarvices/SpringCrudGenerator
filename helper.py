import re
import os
import json


def shortCodeParser(text, wordDic):
    rc = re.compile('|'.join(map(re.escape, wordDic)))

    def translate(match):
        return replace(wordDic[match.group(0)], '"', '\\"', True)
    return rc.sub(translate, text)


def toCamelCase(word, first=False):
    components = ""
    if(first):
        components = ''.join(x.capitalize() or '_' for x in word.split('_'))
    else:
        components = word.split('_')
        components = components[0] + ''.join(x.title() for x in components[1:])
    components = replace(components, "Mst", "MST", True)
    components = replace(components, "Dtl", "DTL", True)
    components = replace(components, "Trx", "TRX", True)
    return components


def toSnakeCase(word):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()

def toLowerCase(word):
    return word.lower()

def toUpperCase(word):
    return word.upper()

def replace(w, s, d, litral=False):
    if(litral):
        return w.replace(s, d)
    return w.replace("${"+s+"}", d)


def transform(field, find, func):
    matches = re.findall(r'\$'+ find +r'{(.*?)\}',field)
    for match in matches:
        withBraces = "$"+find+"{"+match+"}"
        field = replace(field , withBraces , func(match) , True)
    return field
    # if(x is not None):
    #     adasd = x.group()
    #     adasad = re.search(r'\{(.*?)\}',x.group())
    #     val = re.search(r'\{(.*?)\}',x.group()).group(1)
    #     return replace(field , x.group() ,func(val), True )
    # else:
    #     return field


def joinStrings(stringList):
    return ''.join(string for string in stringList)


def writeFile(name, content):
    name = "output/"+name
    os.makedirs(os.path.dirname(name), exist_ok=True)
    with open(name, "w") as f:
        f.write(content)
        f.close()


def readFile(path, fail=False):
    if(os.path.isfile(path)):
        return open(path).read()
    if(fail):
        raise Exception("file at "+path+" not exists")
    return ""


def convertToJson(str, fail):
    try:
        return json.loads(str)
    except:
        if(fail):
            raise Exception("failed json conversion")
        return {}


def convertToStr(str, fail):
    try:
        return json.loads(str)
    except:
        if(fail):
            raise Exception("failed json conversion")
        return {}


def arrayJoin(arr, prefix, postfix, delimiter="\n"):
    return delimiter.join(map(lambda x: prefix + x + postfix, arr))
