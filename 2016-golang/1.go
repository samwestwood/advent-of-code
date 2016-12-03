package main

import (
	"bufio"
	"fmt"
	"math"
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
	file, error := os.Open("../2016-inputs/1.txt")
	check(error)
	defer file.Close()

	posX := float64(0)

	posY := float64(0)
	bearing := float64(0) // 0 = N, 1 = E, 2 = S, 3 = W
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		//  Split on comma
		result := strings.Split(scanner.Text(), ",")

		// Iteratate through elements
		for i := range result {

			// Trim whitespace
			direction := strings.Trim(result[i], " ")
			turn := string(direction[0])

			// Surpress "multiple-value strconv.ParseFloat() in single-value context" error
			distance, err := strconv.ParseFloat(string(direction[1:]), 64)
			check(err)

			if turn == "R" {
				bearing = math.Mod(bearing + 1, 4)
			} else if turn == "L" {
				bearing = math.Mod(bearing - 1, 4)
			}

			// Go has weird Mod behaviour compared to python -6%4 is 2 in python, -2 here.
			// http://grokbase.com/t/gg/golang-nuts/147d606njp/go-nuts-mod-of-a-negative-number
			if bearing < 0 {
				bearing += 4
			}

			if bearing == 0 {
				posY = posY + distance
			}
			if bearing == 1 {
				posX = posX + distance
			}
			if bearing == 2 {
				posY = posY - distance
			}
			if bearing == 3 {
				posX = posX - distance
			}
		}
		fmt.Print(math.Abs(posX) + math.Abs(posY))
	}
}
