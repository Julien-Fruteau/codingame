#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

double strToDbl(string &str, string const sub = ".")
{
    return stod(
        str.replace(
            str.find_first_of(','), 1, sub));
}

template <class T>
void split(const string &str, T &cont, char delim = ';')
{
    size_t curr = 0;
    size_t next = str.find(delim, curr);
    while (next != string::npos)
    {
        cont.push_back(str.substr(curr, next - curr));
        curr = next + 1;
        next = str.find(delim, curr);
    }
    cont.push_back(str.substr(curr, str.length() - curr));
}

double getDistance(double const &lonA, double const &latA, double const &lonB, double const &latB)
{
    double x = (lonB - lonA) * cos((latA + latB) / 2);
    double y = latB - latA;
    return sqrt(pow(x, 2) + pow(y, 2)) * 6371;
}

int main()
{
    string LON;
    cin >> LON; cin.ignore();
    double dLON = strToDbl(LON);

    string LAT;
    cin >> LAT; cin.ignore();
    double dLAT = strToDbl(LAT);

    vector<double> distances;
    vector<string> defibsLocation;
    int N;
    cin >> N; cin.ignore();
    for (int i = 0; i < N; i++) {
        string DEFIB;
        getline(cin, DEFIB);

        vector<string> strSplit;
        split(DEFIB, strSplit);
        defibsLocation.push_back(strSplit[1]);
        distances.push_back(getDistance(dLON, dLAT, strToDbl(strSplit[4]), strToDbl(strSplit[5])));
    }

    size_t minDistanceIndex = min_element(distances.begin(), distances.end()) - distances.begin();
    cout << defibsLocation[minDistanceIndex] << endl;
}