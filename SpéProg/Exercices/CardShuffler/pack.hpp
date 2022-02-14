#ifndef PACK_HPP__
#define PACK_HPP__

#include <iostream>
#include "card.hpp"
#include "card.cpp"

class Pack {
    private:
        Card cards[52];
    public:
        Pack();
        void shuffle();
};

#endif