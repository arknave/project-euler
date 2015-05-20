object ProjectEuler5 {
  def gcd(x: Int, y: Int): Int = if (x == 0) y else gcd(y % x, x)

  def lcm(x: Int, y: Int): Int = x * y / gcd(x, y)

  def main(args: Array[String]) = {
    println( (1 to 20).reduceLeft(lcm) )
  }
}
