import re
import os


def getModelName(text):
    try:
        return re.search(r"@RequestMapping\(Constants\.(.*?)\)",text).group(1) 
    except Exception as e:
        return False

def addAnotation(text,annotation):
    if("_MST" in annotation):
        annotation = annotation.split("_MST",1)[0]
        annotation = annotation + "_MASTER"

    annotationText = "@PreAuthorize(\"hasAnyAuthority('MASTERS','${annotation}')\")"
    annotationText = annotationText.replace("${annotation}",annotation)

    text = text.replace("@RestController", annotationText + "\n@RestController")
    return text

def app():
    for dname, dirs, files in os.walk(input("Enter Path :- ")):
    # for dname, dirs, files in os.walk("./../temp/src/main/java/com/harvices/poslocalapi/controller"):
        for fname in files:
            fpath = os.path.join(dname, fname)
            # print(fpath)
            with open(fpath) as f:
                s = f.read()
            f.close();
            model = getModelName(s)
            if(model == False):
                print("404 model : " + fname)
                model = input("Enter model name manully(n = IGNORE) : ")
            else:
                if("_MST" not in model):
                    print("MODEL : "+model)
                    print("model is not master")
                    model = input("Enter model name manully(n = IGNORE) : ")

            if(model != "n"):
                s = addAnotation(s,model)
                with open(fpath, "w+") as f:
                   print("YES == "+fpath)
                   f.write(s)
                   f.close()
            else:
                print("NO == "+fpath)
            print("--------------------------------------")
app()
