#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

int C;
int clocks[16];
int global_min_count;

const int INF = 987654321;

std::vector<std::vector<int>> CLOCK_SYNCS = {
    {0,1,2},
    {3,7,9,11},
    {4,10,14,15},
    {0,4,5,6,7},
    {6,7,8,10,12},
    {0,2,14,15},
    {3,14,15},
    {4,5,7,14,15},
    {1,2,3,4,5},
    {3,4,5,9,13}
};

std::map<int, int> CTN = {
    {12,0}, {3,1}, {6,2}, {9,3}
};


bool is_all_clock(int clocks[]){
    for (int i=0;i<16;i++) 
        if (clocks[i] != 0) return false;
    return true;
}

void turn_clock(int button, int clocks[]){
    for (int e:CLOCK_SYNCS[button])
        clocks[e] = (clocks[e] + 1) % 4;
    return;
}

void dfs(int step, int count, int clocks[]){
    if (step == 10){
        if (is_all_clock(clocks))
            global_min_count = std::min(global_min_count, count);
        return;
    }
    for (int i=0;i<4;i++){
        dfs(step+1, count+i, clocks);
        turn_clock(step, clocks);
    }

    return;
}

int main(){

    std::ifstream ifs;
    ifs.open("CLOCKSYNC.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        for (int i=0;i<16;i++) {
            int num;
            ifs >> num;
            clocks[i] = CTN[num];
        }
        global_min_count = INF;
        dfs(0,0, clocks);

        if (global_min_count == INF)
            std::cout << -1 << std::endl;
        else
            std::cout << global_min_count << std::endl;

    }

    return 0;
}