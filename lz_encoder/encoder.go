package main

import (
	"fmt"
)

type LZ77Tuple struct {
	offset int
	length int
	char   byte
}

func maxOfTwo(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func compressLZ77(history, lookahead string) []LZ77Tuple {
	var compressedData []LZ77Tuple
	windowSize := len(history)
	i := 0

	for i < len(lookahead) {
		bestMatchDistance := 0
		bestMatchLength := 0

		// Search for the longest match in the sliding window (history)
		for j := maxOfTwo(0, len(history)-windowSize); j < len(history); j++ {
			length := 0
			for length < len(lookahead)-i && history[j+length] == lookahead[i+length] {
				length++
			}
			if length > bestMatchLength {
				bestMatchDistance = len(history) - j
				bestMatchLength = length
			}
		}

		// If a match is found, add a tuple (offset, length, next char)
		if bestMatchLength > 0 && i+bestMatchLength < len(lookahead) {
			nextChar := lookahead[i+bestMatchLength]
			compressedData = append(compressedData, LZ77Tuple{bestMatchDistance, bestMatchLength, nextChar})
			i += bestMatchLength + 1
		} else {
			// No match found, add a tuple with zero offset and length, and the current character
			compressedData = append(compressedData, LZ77Tuple{0, 0, lookahead[i]})
			i++
		}

		// Update the history window
		if i < len(lookahead) {
			history += lookahead[:i]
			if len(history) > windowSize {
				history = history[len(history)-windowSize:]
			}
		}
	}

	return compressedData
}

// sliceAndCompress slices the input string, divides it, compresses it, and prints results
func sliceAndCompress(input string, n int) {
	// Ensure n does not exceed the length of input
	if n > len(input) {
		n = len(input)
	}

	newText := input[:n]
	fmt.Println("NewText:", newText)

	// Calculate the 2/3 and 1/3 split
	twoThirdsIndex := (2 * n) / 3
	history := newText[:twoThirdsIndex]
	lookahead := newText[twoThirdsIndex:]

	fmt.Println("History:", history)
	fmt.Println("Lookahead:", lookahead)

	// Apply LZ77 compression on history and lookahead
	compressedData := compressLZ77(history, lookahead)

	// Print compressed data
	fmt.Println("Compressed Data:")
	for _, tuple := range compressedData {
		fmt.Printf("(%d, %d, %q)\n", tuple.offset, tuple.length, tuple.char)
	}

	// Calculate memory size of compressed data
	memorySizeCompressed := 0
	for _, tuple := range compressedData {
		memorySizeCompressed += len(fmt.Sprintf("%d%d%c", tuple.offset, tuple.length, tuple.char))
	}
	memorySizeOriginal := len(newText)

	fmt.Println("Memory Size of Compressed Data:", memorySizeCompressed)
	fmt.Println("Memory Size of Original Data:", memorySizeOriginal)

	// Compression ratio
	compressionRatio := float64(memorySizeCompressed) / float64(memorySizeOriginal)
	fmt.Printf("Compression Ratio: %.2f\n", compressionRatio)
}

func main() {
	input := "In radio c'è un pulcino In radio c'è un pulcino È il pulcino pio, è il pulcino pio E il pulcino pio, e il pulcino pio"
	plaque := "2077518"
	n := 0
	for i := 0; i < len(plaque); i++ {
		n += int(plaque[i] - '0')
	}

	sliceAndCompress(input, n)
}
