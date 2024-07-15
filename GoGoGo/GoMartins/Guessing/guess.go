package main


import (
    "bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
    "github.com/inancgumus/screen"
)

func main() {
    max, tries := 27, 5
	rand.Seed(time.Now().UnixNano())
	resposta := rand.Intn(max) 

    for tries > 0 {
	    fmt.Println("Adivinha vai, qual ce acha q eh")

	    reader := bufio.NewReader(os.Stdin)
	    input, err := reader.ReadString('\n')
	    if err != nil {
            fmt.Println("erro ao inserir numero:\n", err)
		    return
	    }

	    input = strings.TrimSuffix(input, "\n")

	    guess, err := strconv.Atoi(input)
	    if err != nil {
		    fmt.Println("erro ao parsar input. Escreva um numero.", err)
		    return
	    }

        if guess > resposta {
            tries--
            screen.Clear()
            screen.MoveTopLeft()
            fmt.Println(guess, "?\nAlto demais... Tenta de novo: \n", tries, "tentativas faltando")
	    } else if guess < resposta {
            tries--
            screen.Clear()
            screen.MoveTopLeft()
		    fmt.Println(guess, "?\nMuito baixo, vai de novo! \n", tries, "tentativas faltando")
	    } else {
            screen.Clear()
            screen.MoveTopLeft()
            fmt.Println("AEEEEEEEEEEEEEE!!!!!!!")
            break
	    }
    }
    if tries == 0 {
        fmt.Println("Acabaram as tentativas! Voce perdeu!")
    }
}
