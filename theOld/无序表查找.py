def sequential_search(slist,key):
    for i in xrange(len(slist)):
        if slist[i] == key:
            return i
        else:
            return -1

    sindex = sequential_search([1,3,5,6,8,4,2,5,4,8,5])
    print(sindex)
