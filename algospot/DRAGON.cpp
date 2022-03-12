#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <cmath>

#include <algorithm>

int C;
int n, p, l;
int lengths[51];

const int MAX = 1000000000+1;

void set_lengths(){
    lengths[0] = 1;
    for (int i=1;i<=50;i++)
        lengths[i] = std::min(2*lengths[i-1] + 2, MAX);
    return;
}

char dfs(const std::string& text, int step, int skip){
    if (step == 0)
        return text[skip];
    
    for (int i=0;i<text.size();i++){
        if (text[i] == 'X' || text[i] == 'Y'){
            if (skip >= lengths[step])
                skip -= lengths[step];
            else if (text[i] == 'X')
                return dfs("X+YF", step-1, skip);
            else if (text[i] == 'Y')
                return dfs("FX-Y", step-1, skip);
        }
        else if (skip > 0)
            skip--;
        else
            return text[i];
        
    }
    return 'a';
}

int main(){
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0);

    std::ifstream ifs;
    ifs.open("DRAGON-1.txt");

    set_lengths();
    ifs >> C;
    while (C--){
        ifs >> n >> p >> l;
        // for (int i = 0; i < l; i++){
        //     std::cout << p + i - 1 << std::endl;
		// 	std::cout << dfs("FX", n, p + i - 1);
        // }
        for (int i = p; i < p+l; i++)
			std::cout << dfs("FX", n, i-1);
		std::cout << std::endl;

    }


    return 0;
}