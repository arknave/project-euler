object ProjectEuler10 {
  lazy val primes: Stream[Long] = 
    2 #:: Stream.from(3, 2)
                .filter(
                  x => primes.takeWhile(p => p * p <= x)
                             .forall(p => x % p != 0))
                .map(_.toLong)

  def main(args: Array[String]) = println(primes.takeWhile(_ < 2000000).sum)
}
