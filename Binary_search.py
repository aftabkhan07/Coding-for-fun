def binsearch(list2,a):
    
    lower = 0
    upper = len(list2)-1
    
    while lower<=upper:
        mid = (lower+upper)//2
        if list2[mid]==n:
            return True,mid
        else:
            if list2[mid] < n and lower!=mid:
                lower = mid
            else:
                upper = mid
    return False

list1 = [3, 4, 5, 6, 12, 34, 47, 66, 85, 324, 435, 588, 2424]
n = 588

print(binsearch(list1,n))

# Issue with last element of list may be fixed bt changing at line 12 or something








