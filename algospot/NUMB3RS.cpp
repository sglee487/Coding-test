#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C, N, D, P, T;
int A[51][51];
int G[51];
int ways[51];
double cache[101][51];

int cal_ways(int vil){
    int result = 0;
    for(int i=0;i<N;i++)
        result += A[vil][i];
    return result;
}

// 종만북 풀이 3
double search3(int day, int here){
    if (day == 0) return (here == P ? 1.0 : 0.0);
    double &ret = cache[day][here];
    if (ret > -0.5) return ret;

    ret = 0.0;
    for (int there = 0; there < N; there++)
        if (A[here][there])
            ret += (search3(day-1, there) / ways[there]);
    return ret;
}

int main(){

    std::ifstream ifs;
    ifs.open("NUMB3RS-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> N >> D >> P;
        for (int i=0;i<N;i++)
            for (int j=0;j<N;j++)
                ifs >> A[i][j];
        ifs >> T;
        for (int i=0;i<T;i++)
            ifs >> G[i];

        for (int i=0;i<101;i++)
            for (int j=0;j<51;j++)
                cache[i][j] = (double)-1;

        for (int i=0;i<N;i++)
            ways[i] = cal_ways(i);

        std::cout.precision(8);
        for (int i=0;i<T;i++)
            std::cout << search3(D, G[i]) << " ";
        std::cout << std::endl;

    }

    return 0;
}