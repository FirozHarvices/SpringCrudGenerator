import re
import os


def getMethod(text):
    try:
        a = re.search(r"@PutMapping[\s\S]*@DeleteMapping",text).group(0)
        # print(a)
        return a
    except Exception as e:
        return False

def getModelName(text):
    try:
        return re.search(r"@RequestBody (.*) ",text).group(1)
    except Exception as e:
        return False

def changeMethod(text,method,model):
    method_old = method
    model_s = model[0].lower() + model[1:];
    if(model == False):
        return False
    # print(method + "\n\n"+model_s+"Repository.findBy"+model+"IdAndIsActiveTrue",model_s+"Repository.findBy"+model+"Id"+"\n\n")
    method = method.replace(model_s+"Repository.findBy"+model+"IdAndIsActiveTrue",model_s+"Repository.findBy"+model+"Id")
    return text.replace(method_old,method)

def app():
    for dname, dirs, files in os.walk(input("Constoller Folder Path :- ")):
        for fname in files:
            fpath = os.path.join(dname, fname)
            # print(fpath)
            with open(fpath) as f:
                s = f.read()
            f.close();
            method = getMethod(s)
            if(method != False):
                model = getModelName(method)
                if(model != False):
                    s = changeMethod(s,method,model)
                    if(s != False):
                        with open(fpath, "w+") as f:
                            print("1 == "+fpath +"  //Changed")
                            f.write(s)
                        f.close()
                    else:
                        print("0 == "+fpath+"   //Not Changed")
                        f.close()
                else:
                    print("0 == "+fpath+ "  //Model 404")
            else:
                print("0 == "+fpath+ "  //Method 404")
                f.close()
app()