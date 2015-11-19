class checkio:
    """
        answer to anything class
    """
    
    def __init__(self, other): pass
    def __eq__(self, other): return True
    
    __ne__ = __lt__= __le__ = __gt__ = __ge__ = __eq__
    

    
if __name__ == '__main__':
    import re, math
    
    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'
    
    print('NO WAY :(')
