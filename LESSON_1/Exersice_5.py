def writer(satrlar:list =["Python oddiy, yetarli, va yuqori darajada o'rganishga mos til. Uni foydalanish zud vaqt oldin yozib ko'rish mumkin. Bunday sintaksisga ega, modul va paketlari o'rnating va boshqa, yaxshi maslahat berish "]):
    with open("index.txt","w") as index:
        index.write(satrlar[0])
writer()

