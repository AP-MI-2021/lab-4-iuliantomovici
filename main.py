def afiseaza_daca_nr_e_in_lista_incepand_cu_o_poz(lst,nr,poz):
    '''
    Verifica dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție
    citită de la tastatură
    :param lst: lista de nr intregi
    :param nr: Numarul de cautat
    :param poz:pozitia de la care incepe cautarea
    :return: 1 daca numarul este gasit, 0 daca nu
    '''
    for i in range(poz,len(lst) ):
        if lst[i]==nr:
            return 1
    return 0


def test_afiseaza_daca_nr_e_in_lista_incepand_cu_o_poz():
    assert afiseaza_daca_nr_e_in_lista_incepand_cu_o_poz([1,2,3,4,5],4,2)==1
    assert afiseaza_daca_nr_e_in_lista_incepand_cu_o_poz([1, 2, 3, 4, 5], 2, 4) == 0


def get_suma_nr_pare(lst):
    '''
    Returneaza suma numerelor pare din lista
    :param lst: lista de nr intregi
    :return: suma
    '''
    suma=0
    for x in lst:
        if x%2==0:
            suma=suma+x
    return suma



def test_get_suma_nr_pare():
    assert get_suma_nr_pare([1,2,3,4])==6
    assert get_suma_nr_pare([3, 5]) == 0


def get_lista_nr_pare_fara_duplicate(lst):
    '''
    Afișați toate numere din lista care sunt pare. Daca se repeta un numar, acesta va apărea în
    lista rezultat doar o singura data.
    :param lst: lista de nr intregi
    :return:rez: lista rezultata
    '''
    rez=[]
    for x in lst:
         if (x not in rez)and (x%2==0):
            rez.append(x)
    return rez

def test_get_lista_nr_pare_fara_duplicate():
    assert get_lista_nr_pare_fara_duplicate([2,2,4,4,1,2])==[2,4]
    assert get_lista_nr_pare_fara_duplicate([1,1,3,5]) == []






def meniu():
    print("""
1.Citire date
2.Afișați dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție
citită de la tastatură.
3.Afișați suma tuturor numerelor întregi pare din lista.
4.Afișați toate numere din lista care sunt pare. Daca se repeta un numar, acesta va apărea în
lista rezultat doar o singura data.
5.Afișați lista obținută prin înlocuirea fiecărui număr cu un tuplu format din două numere de pe
poziții distincte din listă care adunate dau acel număr, dacă se poate.
x. Iesire
""")


def citire(n):
    lst=[]
    for i in range(0,n):
        p=int(input("introduceti elemntul"))
        lst.append(p)
    return lst


def teste():
    test_afiseaza_daca_nr_e_in_lista_incepand_cu_o_poz()
    test_get_suma_nr_pare()
    test_get_lista_nr_pare_fara_duplicate()



def main():
    lst=[]
    teste()
    while True:
        meniu()
        cmd=input("introduceti comanda: ")
        if cmd=='1':
            n=int(input("cate numere sa fie in lista? "))
            lst=citire(n)
        elif cmd=='2':
            nr=int(input("dati numarul de cautat: "))
            poz=int(input("dati pozitia de la care incepe cautarea:" ))
            if afiseaza_daca_nr_e_in_lista_incepand_cu_o_poz(lst,nr,poz)==1:
                print("DA")
            else:
                print("NU")
        elif cmd=='3':
           print(get_suma_nr_pare(lst))
        elif cmd=='4':
            print(get_lista_nr_pare_fara_duplicate(lst))
        elif cmd=='5':
            pass
        elif cmd=='x':
            break
        else:
            print("comanda invalida")


if __name__ == '__main__':main()