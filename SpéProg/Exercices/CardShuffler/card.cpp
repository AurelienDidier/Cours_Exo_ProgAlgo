#include <iostream>
#include "card.hpp"

Card::Card() {
    this->value = 1;
    this->suit = Suits::Spades;
}

Card::Card(int valueInit, Suits suitInit) {
    this->value = valueInit;
    this->suit = suitInit;
}