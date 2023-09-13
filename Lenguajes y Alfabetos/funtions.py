import re
import random

LANDA="*"
def concatenate_symbol(a:str,b:str):
    if a==LANDA and b==LANDA:
        return LANDA
    elif a==LANDA and b!=LANDA:
        return b
    elif a!=LANDA and b==LANDA:
        return a
    else:
        return a+b


def concatenate_set(set_1:set(),set_2:set()):
    auxiliary_matriz=list(map(lambda x:list(map(lambda y: concatenate_symbol(x,y), set_2)),set_1))
    return set([value for row in auxiliary_matriz for value in row])

def power_of_set(set_1:set(),n:int):
    if n==1:
        return set_1
    else:
        return concatenate_set(set_1,power_of_set(set_1,n-1))
        
def accumulated_power_of_sets(set_1:set(),n:int):

    if n==1:
        return set_1
    else:    
        return power_of_set(set_1,n)|accumulated_power_of_sets(set_1,n-1)
    

    
def star_lock_set(set_1:set(),n:int,m:int):#al usar esta funcion recursiva la variable "m" siempre tiene que ser 1
    
    if len(accumulated_power_of_sets(set_1,m))>=n:
        auxiliary_set=accumulated_power_of_sets(set_1,m)
        out_set=set()
        while len(out_set)<n:
            out_set.add(auxiliary_set.pop())
        return out_set
    else:
        return star_lock_set(set_1,n,m+1)

def create_sets_from_input(input_text):
    # Usamos una expresión regular para encontrar los conjuntos entre llaves
    sets = re.findall(r'{(.*?)}', input_text)
    
    if len(sets) >= 2:
        # Dividimos los conjuntos 1 y 2
        set_1 = set(sets[0].split(','))
        set_2 = set(sets[1].split(','))
        return set_1, set_2   
    else:
        raise ValueError("Se esperan al menos dos conjuntos entre llaves.")








