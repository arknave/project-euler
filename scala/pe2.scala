object ProjectEuler2 {
  val fibs:Stream[Int] = 0 #:: 1 #:: (fibs zip fibs.tail).map(t => t._1 + t._2)

  def main(args: Array[String]) = 
    println(fibs 
            takeWhile (_ <= 4000000)
            filter (_ % 2 == 0)
            sum)
}
