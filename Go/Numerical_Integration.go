package main

import (
	"fmt"
	"math"
)

func main() {
	var interval_a float64 = 0.0 // lower interval bound
	var interval_b float64 = 4.0 // upper interval bound
	var n int = 100              // number of subintervals

	// Call functions to calculate integral value
	// Example 1:
	integral_g_1 := com_simpson(g, interval_a, interval_b, n)
	integral_g_2 := trapez(g, interval_a, interval_b, n)

	// Example 2:
	integral_h_1 := com_simpson(h, 0.00, 3.141592654/2.0, 400)
	integral_h_2 := trapez(h, 0.00, 3.141592654/2.0, 100)

	// Example 3:
	integral_k_1 := com_simpson(k, 0.0, 2.0, 3)
	integral_k_2 := trapez(k, 0.0, 2.0, 3)

	// Output
	fmt.Println("Integral of g(x) over [", interval_a, ",", interval_b, "]")
	fmt.Println("Simpson: ", integral_g_1)
	fmt.Println("Trapez:  ", integral_g_2)
	fmt.Println("Exact value is ", 1.0/3.0*(4.0*4.0*4.0))
	fmt.Println()

	fmt.Println("Integral of h(x) over [0,pi/2]")
	fmt.Println("Simpson: ", integral_h_1)
	fmt.Println("Trapez:  ", integral_h_2)
	fmt.Println("Exact value is ", -math.Cos(3.141592654/2.)+math.Cos(0.))
	fmt.Println()

	fmt.Println("Integral of k(x) over [0, 2]")
	fmt.Println("Simpson: ", integral_k_1)
	fmt.Println("Trapez:  ", integral_k_2)
	fmt.Println("Exact value is ", 728/(9*math.Log(3)))
}

// Create some functions you want to integrate like this:

// Example 1: g(x) = x^2
func g(x float64) float64 {
	return math.Pow(x, 2)
}

// Example 2: h(x) = sin(x)
func h(x float64) float64 {
	return math.Sin(x)
}

// Example 3: k(x) = 3^(3*x-1)
func k(x float64) float64 {
	return math.Pow(3, 3*x-1)
}

// Composite Simpson's rule.
// Integration of function f over interval [a,b] where n is
// the number of subintervals. Accuracy only depends on the
// number of subintervals.
func com_simpson(f func(float64) float64, a float64, b float64, n int) float64 {
	var h float64
	var x_k float64
	var x_k1 float64
	var simpson float64
	var sum float64 = 0.0

	if a > b {
		fmt.Print("ERROR: Lower interval bound a has to be smaller than upper bound b.")
		return 0
	}

	// Step length h
	h = (b - a) / float64(n)

	// Calculate integral value with composite simpson's rule
	for k := 1; k <= n; k++ {
		x_k = a + float64(k)*h
		x_k1 = a + (float64(k)-1.0)*h
		simpson = h / 6 * (f(x_k1) + 4*f((x_k1+x_k)/2) + f(x_k))
		sum = sum + simpson
	}

	return sum
}

// Trapezoidal rule
// Integration of function f over interval [a,b] where n is
// the number of subintervals. Accuracy only depends on the
// number of subintervals. The trapezoidal rule converges
// rapidly for periodic functions.
func trapez(f func(float64) float64, a float64, b float64, n int) float64 {
	var h float64
	var sum float64 = 0.0

	if a > b {
		fmt.Print("ERROR: Lower interval bound a has to be smaller than upper bound b.")
		return 0
	}

	// Step length h
	h = (b - a) / float64(n)

	// Calculate integral value with trapezoidal rule
	for k := 1; k <= n-1; k++ {
		sum = sum + f(a+float64(k)*h)
	}

	return h * (0.5*f(a) + 0.5*f(b) + sum)
}
