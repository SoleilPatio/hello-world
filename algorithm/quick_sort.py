

def quicksort(a_list, start, end):
    
    if start > end:
        return
    
    pivot = a_list[start]
    left = start+1
    right = end
    
    
    while True:
        while left <= right and a_list[left] <= pivot:
            left += 1
        while right >= left and a_list[right] >= pivot:
            right -= 1
        if left > right:
            break
        #swap
        temp = a_list[left]
        a_list[left] = a_list[right]
        a_list[right] = temp
        
    
    #swap pivot with right
    temp = a_list[start]
    a_list[start] = a_list[right]
    a_list[right] = temp
    pivot = right
    
    quicksort(a_list, start, pivot-1)
    quicksort(a_list, pivot+1, end)
            
        
def main_quick_sort():
    import numpy as np
    a_list = [2,5,7,3,6,9,0,1]
    a_list = np.random.randint(20,size=20)
    print a_list
    quicksort(a_list, 0, len(a_list)-1)
    
    print a_list
        
    


if __name__ == "__main__":
    main_quick_sort()
    
    print "\nDone\n"
    
    
    
    
    