
# coding: utf-8

# The algorithm for this code is inspired to this one: https://www.youtube.com/watch?v=373FUw-2U2k

# In[6]:


def hammingEncoder(bin_input):
    '''function to return the hamming code of a binary string.
    gets as argument a binary string and return it's hamming code
    '''
    # check if the argument is a valid binary string
    set_input = set(bin_input)
    for c in set_input:
        if c not in ("0","1"):
            return 'Error: Input must be binary!'

    # add '00' at the start of the string (the first 2 bits are always checkbits)
    input_plus2 = '00' + bin_input
    # get the new string and add a '0' every power of 2 position number (4,8,16...)
    newstring = ''
    if len(input_plus2) >= 4:
        i=4
        while i <= len(input_plus2):
            if i == 4:
                newstring = input_plus2[:i-1] + '0' + input_plus2[i-1:]
            else:
                newstring = newstring[:i-1] + '0' + newstring[i-1:]
            i *= 2
    
    # get the parity check of each checkbit
    # parity check of n checkbit = get n, skip n etc.
    # e.g. if newstring = '0010100' "parity check for checkbit n.2 = '0100'
    check = 1
    parity_list = []
    while check <= len(newstring):
        lst = []
        for i in range(check-1, len(newstring), 2*check):
            lst.append(newstring[i:i+check])
        check *= 2
        parity_list.append(''.join(lst))
        
    # for each parity bit, check the checkbit:
    # 1 if the number of 1 is odd, 0 is they are even
    checkbits = []
    for parity in parity_list:
        n = parity.count('1')
        if n % 2 == 0:
            checkbits.append('0')
        else:
            checkbits.append('1')
      
    # insert the checkbits in the appropriate position in the newstring to form the hamming code
    hamming_list = []
    count_check = 0
    for i in range(1,len(newstring)+1):
        if i == 1 or i == 2:
            hamming_list.append(checkbits[count_check])
            count_check += 1
        elif ((i & (i - 1)) == 0) and i != 0:
            hamming_list.append(checkbits[count_check])
            count_check += 1
        else:
            hamming_list.append(newstring[i-1])
        
            
    hamming = (''.join(hamming_list)) 

    return hamming


# In[8]:


print(hammingEncoder('01001111'))

