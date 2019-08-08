# Numerical_Integration.py

import numpy as np 

# Test function 1
def g (x):
  return x**2

# Test function 2
def h (x):
  return np.sin(x)

# Test function 3
def k (x):
  return 3**(3*x-1)

# Composite Simpson's rule
def com_simpson(function, a, b, n):
  sum1 = 0.0
  h = (b-a)/n

  for k in range(1,n+1):
    x_k = a + k * h
    x_k1 = a + (k - 1) * h

    simpson = h/6 * ( function(x_k1) + 4* function((x_k1 + x_k)/2) + function(x_k))
		
    sum1 = sum1 + simpson

  return sum1


# Trapezoidal rule
def trapez(function, a, b, n):
  sum2 = 0.0
  h = (b - a) / n

  for k in range(1,n-1):
    sum2 = sum2 + function(a + k*h)

  return h * (0.5 * function(a) + 0.5 * function(b) + sum2)



interval_a = 0       # Lower interval bound 
interval_b = 4       # Upper interval bound
n = 100              # Number of subintervals

# Call functions to calculate integral value
# Example 1:
integral_g_1 = com_simpson(g, interval_a, interval_b, n)
integral_g_2 = trapez(g, interval_a, interval_b, n)

# Example 2:
integral_h_1 = com_simpson(h, 0.00, 3.141592654/2.0, 400)
integral_h_2 = trapez(h, 0.00, 3.141592654/2.0, 100)

# Example 3:
integral_k_1 = com_simpson(k, 0.00, 2.0, 3)
integral_k_2 = trapez(k, 0.00, 2.0, 3)

# Output
print("Integral of g(x) over [", interval_a, " , ", interval_b, "]")
print("Simpson: ", integral_g_1)
print("Trapez: ", integral_g_2)
print("Exact value is ", 1/3 * (4*4*4))
print()

print("Integral of g(x) over [0 , pi/2]")
print("Simpson: ", integral_h_1)
print("Trapez: ", integral_h_2)
print("Exact value is ", -1 * np.cos(3.141592654/2.) + np.cos(0.))
print()

print("Integral of k(x) over [0 , 2]")
print("Simpson: ", integral_k_1)
print("Trapez: ", integral_k_2)
print("Exact value is ", 728/(9 * np.log(3)))
