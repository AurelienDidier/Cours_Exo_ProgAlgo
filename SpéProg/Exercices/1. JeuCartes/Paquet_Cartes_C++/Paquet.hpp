/*
 * Paquet.hpp
 *
 *  Created on: 24 janv. 2022
 *      Author: GAME1.1
 */

#ifndef PAQUET_HPP_
#define PAQUET_HPP_

#include "Cartes.hpp"
#include <stdio.h>

class Paquet{

private:
	Cartes carte[52];

public:
	Paquet();
	void Melanger();
};





#endif /* PAQUET_HPP_ */
