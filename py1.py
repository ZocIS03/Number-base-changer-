while True:
    in_data = str(input('Liczba Do Skonwertowania: '))
    system = str(input('System Zapisu: '))
    allowed = ['0','1','2','3','4','5','6','7','8','9']
    out_s_input = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'
    out_s = list(out_s_input)
    l_end = []
    s_end = ''
    number = ''
    data = list(in_data)

    
    for i in range(len(in_data)):
        for o in range(len(allowed)):
            if data[i] == allowed[o]:
                l_end = l_end + list(data[i])
    for i in range(len(l_end)):
        number = str(number) + str(l_end[i])
        
    l_end = []
    data = list(system)
    
    for i in range(len(system)):
        for o in range(len(allowed)):
            if data[i] == allowed[o]:
                l_end = l_end + list(data[i])

    system = ''
                
    for i in range(len(l_end)):
        system = str(system) + str(l_end[i])

    if number == '' or system == '':
        break

    number = int(number)
    system = int(system)

    for i in range(20):
        n=0
        for o in range(system):
        
            if number > (system**(19-i))-1:
                number = number - system**(19-i)
                n += 1

        s_end = s_end + out_s[n]

    print(s_end)

print('nice')
exit()
                
