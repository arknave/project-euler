package main

import (
	"fmt"
)

func main() {
	var sumsq, sqsum, i int64
	sumsq = 0
	sqsum = 0
	for i = 1; i <= 100; i++ {
		sumsq += i * i
		sqsum += i
	}
	sqsum *= sqsum

	fmt.Println(sqsum - sumsq)
}
