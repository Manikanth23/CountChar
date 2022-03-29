def count_characters(m):
    count = {}
    for i in m:
        if i in count:   
            count[i] += 1 #if char is there count will be incremented
        else:
            count[i] = 1
    print(count)
print(count_characters("ManikanthManikanth"))