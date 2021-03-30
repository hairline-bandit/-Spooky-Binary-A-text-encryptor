package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// string for conversions
var ascii string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "

// slice for getting characters
var dict = []string{
	"/ 000000",
	"  000001",
	"9 000010",
	"8 000011",
	"7 000100",
	"6 000101",
	"5 000110",
	"4 000111",
	"3 001000",
	"2 001001",
	"1 001010",
	"0 001011",
	"Z 001100",
	"Y 001101",
	"X 001110",
	"W 001111",
	"V 010000",
	"U 010001",
	"T 010010",
	"S 010011",
	"R 010100",
	"Q 010101",
	"P 010110",
	"O 010111",
	"N 011000",
	"M 011001",
	"L 011010",
	"K 011011",
	"J 011100",
	"I 011101",
	"H 011110",
	"G 011111",
	"F 100000",
	"E 100001",
	"D 100010",
	"C 100011",
	"B 100100",
	"A 100101",
	"z 100110",
	"y 100111",
	"x 101000",
	"w 101001",
	"v 101010",
	"u 101011",
	"t 101100",
	"s 101101",
	"r 101110",
	"q 101111",
	"p 110000",
	"o 110001",
	"n 110010",
	"m 110011",
	"l 110100",
	"k 110101",
	"j 110110",
	"i 110111",
	"h 111000",
	"g 111001",
	"f 111010",
	"e 111011",
	"d 111100",
	"c 111101",
	"b 111110",
	"a 111111"}

func main() {
	// making bufio scanner as fmt.Scan/fmt.Scanln scans to space or new-line
	scanner := bufio.NewScanner(os.Stdin)
	var choice string
	// deciding which function to run
	fmt.Print("Encrypt(0) or Decrypt(1): ")
	fmt.Scanln(&choice)
	// encryption
	if choice == "0" {
		var orgText string
		var orgKey string
		fmt.Print("Enter the text that you'd like to encrypt: ")
		scanner.Scan()
		orgText = scanner.Text()
		fmt.Print("Enter the key you'd like to encrypt with: ")
		scanner.Scan()
		orgKey = scanner.Text()
		fmt.Println(encrypt(orgText, orgKey))
		// decryption
	} else if choice == "1" {
		var cipherText string
		var key string
		fmt.Print("Enter ciphertext: ")
		scanner.Scan()
		cipherText = scanner.Text()
		fmt.Print("Enter key: ")
		scanner.Scan()
		key = scanner.Text()
		fmt.Println(decrypt(cipherText, key))
	}
	// keeps executable open to enable copying ciphertext
	fmt.Scanln()
}

// function for encrypting text
func encrypt(text string, key string) string {
	textAlt := []string{}
	keyAlt := []string{}
	combinedAlt := []string{}
	cipherText := []string{}
	// get alternates
	for i := 0; i < len(text); i++ {
		textAlt = append(textAlt, alternate(string(text[i]), i, len(text)))
	}
	for i := 0; i < len(key); i++ {
		keyAlt = append(keyAlt, alternate(string(key[i]), i, len(key)))
	}
	// combine them
	if len(textAlt) > len(keyAlt) {
		combinedAlt = specialAdd(textAlt, keyAlt, "t")
	} else if len(textAlt) < len(keyAlt) {
		combinedAlt = specialAdd(textAlt, keyAlt, "k")
	} else if len(textAlt) == len(keyAlt) {
		combinedAlt = specialAdd(textAlt, keyAlt, "e")
	}
	// get the chars for each
	for i := 0; i < len(combinedAlt); i++ {
		cipherText = append(cipherText, makeChar(combinedAlt[i]))
	}
	return strings.Join(cipherText, "")
}

// function for getting the alternate string of a character
func alternate(char string, index int, length int) string {
	out := ""
	if strings.Contains(ascii, char) {
		out += string(ascii[len(ascii)-1-strings.Index(ascii, char)])
	}
	out += strconv.Itoa(length - index)
	return out
}

// function for adding 2 alternates together (into 1)
func specialAdd(text []string, key []string, choice string) []string {
	conversion := ascii + ascii
	var end []string
	if choice == "t" {
		for i := 0; i < len(key); i++ {
			var numNum int64
			textIndex := strings.Index(conversion, string(text[i][0]))
			keyIndex := strings.Index(conversion, string(key[i][0]))
			a, err := strconv.ParseInt(text[i][1:], 10, 64)
			b, er := strconv.ParseInt(key[i][1:], 10, 64)
			if err == nil && er == nil {
				numNum = a + b
			}
			extra := ""
			if numNum >= int64(len(conversion)) {
				extra += "/"
			} else {
				extra += string(conversion[numNum])
			}
			out := string(conversion[textIndex+keyIndex]) + extra
			end = append(end, out)
		}
		for i := len(key); i < len(text); i++ {
			end = append(end, text[i])
		}
	} else if choice == "k" {
		for i := 0; i < len(text); i++ {
			var numNum int64
			textIndex := strings.Index(conversion, string(text[i][0]))
			keyIndex := strings.Index(conversion, string(key[i][0]))
			a, err := strconv.ParseInt(text[i][1:], 10, 64)
			b, er := strconv.ParseInt(key[i][1:], 10, 64)
			if err == nil && er == nil {
				numNum = a + b
			}
			extra := ""
			if numNum >= int64(len(conversion)) {
				extra += "/"
			} else {
				extra += string(conversion[numNum])
			}
			out := string(conversion[textIndex+keyIndex]) + extra
			end = append(end, out)
		}
		for i := len(text); i < len(key); i++ {
			end = append(end, key[i])
		}
	} else if choice == "e" {
		for i := 0; i < len(text); i++ {
			var numNum int64
			textIndex := strings.Index(conversion, string(text[i][0]))
			keyIndex := strings.Index(conversion, string(key[i][0]))
			a, err := strconv.ParseInt(text[i][1:], 10, 64)
			b, er := strconv.ParseInt(key[i][1:], 10, 64)
			if err == nil && er == nil {
				numNum = a + b
			}
			extra := ""
			if numNum >= int64(len(conversion)) {
				extra += "/"
			} else {
				extra += string(conversion[numNum])
			}
			out := string(conversion[textIndex+keyIndex]) + extra
			end = append(end, out)
		}
	}
	return end
}

// function for making a character out of a combined alternate
func makeChar(alt string) string {
	var decision string
	for i := 0; i < len(alt); i++ {
		if i < 2 {
			for j := 0; j < len(dict); j++ {
				if dict[j][0] == alt[i] {
					decision += dict[j][2:]
					break
				}
			}
		}
	}
	return decision
}

// function for decrypting ciphertext
func decrypt(text string, key string) string {
	keyAlt := []string{}
	textAlt := []string{}
	combinedAlt := []string{}
	split := []string{}
	characters := []string{}
	var out string
	a := len(text)
	// splitting into 6 bit sequences
	for i := 0; i < a-1; i++ {
		if i%6 == 0 && i != 0 {
			split = append(split, text[i-6:i])
		}
	}
	// getting the characters from 6 bit sequences
	split = append(split, text[len(text)-6:])
	for i := 0; i < len(split); i++ {
		for j := 0; j < len(dict); j++ {
			if dict[j][2:] == split[i] {
				characters = append(characters, string(dict[j][0]))
				break
			}
		}
	}
	// combining every 2 into their original alternate
	characters = append(characters, " ")
	current := ""
	counter := 0
	for i := 0; i < len(characters); i++ {
		if counter < 2 {
			current += characters[i]
		} else if counter == 2 {
			combinedAlt = append(combinedAlt, current)
			current = ""
			counter = 0
			current += characters[i]
		}
		counter++
	}
	// getting alternates for inputted key
	for i := 0; i < len(key); i++ {
		keyAlt = append(keyAlt, alternate(string(key[i]), i, len(key)))
	}
	// "subtracting" key's alternates from the combined ones got from ciphertext
	if len(combinedAlt) > len(keyAlt) {
		for i := 0; i < len(keyAlt); i++ {
			textAlt = append(textAlt, specialSub(string(combinedAlt[i]), string(keyAlt[i])))
		}
		for i := len(keyAlt); i < len(combinedAlt); i++ {
			textAlt = append(textAlt, string(combinedAlt[i][0]))
		}
	} else if len(combinedAlt) < len(keyAlt) || len(combinedAlt) == len(keyAlt) {
		for i := 0; i < len(combinedAlt); i++ {
			textAlt = append(textAlt, specialSub(string(combinedAlt[i]), string(keyAlt[i])))
		}
	}
	// undoing alternates
	for i := 0; i < len(textAlt); i++ {
		out += unAlternate(textAlt[i])
	}
	return out
}

// function for subtracting alterates
func specialSub(alt string, keyAlt string) string {
	out := ""
	conversion := ascii + ascii
	keyIndex := strings.Index(conversion, string(keyAlt[0]))
	altIndex := strings.Index(conversion, string(alt[0]))
	if keyIndex > altIndex {
		altIndex = strings.LastIndex(conversion, string(alt[0]))
	}
	out += string(conversion[altIndex-keyIndex])
	return out
}

// function for undoing alternates
func unAlternate(alt string) string {
	out := ""
	if strings.Contains(ascii, alt) {
		out += string(ascii[len(ascii)-1-strings.Index(ascii, alt)])
	}
	return out
}
