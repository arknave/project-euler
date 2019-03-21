package main

import "fmt"

func main() {
	sum := 0
	a := 1
	for b := 2; b < 4000000; {
		if b%2 == 0 {
			sum += b
		}
		c := a + b
		a = b
		b = c
	}

	fmt.Println(sum)
}
