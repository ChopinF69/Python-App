from domain.domainFilm import Film
from domain.domainClient import Client
from random import *

def generateRandomString(length):
    '''
    Functia va genera un string random de lungime specificata
    :param length: INT
    :return: STRING
    '''
    new_string = ""
    for _ in range(length):
        random_value = randint(ord('a') , ord('z'))
        new_string += random_value

    return new_string

def generateRandomCnp(length):
    '''
    Functia va genera un cnp random de lungime data
    :param length: INT
    :return: INT
    '''

    new_cnp = ""
    for _ in range(length):
        random_value = randint(ord('0') , ord('9'))
        new_cnp += random_value

    return new_cnp

#4. a. Quick sort
#b. Gnome sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def my_sort_1(data, key=lambda x: x, reverse=False):
    data = list(data)  # Convert dict_items to a list
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if key(x) < key(pivot)]
    middle = [x for x in data if key(x) == key(pivot)]
    right = [x for x in data if key(x) > key(pivot)]

    if reverse:
        return my_sort_1(right, key, reverse) + middle + my_sort_1(left, key, reverse)
    else:
        return my_sort_1(left, key, reverse) + middle + my_sort_1(right, key, reverse)

def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i] , arr[i - 1] = arr[i - 1] , arr[i]
            i -= 1

def my_sort_2(arr , key = None , reverse = False):
    arr = list(arr)  # Convert dict_items to a list
    if key == None:
        key = lambda x : x

    i = 0
    while i < len(arr):
        if i == 0 or key(arr[i - 1]) <= key(arr[i]):
            i += 1
        else:
            arr[i] , arr[i - 1] = arr[i - 1] , arr[i]
            i -= 1

    if reverse == True:
        return arr[::-1]
    else:
        return arr

def my_sort_3(arr , key1 = None , key2 = None , reverse = False):
    #vom folosi quick sort
    #aici vreau sa implementez sa sorteze dupa 2 paramatrii
    #primul parametru va fi numarul de filme
    #al doilea va fi numele
    # adica sirul nou va fi sortat dupa numarul de filme si dupa nume
    #primim o lista cu 2 parametrii - nume si cnp , si vom sorta acum dupa nume
    new_arr = []
    for i in range(0 , len(arr)):
        nume = arr[i][0]
        cnp = arr[i][1]
        new_arr.append((nume , cnp))

    for i in range(0 , len(arr)):
        for j in range(i + 1 , len(arr)):
            nume1 = new_arr[i][0]
            nume2 = new_arr[j][0]
            cnp1 = new_arr[i][0]
            cnp2 = new_arr[j][1]

            if(nume1 > nume2):
                new_arr[i] , new_arr[j] = new_arr[j] , new_arr[i]

    if(reverse == True):
        return new_arr[::-1]
    else:
        return new_arr
