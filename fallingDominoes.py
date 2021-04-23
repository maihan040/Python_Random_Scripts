#falling_dominoes.py
#
#purpose: Given a string, representing falling dominoes, where "L" indicates the given piece is falling to the left, 
#         "R" indicates the given piece is falling to the right, and "." indicates the piece is still standing
#         write a function that will show the final directions of all the dominoes. 
#         I.e: 
#         I/P = "..L...R..L.."
#         O/P = "LLL...RRLL..""
#
#date: 10/20/20
#
#version: 1.0
#

#############################################################
#                   method definition                       #
#############################################################
def falling_dominoes(dominoes):

    #validate the input 
    if len(dominoes) <= 1: 
        return dominoes
    
    #create an array that only holds the dominoes which are falling
    # (either to the left or the right), as well as their position
    falling = [(i, j) for i, j in enumerate(dominoes) if j in "LR"]
   
    #since strings can't be mutated, copy the contents to a list 
    list_dominoes = list(dominoes)

    #iterate through each tuple inside the "falling" list
    #and compare the current falling domino along with its 
    #right neighbor. 
    #
    #there can only be the following combinations:
    #
    # L.R -> L.R
    # R.L -> R.L
    # L.L -> LLL
    # R.R -> RRR
    # ..L -> LLL
    # R.. -> RRR
    for d in range(len(falling) - 1):
        
        #variable to compare the current falling domino 
        #with its adjacent right one
        pair = falling[d][1] + falling[d+1][1]

        #check for each possible scenario 
        if pair == 'LR':
            continue 

        #variables to indicate start and end positions 
        #for the given pair of neighboors. The slots between
        # these would potentially have to be processed 
        s = falling[d][0] + 1
        e = falling[d+1][0] - 1

        if pair == 'RL':
            while s < e:
                list_dominoes[s] = 'R'
                list_dominoes[e] = 'L'
                s += 1
                e -= 1
        elif pair == 'RR':
            while s < e: 
                list_dominoes[s] = 'R'
                s += 1
        else: 
            while s < e: 
                list_dominoes[s] = 'L'
                s += 1
       
    #process the beginning of the string only if the first falling
    #domino is "L"
    if(falling[0][1] == 'L'):
        for i in range(falling[0][0]):
            list_dominoes[i] = 'L'

    #process the end of the string only if the last falling 
    #domino is "R"
    if(falling[-1][1] == 'R'):
        for i in range(falling[-1][0], len(dominoes)):
            list_dominoes[i] = 'R'
    
    #convert the list back to a string and return it 
    return ''.join(list_dominoes)

#############################################################
#                       main method                         #
#############################################################

#local variables 
ip_string = "R.L.R.L"

#display to user 
print("Processing : " + ip_string)

#call the method
op_string = falling_dominoes(ip_string)

#display result
print("Output is : " + op_string)