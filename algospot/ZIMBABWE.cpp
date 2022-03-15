#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <cmath>

#include <algorithm>

int C;
std::string e, cards;
int visited;
int cache[1<<14][20][2];
int n, m;

const int MOD = 1000000007;

int pos_nums(int index, int taken, int remainder, int less){
    if (index == n)
        return (less && remainder==0) ? 1 : 0;

    int& ret = cache[taken][remainder][less];
    if (ret != -1) return ret;
    ret = 0;

    for (int next=0;next<n;next++){
        if ((taken & (1<<next)) == 0){
            if (!less && cards[next] > e[index]) continue;
            if (next>0 && ((taken & (1<<(next-1))) == 0) && cards[next-1] == cards[next]) continue;

            int next_taken = taken | (1<<next);
            int next_remainder = (remainder*10 + cards[next] - '0') % m;
            int next_less = less || (e[index] > cards[next]);
            ret += pos_nums(index+1, next_taken, next_remainder, next_less);
            ret %= MOD;
        }
    }
    return ret;
}

int main(){
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0);

    std::ifstream ifs;
    ifs.open("ZIMBABWE-1.txt");

    ifs >> C;
    while (C--){
        ifs >> e >> m;
        n = e.size();
        std::vector<int> cards_;
        long long num = std::stoll(e);
        while (num > 0){
            cards_.push_back(num%10);
            num /= 10;
        }
        std::sort(cards_.begin(), cards_.end());
        cards = "";
        for (int i=0;i<cards_.size();i++)
            cards += std::to_string(cards_[i]);

        memset(cache, -1, sizeof(cache));

        std::cout << pos_nums(0, 0, 0, 0) << std::endl;
        // std::cout << pos_nums(e, visited) << std::endl;

    }


    return 0;
}