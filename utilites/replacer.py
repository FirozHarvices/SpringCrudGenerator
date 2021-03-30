import os
import re
codes = [
    {
        'Bpc': 'Customer',
        'bpc': 'customer',
        "BPC_": 'CUSTOMER_',
        "BPC": "customer"
    },
    {
        "Bp":"Outlet",
        "bp":"outlet",
        "BP_":"OUTLET_",
        "BP":"outlet"
    },
    {
        "Bom":"Recipe",
        "bom":"recipe",
        "BOM_":"RECIPE_",
        "BOM":"recipe"
    }
]
def replace(text, table):
    rc = re.compile('|'.join(map(re.escape, table)))
    def translate(match):
        return table[match.group(0)]
    return rc.sub(translate, text)

def app():
    for dname, dirs, files in os.walk(input("enter directory path")):
        for fname in files:
            fpath = os.path.join(dname, fname)
            print(fpath)
            with open(fpath) as f:
                s = f.read()
            f.close();
            os.remove(fpath)
            for code in codes:
                s = replace(s,code)
                fpath = replace(fpath,code)
            with open(fpath, "w+") as f:
                f.write(s)
app()