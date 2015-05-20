object ProjectEuler3 {

  def factorFrom(x: Long, factor: Long): List[Long] = {
    if      (x == 1L)         List()
    else if (x < factor)      List()
    else if (x % factor == 0) factor :: factorFrom(x / factor, factor)
    else                      factorFrom(x, factor + 1)
  }

  def factor(x: Long): List[Long] = factorFrom(x, 2)

  def main(args: Array[String]) = println(factor(600851475143L).last)
}
