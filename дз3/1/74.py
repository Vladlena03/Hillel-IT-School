def common_elements():
    numbers_3 = set(range( 0 , 100 , 3))
    numbers_5 = set(range( 0, 100 , 5))
    result= numbers_3 & numbers_5
    return result
print(common_elements())
