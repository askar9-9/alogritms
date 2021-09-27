#список с 4 000 000 цифрами
num = []
for i in range(1,4000000):
    num.append(i)
#бинарный поиск
def binary_search(list,item):
    #мин значение индекса
    low = 0
    #макс значение индекса
    high = len(list)-1 #индекс списка начинается с 0

    #подбирает с макс к мин индексу
    while low<=high:
        mid=(low+high)#index 
        guess = list[mid]
        if guess>item:
            high = mid-1
        elif guess<item:
            low = mid+1
        else:
            return mid
    return None
#загадываем число 3000
print(binary_search(num,2000))  #выводит индекс списка 
print(num[binary_search(num,2000)]) #выводит саму цифру