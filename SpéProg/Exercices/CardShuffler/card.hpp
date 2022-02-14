#ifndef CARD_HPP__
#define CARD_HPP__

#include <iostream>

enum Suits { Spades, Hearts, Diamonds, Clubs };
class Card {
    private:
        int value;
        Suits suit;
    public:
        Card();
        Card(int value, Suits suit);
};

#endif