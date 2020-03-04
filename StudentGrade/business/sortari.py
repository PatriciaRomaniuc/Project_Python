def InsertionSort(l,*,key,cmp,reversed):
    '''
    Functie ce sorteaza prin insertie o lista
   :param l:
    '''
    for i in range(1,len(l)):
        ind = i-1
        a = l[i]
        while ind>=i-1 and key(l[i]<l[ind]):
            l[ind+1] = l[ind]
            ind = ind-1
        l[ind+1] = a
        
def getNextGap(gap): 
    gap = (gap * 10)/13
    if gap < 1: 
        return 1
    return gap 

def CombSort(l,*,key,cmp,reversed): 
    n = len(l) 
    gap = n 
    swapped = True

    while gap !=1 or swapped == 1: 
        gap = int(getNextGap(gap)) 
        swapped = False
        for i in range(0, int(n-gap)): 
            if key(l[i]) > key(l[i + gap]): 
                l[i], l[i + gap]=l[i + gap], l[i] 
                swapped = True
                
def key_alfabetic(obj):
        return obj.get_student().get_nume()
    
def key_note(obj):
        return obj.get_nota()
