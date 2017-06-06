# Me1337 created by Breadinator.

while 1:

    # SET leetification MODE
    leetMode = 'unset'
    while leetMode == 'unset':
        uin0 = input('What leet mode would you like to use? Type \'help\' to see your options.\n> ')
        if uin0 == 'help':
            print('Modes:\n- Bread1337(input \'bread\')\n- Full1337(input \'full\')\n- More coming soon!')
        elif uin0 == 'bread':
            leetMode = 'bread'
            print(leetMode + ' selected!\n')
        elif uin0 == 'full':
            leetMode = 'full'
            print(leetMode + ' selected!\n')
        else:
            print('Unknown mode. Please try again.\n')

    # SET STRING
    string = input('What would you like to leetify?\n> ').lower()
    print('String set!')

    # SPLIT STRING
    splitString = [list(string)]
    print('String split!\n')
    
    # LEEEETIFICATIOOOON!
    leetList = []
    leetString = ''
    for l in splitString:
        for i in l:
            # BREAD LEET
            if leetMode == 'bread':
                if i == 'a':
                    leetList.append('4')
                elif i == 'e':
                    leetList.append('3')
                elif i == 'i':
                    leetList.append('1')
                elif i == 'o':
                    leetList.append('0')
                elif i == 's':
                    leetList.append('5')
                elif i == 't':
                    leetList.append('7')
                else:
                    leetList.append(i)
            # FULL LEET
            elif leetMode == 'full':
                if i == 'a':
                    leetList.append('4 ')
                elif i == 'b':
                    leetList.append('|3 ')
                elif i == 'c':
                    leetList.append('( ')
                elif i == 'd':
                    leetList.append('|) ')
                elif i == 'e':
                    leetList.append('3 ')
                elif i == 'f':
                    leetList.append('|= ')
                elif i == 'g':
                    leetList.append('9 ')
                elif i == 'h':
                    leetList.append('|-| ')
                elif i == 'i':
                    leetList.append('! ')
                elif i == 'j':
                    leetList.append('_| ')
                elif i == 'k':
                    leetList.append('|< ')
                elif i == 'l':
                    leetList.append('|_ ')
                elif i == 'm':
                    leetList.append('/\\\\/\\\\ ')
                elif i == 'n':
                    leetList.append('|\\\\| ')
                elif i == 'o':
                    leetList.append('0 ')
                elif i == 'p':
                    leetList.append('|D ')
                elif i == 'q':
                    leetList.append('q ')
                elif i == 'r':
                    leetList.append('|2 ')
                elif i == 's':
                    leetList.append('5 ')
                elif i == 't':
                    leetList.append('7 ')
                elif i == 'u':
                    leetList.append('(_) ')
                elif i == 'v':
                    leetList.append('\\\\/ ')
                elif i == 'w':
                    leetList.append('\\\\/\\\\/ ')
                elif i == 'x':
                    leetList.append('>< ')
                elif i == 'y':
                    leetList.append('`/ ')
                elif i == 'z':
                    leetList.append('2 ')
                elif i == ' ':
                    leetList.append('\n')
                else:
                    leetList.append(i)
    for i in leetList:
        leetString += i
    print(leetString + '\n')
    
    # ASK IF YOU WANNA DO IT AGAIN BRO
    print('--------------------------------')
    uin1 = input('Would you like to leetify another string? (y/n)\n> ')
    if not uin1 == 'y':
        break
    else:
        print('--------------------------------\n')
