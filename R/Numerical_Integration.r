# Numerical_Integration.r
# Date: 28.06.2019. Created by Joshua Simon. 

# Creat some functions you want to integrate
# Example 1:
g <- function(x) {
    return(x^2)
}

# Example 2:
h <- function(x) {
    return(sin(x))
}

# Example 3:
k <- function(x) {
    return(3^(3*x-1))
}

com_simpson <- function(f, a, b, n) {
    # Composite Simpson's rule
    # Integration of function f over interval [a,b] where n is
	# the number of subintervals. Accuracy only depends on the 
	# number of subintervals.

    sum <- 0

    if(a > b) {
        print("ERROR: Lower interval bound a has to be smaller than upper bound b.")
        return(0)
    }
    
    # Step length h
    h <- (b - a) / n

    # Calculate integral value with composite simpson's rule
    for (k in 1:n) {
        x_k <- a + k * h
		x_k1 <- a + (k-1) * h
        
		simpson <- h/6 * ( f(x_k1) + 4* f((x_k1 + x_k)/2) + f(x_k) )
		
        sum <- sum + simpson
    }
    
    return(sum)
}


trapez <- function(f, a, b, n) {
    # Trapezoidal rule
    # Integration of function f over interval [a,b] where n is
    # the number of subintervals. Accuracy only depends on the 
    # number of subintervals. The trapezoidal rule converges 
    # rapidly for periodic functions.

    sum <- 0

    if(a > b) {
        print("ERROR: Lower interval bound a has to be smaller than upper bound b.")
        return(0)
    }

    # Step length h
    h <- (b - a) / n

    # Calculate integral value with trapezoidal rule
    for (k in 1:n-1) {
        sum <- sum + f(a + k*h)
    }

    return(h * (0.5 * f(a) + 0.5 * f(b) + sum))
}

interval_a <- 0.0
interval_b <- 4.0
n <- 100

# Call functions to calculate integral value
# Example 1:
integral_g_1 <- com_simpson(g, interval_a, interval_b, n)
integral_g_2 <- trapez(g, interval_a, interval_b, n)

# Example 2:
integral_h_1 <- com_simpson(h, 0.0, 3.141592654/2.0, 400)
integral_h_2 <- trapez(h, 0.0, 3.141592654/2.0, 100)

# Example 3:
integral_k_1 <- com_simpson(k, 0.0, 2.0, 3)
integral_k_2 <- trapez(k, 0.0, 2.0, 3)
	
# Output
print(paste0("Integral of g(x) over [", interval_a, ",", interval_b, "]"))
print(paste0("Simpson: ", integral_g_1))
print(paste0("Trapez: ", integral_g_2))
print(paste0("Exact value is ", 1/3 * (4*4*4)))
cat("\n")

print(paste0("Integral of g(x) over [0 , pi/2]"))
print(paste0("Simpson: ", integral_h_1))
print(paste0("Trapez: ", integral_h_2))
print(paste0("Exact value is ", -cos(3.141592654/2.) + cos(0.)))
cat("\n")

print(paste0("Integral of k(x) over [0 , 2]"))
print(paste0("Simpson: ", integral_k_1))
print(paste0("Trapez: ", integral_k_2))
print(paste0("Exact value is ", 728/(9 * log(3))))
