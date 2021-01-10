package main

import "fmt"

// This is a comment

func main() {
	fmt.Println("Hello world!")
	fmt.Println(102 % 10)

	// String literal: can contain special characters as \n, \t
	var s1 = "this is a simple string\tdemo\n"

	// String literal: can span several lines, but doesn't process special characters \n, \t
	var s2 = `This is another kind of string 
which can span several lines\n`

	fmt.Println(s1)
	fmt.Println(s2)

	// String operations
	fmt.Println(len("String length"))
	fmt.Println("Character at position"[3])
	fmt.Println("Concatenate " + "strings")

	// Booleans
	fmt.Println(true && false)
	fmt.Println(false || true)
	fmt.Println(!false)

	// Variables
	var v1 string
	fmt.Println("Unassigned var: " + v1)

	v1 = "A variable 1"
	fmt.Println(v1)

	var v2 = 1
	v2 += 4
	fmt.Println(v2)

	// Equality
	fmt.Println("AAA" == "aaa")

	// Infer type from assigned literal and abbreviated variable declaration (Idiomatic Go)
	var v3 = "Another string"
	v4 := 821

	fmt.Println(v3)
	fmt.Println(v4)

	// Go is lexically scoped using blocks
	fmt.Println("Global variable: " + g1)

	// Constants
	const c1 = 3.1416
	const c2 int64 = 99928320930192391

	fmt.Println(c2)

	// Define multiple variables (can also be constants, using const)
	var (
		mv1 = "1"
		mv2 = "2"
		mv3 = "3"
	)

	fmt.Println("Multi-vars: " + mv1 + ", " + mv2 + ", " + mv3)

	// Casting
	var f1 float64 = float64(12)
	fmt.Println(f1)

	mapsDemo()
}

/* GO INTEGER DATATYPES:
uint8, uint16, uint32, uint64, int8, int16, int32, int64 -> Machine independent
uint, int, intptr -> Machine dependent */

// Global variable
var g1 = "THIS IS A GLOBAL"

// Example: read user input
func doubleInput() {
	fmt.Println("Please enter a number: ")

	var inputNumber float64

	fmt.Scanf("%f", &inputNumber)

	result := inputNumber * 2

	fmt.Println(result)
}

func fahrenheitToCelcius() {
	var fahrenheit float64

	fmt.Println("Enter degrees Fahrenheit: ")
	fmt.Scanf("%f", &fahrenheit)

	celcius := (fahrenheit - 32.0) * (5.0 / 9.0)

	fmt.Println("Degrees Fahrenheit: ")
	fmt.Println(celcius)
}

func controlStructures() {
	// Go has only a loop keyword: for, which can be used in different ways

	// 1. As a while loop:
	i := 0
	for i <= 5 {
		fmt.Println(i)
		i++
	}

	// 2. As a classic for loop
	for i = 10; i <= 25; i++ {
		if i%2 == 0 {
			fmt.Println("Divisible by 2")
		} else if i%3 == 0 {
			fmt.Println("Divisible by 3")
		} else {
			fmt.Println("Not divisible neither 2 nor 3")
		}
	}

	// Switch statement. Note that using break on each case is not necessary
	v2 := 3

	switch v2 {
	case 1:
		fmt.Println("One")
	case 2:
		fmt.Println("Two")
	case 3:
		fmt.Println("Three")
	case 4:
		fmt.Println("Four")
	case 5:
		fmt.Println("Five")
	default:
		fmt.Println("> Five")
	}
}

func arraysDemo() {
	var a [10]float64
	var total float64 = 0

	a[5] = 30
	a[7] = 75

	for i := 0; i < len(a); i++ {
		total += a[i]
	}

	fmt.Println(total / float64(len(a)))

	// Short array declaration
	a2 := [7]float64{1, 2, 3, 4, 5, 6, 7}
	total2 := 0.0

	// Iterate through an array and its indices
	for _, val := range a2 {
		total2 += val
	}

	fmt.Println(total2)
}

func slicesDemo() {
	// A slice is a segment of an array, but length is allowed to change

	// Create an empty slice
	var s1 []float64

	// Create a slice with length (and capacity) 10
	s2 := make([]float64, 10)

	// Create a slice with length 10 and capacity 20
	s3 := make([]float64, 10, 20)

	a1 := []float64{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	s4 := a1[2:5]
	s5 := a1[3:]

	// Append elements to a slice. Increases length. Creates a new copy with if capacity is exceeded
	s6 := append(s5, 11, 33)

	fmt.Println(s1, s2, s3, s4)
	fmt.Println(s6)

	// Copy(dst, src) all entries in src into dst, overwritting whatever is there. Uses the smaller of the two. Does not grow the destination
	s7 := []int{1, 2, 3}
	s8 := make([]int, 2)
	copy(s8, s7)

	fmt.Println(s7, s8)
}

func mapsDemo() {
	// Declare a map of strings to ints
	var x map[string]int

	// Different to slices, maps must be initialized before use
	x = make(map[string]int)

	x["k1"] = 10
	x["k2"] = 11

	fmt.Println(x)

	// Length of map
	xLen := len(x)

	// Delete an element from a map
	delete(x, "k1")

	fmt.Println(xLen)

	// Getting a key not existing in the map returns the 'zero value' for the data type (e.g. "" for strings).
	// But accessing an element from a map can return two values, the second says whether or not the lookup was successful
	val, found := x["k3"]

	fmt.Println(val, found)

	// Idiomatic in go is:
	if v1, ok := x["k2"]; ok {
		fmt.Println(v1, ok)
	}

	m1 := map[string]map[string]string{
		"H": map[string]string{
			"name":  "Hydrogen",
			"state": "gas",
		},
		"He": map[string]string{
			"name":  "Helium",
			"state": "gas",
		},
	}

	fmt.Println(m1)
}
