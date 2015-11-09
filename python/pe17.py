def thousand(x):
    if x < 1000:
        return hundred(x)

    thousand_name = ones(x / 1000)
    x_hund = x % 1000

    if x_hund == 0:
        return thousand_name + 'thousand' 
    else:
        return thousand_name + hundred(x_hund)

def hundred(x):
    if x < 100:
        return tens(x)

    hundred_name = ones(x / 100)
    x_tens = x % 100

    if x_tens == 0:
        return hundred_name + 'hundred'
    else:
        return hundred_name + 'hundred' + 'and' + tens(x_tens)

def tens(x):
    if x < 10:
        return ones(x)

    tens_table = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens_table = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    if x < 20:
        return teens_table[x - 10]
    if x % 10 == 0:
        return tens_table[x / 10]
    return tens_table[x / 10] + ones(x % 10)

def ones(x):
    ones_table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return ones_table[x]

def main():
    ans = 0
    for i in xrange(1, 1001):
        name = thousand(i)
        ans += len(name)
    print ans

if __name__ == '__main__':
    main()
