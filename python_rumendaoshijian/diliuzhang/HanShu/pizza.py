'''
def make_pizza(*toppins):
    print(toppins)
make_pizza('hah')
make_pizza('gg','ss','aaa')


def make_pizza(*toppins):
    print("\n enter place :")
    for toppin in toppins:
        print(" - "+toppin)

make_pizza('aa')
make_pizza('dd','bb','cc')

'''
def make_pizz(size,*toppins):
    print("\n enter place : "+str(size) +"tiao liao wei")
    for toppin in toppins:
        print("- "+toppin)

# make_pizz(13,'dd','as','ss')
# make_pizz(18,'ff','fff','aa')



