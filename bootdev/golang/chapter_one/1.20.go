package main

import "fmt"

func main() {
	const name = "Saul Goodman"
	const openRate = 30.5

	// ?
	msg := fmt.Sprintf("%v, your open rate is %v percent\n", name, openRate)
	// don't edit below this line

	fmt.Print(msg)
}
