import re
import os

def addImport(text):
    text = text.replace("import org.springframework.beans.factory.annotation.Autowired;", "import org.springframework.beans.factory.annotation.Autowired;" + "\nimport org.springframework.security.access.prepost.PreAuthorize;")
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
        
            s = addImport(s)
            with open(fpath, "w+") as f:
               print("YES == "+fpath)
               f.write(s)
               f.close()
            print("--------------------------------------")
app()
