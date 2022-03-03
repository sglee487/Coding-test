#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <cmath>

#include <algorithm>

int C;
int n,m,k;
int pascal[202][202];

int MAX = 1000000100;

void make_pascal(){
    pascal[0][0] = 1;
    for (int i=1;i<=201;i++){
        pascal[i][0] = pascal[i][i] = 1;
        for (int j=1;j<i;j++)
            pascal[i][j] = std::min(MAX, pascal[i-1][j-1] + pascal[i-1][j]);
    }

}

void dfs(int n, int m, std::string word){
    if (k<0) return;
    if (n==0 && m==0){
        if (k==0)
            std::cout << word << std::endl;
        k--;
        return;
    }

    if (pascal[n-1+m][n-1] <= k){
        k -= pascal[n-1+m][n-1];
        dfs(n,m-1,word + "o");
    } else{
        dfs(n-1,m,word + "-");
    }

    // if (n>0)
    //     dfs(n-1,m,word + "-");
    // if (m>0)
    //     dfs(n,m-1,word + "o");

    return;
}

int main(){
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0);

    std::ifstream ifs;
    ifs.open("MORSE-1.txt");

    memset(pascal,0,sizeof(pascal));

    make_pascal();
    // for (int i=0;i<10;i++){
    //     for (int j=0;j<10;j++)
    //         std::cout << pascal[i][j] << " ";
    //     std::cout<<std::endl;
    // }

    ifs >> C;
    while (C--){
        ifs >> n >> m >> k;
        k--;
        dfs(n,m,"");


    }


    return 0;
}