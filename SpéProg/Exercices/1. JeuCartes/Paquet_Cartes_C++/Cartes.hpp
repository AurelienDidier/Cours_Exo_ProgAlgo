/*
 * Cartes.hpp
 *
 *  Created on: 24 janv. 2022
 *      Author: GAME1.1
 */

#ifndef CARTES_HPP_
#define CARTES_HPP_

#include <string>

enum Type {Trefle, Carreaux, Coeur, Pique};

class Cartes{

private:
	int valeur;
	Type type;

public:
	Cartes();
	Cartes(int valeur, Type type);

};


#endif /* CARTES_HPP_ */
