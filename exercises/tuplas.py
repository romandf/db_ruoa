# frutas = (("manzana","roja", "madura"),
#           ("pera","verde","verde"),
#           ("guayaba","amarilla","podrida"),
#           ("pinnaple","verde","dura"))

def data_fam(**kwargs):
    print( kwargs)

data_fam(fruta="manzana", color="amarilla", estado="podrida")

def data(*args):
    # print(args)
    # print(len(args))
    for i,value in enumerate(args):
        for va in value:
            va += va
        return va
    

data(2,4,5)
    