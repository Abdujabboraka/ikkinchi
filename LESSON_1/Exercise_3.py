import json
def mahsulotlar(nomi="", narxi=0.0, rangi="",soni=0):
    try:nomi=str(input("nomi>>>"))
    except:print("nomi matnli")
    try:narxi =float(input("narxi>>>"))
    except: print("narxi float")
    try: rangi=input("rangi>>>")
    except:print("rangi matnli")
    try:  soni=int(input("soni>>>"))
    except: print("soni raqamli")


    dict_mahsulot = {"nomi":nomi,"narxi":narxi,"rangi":rangi,"soni":soni}

    json_mahsulotlar ="dict_mahsulot.json"

    with open("mahsulotlar.json", "w") as file:
        json.dump(dict_mahsulot,file,indent=4)


mahsulotlar()