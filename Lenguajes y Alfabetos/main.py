from classes import Alphabet,Language
from funtions import create_sets_from_input
def main():
    text_imput=input('Ingrese dos conjuntos de simbolos formato:"A={a,b,c} B={h,i,k}\n el caranter "*" sera considerado expresion lambda o modulo\n')
    set_1,set_2=create_sets_from_input(text_imput)
    alphabetos=Alphabet(set_1,set_2)
    print("la union de los conjuntos A y B es:\n",alphabetos.union_of_set())
    print("la interseccion de los conjuntos A y B es:\n",alphabetos.intersection_of_set())
    print("la diferencia de los conjuntos A y B es:\n",alphabetos.difference_of_set())
    number_elements=int(input("Ingrese el numero de elementos que se desean generar para ambos conjuntos por medio de la cerradura de estrella\n"))
    language_1,language_2=alphabetos.star_lock_alphabet(number_elements)
    languages=Language(language_1,language_2)
    print("se ha generado el lenguaje A:\n",language_1)
    print("se ha generado el lenguaje B:\n",language_2)
    print("la union de los lenguajes A y B es:\n",languages.union_of_set())
    print("la interseccion de los lenguajes A y B es:\n",languages.intersection_of_set())
    print("la diferencia de los lenguajes A y B es:\n",languages.difference_of_set())
    print("la concatenacion de los lenguajes A y B es:\n",languages.concatenate_languages())
    number_pow=int(input("ingrese la potencia a la que sera elevado los lenjueges\n"))
    pow_language_1,pow_language_2=languages.power_of_language(number_pow)
    
    print(f"la potenia grado{number_pow} del lenguaje A es: \n",pow_language_1)
    print(f"la potenia grado{number_pow} del lenguaje B es: \n",pow_language_2)
    reverse_languaje_1,reverse_languaje_2=languages.reverse_of_language()
    print("La inversa del lenguaje A es:\n",reverse_languaje_1)
    print("La inversa del lenguaje B es:\n",reverse_languaje_2)
    cardinality_language_1,cardinality_language_2=languages.language_cardinality()
    print("La cardinalidad del lenguaje A es:\n",cardinality_language_1)
    print("La cardinalidad del lenguaje B es:\n",cardinality_language_2)

if __name__=='__main__':
    main()