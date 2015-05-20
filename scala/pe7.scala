object ProjectEuler7 {

  lazy val primes: Stream[Int] = 
    2 #:: Stream.from(3)
                .filter(x => isPrime(x, primes.takeWhile(y => y * y <= x)))

  def isPrime(x: Int, primes: Stream[Int]) = primes.forall(k => x % k != 0)

  def main(args: Array[String]) = {
    println(primes(10000))
  }
}
