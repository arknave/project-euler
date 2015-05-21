object ProjectEuler6 {
  def ss(from: Int, to: Int) = {
    val range = (from to to)
    val sum = range.sum
    sum * sum - range.map(x => x*x).sum
  }

  def main(args: Array[String]) = {
    println(ss(1, 100))
  }
}
