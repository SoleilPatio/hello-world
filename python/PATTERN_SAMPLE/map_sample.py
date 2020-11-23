


if __name__ == "__main__":
    """
    [CLS]:Do lists subtraction
    """
    A = [1,2,3,4,5]
    B = [2,4,6,8,10]
    
    
    """
    [CLS]:Use default sub() operator
    """
    import operator
    C = map(operator.sub, A, B)
    print C
    
    """
    [CLS]:Use my own function
    """
    def my_sub(a,b):
        return a-b
    
    C = map(my_sub, A, B)
    print C
    
    """
    [CLS]:Use lambda
    """
    C = map(lambda a,b:a-b, A, B)
    print C
    
    
    
    print "\nDone!"
    