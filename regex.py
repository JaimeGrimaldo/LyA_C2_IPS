def Signos(char):
    return char == '*' or char == '+' or char == 'U'

def DetectarCaracter(char):
    return char.isalpha() or char.isdigit()

def SplitRegex(regex):
    posRegex = 0
    operador = None
    res = None
    guardar = None
    
    if regex[0] == '(':
        posRegex = regex.find(')') + 1
        guardar = regex[:posRegex]
    else:
        posRegex = 1
        guardar = regex[0]
    if posRegex < len(regex) and Signos(regex[posRegex]):
        operador = regex[posRegex]
        posRegex += 1
    res = regex[posRegex:]
    
    return guardar, operador, res

def SaberCaracter(dato):
    return DetectarCaracter(dato[0])

def Existe(regex, string):
    head, operator, rest = SplitRegex(regex)
    if len(string) == 0:
        return False
    if DetectarCaracter(head):
        return regex[0] == string[0]
    return False

def SaberRegex(regex, string, tam, tamMin=None, maxTam=None):
    inicio, opera, res = SplitRegex(regex)
    if not tamMin:
        tamMin = 0
  
    subtam = -1
    while not maxTam or (subtam < maxTam):
        [subexpr_matched, subexpr_length] = SaberSigno(
            (inicio * (subtam + 1)), string, tam
        )

        if subexpr_matched:
            subtam += 1
        else:
            break
        
    while subtam >= tamMin:
        [matched, new_tam] = SaberSigno(
            (inicio * subtam) + res, string, tam
        )
        if matched:
            return [matched, new_tam]
        subtam -= 1
    return [False, None]

def SplitUnicion(union):
    return union[1:-1].split('∪')

def SaberRegexUnion(regex, string, tamanio):
    guardar, operador, res = SplitRegex(regex)
    unions = SplitUnicion(guardar)
    for uniones in unions:
        [coin, tamCoin] = SaberSigno(
            uniones + res, string, tamanio
        )
        if coin:
            return [coin, tamCoin]
    return [False, None] 

def Unicion(dato):
    return dato[0] == '(' and dato[-1] == ')'

def SaberSigno(regex, string, tam=0):
    if len(regex) == 0:
        return [True, tam]
    head, operator, rest = SplitRegex(regex)
    if operator == '*':
        return SaberRegex(regex, string, tam)
    elif operator == '+':
        return SaberRegex(regex, string, tam,min_tam= 1)                
    elif Unicion(head):
        return SaberRegexUnion(regex, string, tam)
    elif SaberCaracter(head):     
        if Existe(regex, string):
            return SaberSigno(rest, string[1:], tam + 1)
    else:
        print(f'Caracter desconocido {regex}.')
    return [False, None]


def Coincide(regex, string):
    posCoincide = 0
    bandera = False
    
    while not bandera and posCoincide == 0:
        [coincide, tamCoincide] = SaberSigno(regex, string[posCoincide:])
        if coincide and tamCoincide == len(string):
            return coincide
        posCoincide += 1
    return False
   

def main():
    regex = '(0+1)* |'
    string = '011'
    regex = regex.replace('.','').replace('^*','*').replace('+','∪').replace('^∪','+').replace(' ','')
    Coincideed = Coincide(regex, string)
    if Coincideed:
        print(f'La cadena {string} es válida para la expresión regular.')
    else:
        print(f'La cadena {string} NO es válida para la expresión regular.')


if __name__ == '__main__':
    main()