import sympy as sp


if __name__ == "__main__":
    
    x, y, z = sp.symbols("x y z")
    
    """
    [CLS]: 1 element polynomial of 2 degree, 1 equations
    """
    
    roots = sp.solveset(x**2-x,x)
    print type(roots), roots #{0, 1}  ==> <class 'sympy.sets.sets.FiniteSet'>
    
    roots = sp.solveset(x**2 > x**3,x, domain=sp.S.Reals)
    print type(roots), roots #(-oo, 0) U (0, 1) ==> <class 'sympy.sets.sets.Union'>


    """
    [CLS]:3 elements polynomial of 1 degree, 2 equations
    """
    roots = sp.linsolve([x + y + z - 1, x + y + 2*z - 3 ], (x, y, z))
    print type(roots), roots #{(-y - 1, y, 2)}  ==> <class 'sympy.sets.sets.FiniteSet'>
    
    
    """
    A*x = b Form
    """
    M = sp.Matrix(((1, 1, 1, 1), (1, 1, 2, 3)))
    system = A, b = M[:, :-1], M[:, -1]
    roots = sp.linsolve(system, x, y, z)
    print type(roots), roots #{(-y - 1, y, 2)}  ==> <class 'sympy.sets.sets.FiniteSet'>
    
    
    
    """
    [CLS]:3 elements polynomial of 2 degree, 3 equations
    """
    roots = sp.linsolve([x**2 + y + z - 1, x + y + 2*z - 3, x+y-2*z ], (x, y, z))
    print type(roots), roots #{(5/4, 1/4, 3/4)}  ==> <class 'sympy.sets.sets.FiniteSet'>
    
    
    
    """
    [CLS]:free test
    """
    roots = sp.linsolve([x+y+z-30, x+y-20], (x, y, z))
    print type(roots), roots
    
    
    
    print "\nDone"