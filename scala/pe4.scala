object ProjectEuler4 {
  def isPalindrome(x: Int) = {
    val s = x.toString
    s == s.reverse
  }

  def palindromeGenerator(from: Int, to: Int) =
    for (i <- from until to; 
         j <- from until to if isPalindrome(i * j)) yield i * j

  def main(args: Array[String]) = {
    println(palindromeGenerator(100, 1000) max)
  }
}
