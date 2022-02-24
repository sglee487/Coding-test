#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C;
int N, W;
std::string names[100];
int v[100];
int q[100];
int cache[1001][100];


int dfs(int capacity, int item_index){
    if (item_index == N) return 0;

    int &ret = cache[capacity][item_index];
    if (ret != -1) return ret;
    ret = 0;
    if (capacity >= v[item_index])
        ret = std::max(ret, dfs(capacity-v[item_index], item_index+1)+q[item_index]);
    ret = std::max(ret, dfs(capacity, item_index+1));
    
    return ret;
}

void make_records(int capacity, int item_index, std::vector<int> &records){
    if (item_index == N) return;
    if (dfs(capacity, item_index) == dfs(capacity, item_index+1))
        make_records(capacity, item_index+1, records);
    else{
        records.push_back(item_index);
        make_records(capacity - v[item_index], item_index+1, records);
    }
}

int main(){

    std::ifstream ifs;
    ifs.open("PACKING-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        memset(cache, -1, sizeof(cache));
        ifs >> N >> W;
        for (int i=0;i<N;i++){
            ifs >> names[i] >> v[i] >> q[i];
        }
        std::cout << dfs(W, 0) << " ";
        std::vector<int> records;
        make_records(W, 0, records);
        std::cout << records.size() << std::endl;
        for (int i=0;i<records.size();i++)
            std::cout << names[records[i]] << std::endl;
    }

    return 0;
}