from director import Director

MIN_CARD = 1
MAX_CARD = 13
STARTING_SCORE = 300
WIN_POINTS = 100
LOSS_POINTS = -75

score = STARTING_SCORE


def main():

    def ask_h_or_l(previous_card):
        print(f'The card is: {previous_card.number}')
        return input('Higher or lower? [h/l] ')

    def right_guess():
        global score

        score += WIN_POINTS

    def wrong_guess():
        global score

        score += LOSS_POINTS

    def same_number():
        print('The next card had the same number!')

    game = Director(MIN_CARD, MAX_CARD, ask_h_or_l,
                    right_guess, wrong_guess, same_number)

    while score > 0:
        card_drawn = game.next_play()

        print(f'Next card was: {card_drawn.number}\nYour score is: {score}')

        option = input('Play again? [y/n] ').lower()

        if(score <= 0):
            print('Game over!')
            break

        if(option != 'y'):
            break


if __name__ == '__main__':
    main()
