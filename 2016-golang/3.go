package main

import (
	"bufio"
	"fmt"
	// "math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, error := os.Open("../2016-inputs/3.txt")
	check(error)
	defer file.Close()

	valid := float64(0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {

		// Trim whitespace
		direction := strings.Trim(scanner.Text(), " ")

		//  Split on comma
		result := strings.Fields(direction)

		// Parse string to int (surely there is a better way…)
		a, error := strconv.ParseFloat(string(result[0]), 64)
		b, error := strconv.ParseFloat(string(result[1]), 64)
		c, error := strconv.ParseFloat(string(result[2]), 64)

		check(error)

		if a+b > c && a+c > b && b+c > a {
			// Apparently this is better than += 1
			valid++
		}
	}
	fmt.Print(valid)
}
