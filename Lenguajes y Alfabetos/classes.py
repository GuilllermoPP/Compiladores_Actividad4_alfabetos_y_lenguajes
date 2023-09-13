from abc import ABC
from funtions import concatenate_set,power_of_set,star_lock_set,accumulated_power_of_sets
class Set_char(ABC):
    
    set_1=set()
    set_2=set()


    def __init__(self,set_1:set,set_2:set):
        self.set_1=set_1
        self.set_2=set_2

    def union_of_set(self) :
        return self.set_1 | self.set_2

    def difference_of_set(self):
        return self.set_1 - self.set_2
    
    def intersection_of_set(self):
        return self.set_1 & self.set_2
    

class Alphabet(Set_char):
    def star_lock_alphabet(self,n:int):
        return star_lock_set(self.set_1,n,1),star_lock_set(self.set_2,n,1)
        #return  accumulated_power_of_sets(self.set_1,n)

class Language(Set_char):
    def power_of_language(self,n:int):
        return power_of_set(self.set_1,n),power_of_set(self.set_2,n)

    def reverse_of_language(self):
        return set(map(lambda x: x[::-1],self.set_1)),set(map(lambda x: x[::-1],self.set_2))
    
    def concatenate_languages(self):
        return concatenate_set(self.set_1,self.set_2)
    
        
    def language_cardinality(self):
        return len(self.set_1),len(self.set_2)




