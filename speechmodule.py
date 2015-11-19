FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    if not 0 < number < 1000:
        raise ValueError("input must be 0 < n < 1000", number)

    result = [];
    
    hundreds = number // 100
    if hundreds > 0:
        result.append(FIRST_TEN[hundreds - 1])
        result.append(HUNDRED)
        number -= hundreds * 100
    tens = number // 10
    if tens == 1:
        result.append(SECOND_TEN[number % 10])
        number = 0
    elif tens > 1:
        result.append(OTHER_TENS[tens - 2])
        number -= tens * 10
    if number > 0:
        result.append(FIRST_TEN[number - 1])
    
    return " ".join(result)
    
    
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"