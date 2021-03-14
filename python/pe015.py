def binom(n, r):
    """Calculate n choose r, or n!/(r!(n-r)!)"""
    ans = 1
    denom = 2
    for i in xrange(r+1, n+1): 
        ans *= i
        if denom <= n-r and ans % denom == 0:
            ans /= denom
            denom += 1
    return ans


print binom(40, 20)
