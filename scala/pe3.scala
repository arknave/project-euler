import scala.collection.immutable.Set

object ProjectEuler3 {
  def leastFactorDivides(x: Long, from: Long): Long = {
    if (x % from == 0) return from
    if (from > x) return -1L
    leastFactorDivides(x, from + 1)
  }

  def factor(x: Long, primeFactors: Set[Long]): Set[Long] = {
    if (x == 1) {
      return primeFactors
    } else if (x % 2 == 0) {
      return factor(x / 2, primeFactors + 2)
    } else {
      val oldMax = if (primeFactors isEmpty) 2L else primeFactors max
      val leastFactor = leastFactorDivides(x, oldMax)

      if (leastFactor == -1) {
        return primeFactors
      } else {
        factor(x / leastFactor, primeFactors + leastFactor)
      }
    }
  }

  def main(args: Array[String]) = println(factor(600851475143L, Set()) max)
}
