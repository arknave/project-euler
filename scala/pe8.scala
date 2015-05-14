import scala.io.Source

object ProjectEuler8 {
  val charToInt: PartialFunction[Char, Int] = {
    case c if '0' <= c && c <= '9' => c - '0'
  }

  def prod(l: TraversableOnce[Int]): Long = (1L /: l)(_ * _)

  def main(args: Array[String]) = {
    val it: Iterator[Long] = Source fromFile("../data_files/p08.txt") collect(charToInt) sliding(13) map(prod)

    println(it max)
  }
}
