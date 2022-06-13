/*
Compile and run this program with:
scalac numericalIntegration.scala && scala numericalIntegration.scala
*/

object NumericIntegration:
    def simpson(fun: Double => Double, a: Double, b: Double, n: Int): Double =
        def quadrature(fun: Double => Double, k: Int, h: Double): Double =
            val xk = a + k * h
            val xk1 = a + (k - 1) * h
            h / 6 * (fun(xk1) + 4 * fun((xk1 + xk) / 2) + fun(xk))

        val h = (b - a) / n
        (1 to n).map((k) => quadrature(fun, k, h)).sum


    def trapez(fun: Double => Double, a: Double, b: Double, n: Int): Double =
        val h = (b - a) / n
        val integral = (1 to n-1).map((k) => fun(a + k * h)).sum
        h * (0.5 * fun(a) + 0.5 * fun(b) + integral)


    def main(args: Array[String]): Unit =
        val aInterval = 0       // Lower interval bound 
        val bInterval = 4       // Upper interval bound
        val n = 100             // Number of subintervals

        // Call functions to calculate integral value
        // Example 1:
        val integral_g_1 = simpson(x => x*x, aInterval, bInterval, n)
        val integral_g_2 = trapez(x => x*x, aInterval, bInterval, n)

        // Example 2:
        val integral_h_1 = simpson(scala.math.sin, 0.00, scala.math.Pi / 2.0, n)
        val integral_h_2 = trapez(scala.math.sin, 0.00, scala.math.Pi / 2.0, n)

        // Output
        println(s"Integral of g(x) over [$aInterval, $bInterval]")
        println(s"Simpson: $integral_g_1")
        println(s"Trapez: $integral_g_2")
        println(s"Exact value is ${1/3 * (4 * 4 * 4)} \n")

        println("Integral of g(x) over [0, pi/2]")
        println(s"Simpson: $integral_h_1")
        println(s"Trapez: $integral_h_2")
        println(s"Exact value is ${-1 * scala.math.cos(scala.math.Pi / 2.0) + scala.math.cos(0)}")