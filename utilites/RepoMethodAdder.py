import re
import os


def getModelName(text):
    try:
        return re.search(r"\<([A-Za-z0-9_]+)\>",text).group(1) 
    except Exception as e:
        return False

def addMethod(text,model):
    method = "    Optional<${model}> findBy${model}Id(long id);"
    method = method.replace("${model}",model)
    text = text.replace("}" , method + "\n}")
    return text

def app():
    for dname, dirs, files in os.walk(input("Enter Path :- ")):
        for fname in files:
            fpath = os.path.join(dname, fname)
            # print(fpath)
            with open(fpath) as f:
                s = f.read()
            f.close();
            model = getModelName(s)
            if(model != False):
                s = addMethod(s,model)
                with open(fpath, "w+") as f:
                    print("YES == "+fpath)
                    f.write(s)
                    f.close()
            else:
                print("NO == "+fpath)
app()