#include <iostream>
#include <time.h>
#include "pack.hpp"

inline Pack::Pack() {
    int n = 0;
    for (int i=1; i<14; i++) {
        for (Suits s : {Suits::Spades, Suits::Hearts, Suits::Diamonds, Suits::Clubs}) {
            cards[n] = Card(i, s);
            n++;
        }
    }  
}

inline void Pack::shuffle() {
    srand(time(NULL));              // Randomise seed
    for (int i=0; i<52; i++) {
        int random = rand() % 52;

        Card temp_card;
        temp_card = cards[i];
        cards[i] = cards[random];
        cards[random] = temp_card;
    }
}