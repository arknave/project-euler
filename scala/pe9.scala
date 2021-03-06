object ProjectEuler9 {
  def main(args: Array[String]) = {
    val triples = for (a <- (1 until 1000);
                       b <- (a + 1 until 1000);
                       val c = 1000 - a - b;
                       val c2 = a * a + b * b 
                       if c * c == c2) yield (a, b, c)
    val ans = triples.head
    println(ans._1 * ans._2 * ans._3)
  }
}
