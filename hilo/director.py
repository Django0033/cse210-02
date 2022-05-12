from card import Card


class Director:
    def __init__(self, min_card, max_card, ask_h_or_l, right_guess, wrong_guess, same_number):
        self.min_card = min_card
        self.max_card = max_card
        self.ask_h_or_l_func = ask_h_or_l
        self.right_guess_func = right_guess
        self.wrong_guess_func = wrong_guess
        self.same_number_func = same_number

    def next_play(self):
        card1 = Card(self.min_card, self.max_card)

        option = self.ask_h_or_l_func(card1).lower()

        card2 = Card(self.min_card, self.max_card)

        if option == 'h':
            high_card = card2
            low_card = card1
        elif option == 'l':
            high_card = card1
            low_card = card2

        if high_card > low_card:
            self.right_guess_func()
        elif low_card > high_card:
            self.wrong_guess_func()
        else:
            self.same_number_func()

        return card2
