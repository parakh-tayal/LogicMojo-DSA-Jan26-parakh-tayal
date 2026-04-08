def place_tiles_1(n,m):
    """
    Approach 1 - Recursion only
    """

    # base cases
    if n == 0:
        return 1   # empty floor, one way to fill (do nothing)
    if n < m:
        return 1   # only horizontal tiles fit, one way
    
    return place_tiles_1(n-1,m) + place_tiles_1(n-m,m)

def place_tiles_2(n,m,memo={}):
    """
    Approach 2 - Recursion with DP
    """

    # base cases
    if n == 0:
        return 1   # empty floor, one way to fill (do nothing)
    if n < m:
        return 1   # only horizontal tiles fit, one way
    
    if n in memo:
        return memo[n]
    
    memo[n] = place_tiles_2(n-1,m,memo) + place_tiles_2(n-m,m,memo)
    return memo[n] 
            
n=4
m=3

# print(place_tiles_1(4, 2))  # 5 ✅
# print(place_tiles_1(3, 2))  # 3 ✅
# print(place_tiles_1(2, 2))  # 2 ✅

print(place_tiles_2(4, 2))  # 5 ✅
print(place_tiles_2(3, 2))  # 3 ✅
print(place_tiles_2(2, 2))  # 2 ✅
