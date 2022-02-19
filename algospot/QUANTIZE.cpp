#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C, N, S;
int nl[102];
int cache[101][11];

int INF = 987654321;

int pow(int x){
    return (int)x * x;
}

int min_error(int a, int b){
    int min_sum = INF;
    for (int num=nl[a];num<=nl[b];num++)
    {
        int sum = 0;
        for (int now=a; now <= b; now++)
            sum += pow(num - nl[now]);
        min_sum = std::min(min_sum, sum);
        }
    return min_sum;
}

int dfs(int index, int step){
    if (index == N) return 0;
    if (step == S) return INF;
    
    int &ret = cache[index][step];
    if (ret != -1) return ret;
    ret = INF;
    for (int length=0; index+length < N; length++)
        ret = std::min(ret, min_error(index, index+length) + 
                            dfs(index+length+1, step+1));

    return ret;
}

int main(){

    std::ifstream ifs;
    ifs.open("QUANTIZE-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> N >> S;
        for (int i=0;i<N;i++)
            ifs >> nl[i];
        std::sort(nl, nl+N);
        memset(cache, -1, sizeof(cache));
        std::cout << dfs(0,0) << std::endl;

    }

    return 0;
}