package main

import (
	"fmt"
	"strconv"
)

func isPal(n int) (res bool) {
	str := strconv.Itoa(n)
	s := 0
	e := len(str) - 1
	res = true
	for res == true && s < e {
		res = res && (str[s] == str[e])
		s++
		e--
	}
	return
}

func main() {
	ans := 0

	for i := 100; i < 1000; i++ {
		for j := i; j < 1000; j++ {
			n := i * j
			if n > ans && isPal(n) {
				ans = n
			}
		}
	}

	fmt.Println(ans)
}
