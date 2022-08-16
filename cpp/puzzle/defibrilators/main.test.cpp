#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

double strToDbl(std::string &str, std::string const sub = ".")
{
    return stod(
        str.replace(
            str.find_first_of(','), 1, sub
        )
    );
}


template <class T>
void split(const std::string &str, T &cont, char delim = ';')
{
    size_t curr = 0;
    size_t next = str.find(delim, curr);
    while (next != std::string::npos)
    {
        cont.push_back(str.substr(curr, next - curr));
        curr = next + 1;
        next = str.find(delim, curr);
    }
    cont.push_back(str.substr(curr, str.length() - curr));
}


double getDistance(double const &lonA, double const &latA, double const &lonB, double const &latB)
{
    double x = (lonB - lonA) * cos((latA + latB)/2);
    double y = latB - latA;
    return sqrt(pow(x, 2) + pow(y, 2)) * 6371;
}


    int main()
{
    std::string LON = "3,879483";
    double dLON = strToDbl(LON);

    std::string LAT = "43,608177";
    double dLAT = strToDbl(LAT);

    std::vector<std::string> defibs; 
    defibs.push_back("1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217");
    defibs.push_back("2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849");
    defibs.push_back("3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854");

    std::vector<double> distances;
    std::vector<std::string> defibsLocation;

    for (size_t i = 0; i < defibs.size(); i++)
    {
        std::vector<std::string> strSplit;
        split(defibs[i], strSplit);
        defibsLocation.push_back(strSplit[1]);
        distances.push_back(getDistance(dLON, dLAT, strToDbl(strSplit[4]), strToDbl(strSplit[5])));
    }
    
    size_t minDistanceIndex = std::min_element(distances.begin(), distances.end()) - distances.begin();
    
    std::cout << defibsLocation[minDistanceIndex] << std::endl;
    return 0;
}