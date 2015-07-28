import scala.io.Source
import scala.Char

object ProjectEuler8 {

  def main(args: Array[String]) = {
    val it = (Source fromFile("../data_files/p08.txt") 
                     map(_.asDigit.toLong)
                     filter(_ != -1)
                     sliding(13)
                     map(_.product))

    println(it max)
  }
}
