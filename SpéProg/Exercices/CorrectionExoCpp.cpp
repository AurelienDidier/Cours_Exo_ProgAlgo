#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

//Exo 1
template <class T>
bool isGenericPair (T a){
    return a%2==0;
}

//Exo 2

template <class T>
int countPositive(T tab[], int taille){
    int count = 0;
    for (int i=0; i<taille; i++){
        if (tab[i]>=0){
            count++;
        }
    }
    return count;
}


//Exo 3
template <class T>
T getSomme(vector<T> vect){
    T result = 0;
    for (int i=0; i<vect.size(); i++){
            result+=vect[i];
    }
    return result;
}

//Exo 4
template<class T>
T rechercheMax(list<T> l){
    T result = l.front();
    for (T i:l){
        if (i>result){
            result = i;
        }
    }
    return result;
}

//Exo 5
template <class T>
T fibo(T n, T init){
    if (n>=0 && n<2){
        return init;
    } else if (n>=2){
        return fibo(n-1, init)+fibo(n-2, init);
    }
}

int main()
{
    //Exo 1
    cout << isGenericPair(2222222212222)<<endl;
    //Exo 2
    double tab[5] = {-5.1,5.4,-2.1,3.7,4.0} ;
    cout << countPositive(tab,5)<<endl;
    //Exo 3
    vector<double> v = {-5.1,5.4,-2.1,3.7,4.0} ;
    cout << getSomme(v)<<endl;
    //Exo 4
    list<string> l = {"Hello","Bonjour", "Salut"} ;
    cout << rechercheMax(l)<<endl;
    //Exo 5
    cout << fibo(7,2) << endl;
    cout << fibo(7.4,2.2) << endl;
    return 0;
}
