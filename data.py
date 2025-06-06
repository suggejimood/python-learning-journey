list = [1, 2, 3, 7, 6]

list.append(4) #sonuna değer ekler O(1)
list.insert(2, 100) #2 konumuna 100 ekledi O(n)
list.extend([4, 8]) #listeye ekledi O(k)
list.pop() #son elemanı çıkardı O(1)
list.pop(1) #seçili indexi çıkardı O(n)
list.remove(1) #Seçili değeri çıkardı O(n)
list.clear() #Listeyi temizler O(1)
list.reverse() #Listeyi terse çevirir O(n)
list.sort() #Listeyi sıralar O(n logn)
list.index(3) #İlk bulunduğu indexi döner O(n)
list.count(7) #Verilen değerden kaç tane olduğunu sayar O(n)
list.copy() #Shallow coppy O(n)

tuple = (1, 2, 3, 3, 6, 9)

tuple.count(3) #bu değerden kaç tane olduğunu sayar O(n)
tuple.index(6) #Verilen değerin ilk indexini döner O(n)

set = {1, 3, 6, 9, 5}

set.add(4) #Değeri ekler O(1)
set.remove(4) #Değeri siler O(1)
set.pop() #Rastgele siler O(1)
set.clear() #Seti tamamen temizler O(1)
set.union({1, 3, 9, 0, 3}) # Setleri birleştirir O(n)
set.intersection({3,1,4}) #Kesişimleri bulur O(n)
set.difference({12, 5, 7}) #Farklerı bulur O(n)