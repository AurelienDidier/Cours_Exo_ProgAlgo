/*
 * Cartes.cpp
 *
 *  Created on: 24 janv. 2022
 *      Author: GAME1.1
 */

#include "Cartes.hpp"
#include<stdio.h>

Cartes::Cartes(){
	this -> valeur = 1;
	this -> type = Type::Carreaux;
}

Cartes::Cartes(int valeurInit, Type typeInit)
{
	valeur = valeurInit;
	type = typeInit;
}

