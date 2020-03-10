```c++

#include <fstream>
#include <cmath>
using namespace std;

double A[4];
double B[4];
double P[4];
double len_T;

void binary_Search(double start, double end){
    double s[4], e[4];

    s[0] = start* B[0] + (1-start)*A[0];
    s[1] = start* B[1] + (1-start)*A[1];
    s[2] = start* B[2] + (1-start)*A[2];

    e[0] = end* B[0] + (1-end)*A[0];
    e[1] = end* B[1] + (1-end)*A[1];
    e[2] = end* B[2] + (1-end)*A[2];

    double len_s = (s[0]-P[0])*(s[0]-P[0])+(s[1]-P[1])*(s[1]-P[1])+(s[2]-P[2])*(s[2]-P[2]);
    double len_e = (e[0]-P[0])*(e[0]-P[0])+(e[1]-P[1])*(e[1]-P[1])+(e[2]-P[2])*(e[2]-P[2]);

    double T[4];

    if(len_s == len_e){
        T[0] = (s[0] + e[0])/2;
        T[1] = (s[1] + e[1])/2;
        T[2] = (s[2] + e[2])/2;
        len_T = (T[0]-P[0])*(T[0]-P[0])+(T[1]-P[1])*(T[1]-P[1])+(T[2]-P[2])*(T[2]-P[2]);
        return ;
    }
    else if(len_s < len_e){
        binary_Search(start,(start+end)/2);
        return ;
    }
    else{
        binary_Search((start+end)/2, end);
        return ;
    }
    return ;
}

int main(){
    double len_A, len_B, len_AB;
    int len_L;

    ifstream ifs("1.inp");
    ofstream ofs("1.out");


    for(int i=0; i<3; ++i){
        ifs >> A[i];
    }

     for(int i=0; i<3; ++i){
        ifs >> B[i];
    }

     for(int i=0; i<3; ++i){
        ifs >> P[i];
    }

    len_A = (A[0]-P[0])*(A[0]-P[0]) + (A[1]-P[1])*(A[1]-P[1])+(A[2]-P[2])*(A[2]-P[2]);
    len_B = (B[0]-P[0])*(B[0]-P[0]) + (B[1]-P[1])*(B[1]-P[1])+(B[2]-P[2])*(B[2]-P[2]);
    len_AB = (A[0]-B[0])*(A[0]-B[0]) + (A[1]-B[1])*(A[1]-B[1])+(A[2]-B[2])*(A[2]-B[2]);


    if(len_A <= len_B){
        if(len_A+len_AB <= len_B){
            ofs << len_A;
            return 0;
        }
        else
            binary_Search(0,1);
    }

    else{
        if(len_B+len_AB <= len_A){
            ofs << len_B;
            return 0;
        }
        else
            binary_Search(0,1);
    }

    len_L = (int)ceil(sqrt(len_T));
    ofs << len_L;

    return 0;

}
```
