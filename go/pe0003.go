package main

import "fmt"

func main() {
	var n, i int64
	n = 600851475143
	for i = 2; i*i <= n; i++ {
		for ; n%i == 0; n /= i {
		}
	}
	fmt.Println(n)
}
