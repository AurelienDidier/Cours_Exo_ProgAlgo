/*
 * Paquets.cpp
 *
 *  Created on: 24 janv. 2022
 *      Author: GAME1.1
 */

#include "Paquet.hpp"
#include <iostream>
#include <time.h>

inline Paquet::Paquet(){

	int n = 0;

	for (Type y :{Type::Trefle, Type::Carreaux, Type::Coeur, Type::Pique}){
		for (int i = 0; i < 13; i++){
			carte[n] = Cartes(i,y);
			n++;
		}
	}
}

inline void Paquet::Melanger(){
	srand(time(NULL));
	for (int i=0; i<52; i++){
		Cartes carteTemp;
		int hasard = rand()%52;
		carteTemp = carte[i];
		carte[i] = carte[hasard];
		carte[hasard] = carteTemp;
	}
}


