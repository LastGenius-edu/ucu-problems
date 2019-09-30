def snail(snail_map):
    #declare array for "snailed" result
    result = []
    
    #if empty, return nothing
    if len(snail_map) == 0:
        return result
    
    #declaring start and end points
    r_s = 0
    r_e = len(snail_map) - 1
    c_s = 0
    c_e = len(snail_map[0]) - 1
    
    #see if we are not trying to find nothing
    while r_s <= r_e and c_s <= c_e:
        
        #looping through top row
        for i in range(c_s, c_e+1):
            result.append(snail_map[r_s][i])
        #erasing it for the future looping
        r_s += 1
        
        #looping though right column
        for i in range(r_s, r_e+1):
            result.append(snail_map[i][c_e])
        #erasing it for the future looping
        c_e -= 1

        #looping through down row
        for i in range(c_e, c_s-1, -1):
                result.append(snail_map[r_e][i])
        #erasing it for the future looping
        r_e -= 1
        
        #looping through left column
        for i in range(r_e, r_s-1, -1):
                result.append(snail_map[i][c_s])
        #erasing it for the future looping
        c_s += 1

    return result

#declare array
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

#print "snailed" array
print(snail(array))
