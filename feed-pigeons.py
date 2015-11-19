def checkio(number):
    
    pigeons = 0
    fed = 0
    min = 0
    
    while number > 0:
        min += 1
        pigeons += min
        fed += (pigeons - fed 
                    if number >= pigeons 
                    else number - fed 
                        if number >= fed 
                        else 0)
        number -= pigeons
        
    return fed


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"