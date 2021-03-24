from sympy import plot_implicit, symbols, Eq, And
x, y = symbols('x y')
p=plot_implicit(y+1.5*x-3>=0)