def str_to_int(submit=""):
    try:
        submit=input("son kiriting!")
        submited = int(submit)
        print("kiritilgan son_",submited)
    except ValueError:
        print("xato son kiritmadingiz!")

str_to_int()