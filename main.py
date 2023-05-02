def black_hole(*args):
    print(type(args))
    print(args)
    for argument in args:
        print(argument)
black_hole(256, 'Name', 'adress', '2*5', 2 * 5)


def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for ag in kwargs:
        print(ag)
black_hole_named(name = "Nick", planet = "Earth", galaxy = "Milky way", age = "bagato")



def black_hole_name(var_1, *args, var_2=2,**kwargs):
    if not args:
        return 0
    for ar in args:
        print(ar)
    for ag,val in kwargs.items():
        print(ag,':',val)
    print(var_1,var_2)
black_hole_name(1,2,3, True, name = "Nick", planet = "Earth", galaxy = "Milky way", age = "bagato")

lst = [6,43,4]
dict = { 'a' : 1, 'b': 2, 'c' : 3}
def fun(var_1,var_2,var_3):
    print(var_1, var_2, var_3)
fun(*lst)

def dic(a,b,c):
    print(a,b,c)
dic(**dict)




lst_1 = [77]
dict_1 = {'var_3': 3,'var_4': 64}
def some(var_1,var_2,var_3,var_4):
    print(var_1,var_2,var_3,var_4)
some(6,*lst_1,**dict_1)

