package main

import (
	"fmt"
)

func gcd(a int64, b int64) (g int64) {
	for b > 0 {
		a, b = b, a%b
	}
	return a
}

func lcm(a int64, b int64) (c int64) {
	return a / gcd(a, b) * b
}

func main() {
	var ans, i int64
	ans = 1
	for i = 1; i <= 20; i++ {
		ans = lcm(ans, i)
	}
	fmt.Println(ans)
}
