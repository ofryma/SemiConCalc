arr = [11,45,66,77,32,2,56,79,15,16,33,87,92,45,938,627,22,1354,54,33,2346,1463,1655,6546,88,12,12,57,324,673,76453,9993]
count = 0


def findBest(arr,i,j):

    if arr[i] > arr[j]:
        return arr
    else:
        arr = swap(arr, i, j)
        return arr
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    return arr
def checkOreder(arr,count):
    for i in range(0,len(arr)-1):
        count =  count + 1
        if arr[i] < arr[i+1]:
            return True , count

    return False , count

s = arr[0]
l = arr[0]

while  True:
    check , count = checkOreder(arr, count)
    if check == False:
        break

    for i in range(0,len(arr)-1):
        count +=1
        if arr[i] > l:
            l = arr[i]
        if arr[i] < s:
            s = arr[i]
        arr = findBest(arr,i,i+1)


    print(f"{arr} smallest: {s} largest: {l} count: {count}")




