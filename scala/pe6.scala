object ProjectEuler6 {
  def ss(from: Int, to: Int) = {
    val range = (from to to)
    range.sum * range.sum - range.map(x => x*x).sum
  }

  def main(args: Array[String]) = {
    println(ss(1, 100))
  }
}
