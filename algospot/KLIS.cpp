#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <cmath>

#include <algorithm>

int C;
int N,K;
int L[502];
int lis_cache[502];
int count_cache[502];
int choices[502];

const int MAX = 2000000000 + 1;

int get_lis(int cur){
    int &ret = lis_cache[cur+1];
    if (ret != -1) return ret;
    ret = 1;
    int bestnxt = -1;
    int cand = -1;
    for (int nxt=cur+1;nxt<N;nxt++){
        if (cur == -1 || L[cur] < L[nxt]){
            cand = get_lis(nxt)+1;
            if (cand > ret){
                bestnxt = nxt;
                ret = cand;
            }
        }
    }
    choices[cur+1] = bestnxt;
    return ret;

}

int get_count(int cur){
    if (get_lis(cur) == 1) return 1;
    int &ret = count_cache[cur+1];
    if (ret != -1) return ret;
    ret = 0;
    for (int nxt=cur+1;nxt<N;nxt++){
        if ((L[cur] < L[nxt] && get_lis(cur) == get_lis(nxt)+1)){
            ret = std::min<long long>(MAX, (long long)ret + get_count(nxt));
        }
    }
    return ret;
}

void reconstruct(int now, int k, std::vector<int>& lis){
    if (now != -1) lis.push_back(L[now]);

    std::vector<std::pair<int,int>> next_numinds;
    for (int nxt=now+1;nxt<N;nxt++)
        if ((now == -1 || L[now] < L[nxt]) && get_lis(now) == get_lis(nxt)+1){
            next_numinds.push_back(std::make_pair(L[nxt],nxt));
        }
    std::sort(next_numinds.begin(), next_numinds.end());
    for (int i=0;i<next_numinds.size();i++){
        int next_index = next_numinds[i].second;
        if (get_count(next_index) < k)
            k -= get_count(next_index);
        else{
            reconstruct(next_index, k, lis);
            break;
        }
    }
    return;
}

int main(){
    std::ios_base::sync_with_stdio(0);
	std::cin.tie(0);

    std::ifstream ifs;
    ifs.open("KLIS-1.txt");

    ifs >> C;
    while (C--){
        ifs >> N >> K;
        for (int i=0;i<N;i++)
            ifs >> L[i];
        memset(lis_cache,-1,sizeof(lis_cache));
        memset(count_cache,-1,sizeof(count_cache));
        int lis_len = get_lis(-1)-1;
        int count_len = get_count(-1)-1;

        std::cout << lis_len << std::endl;

        std::vector<int> lis;
        reconstruct(-1, K, lis);
        for (int i=0;i<lis.size();i++) std::cout << lis[i] << " ";
        std::cout << std::endl;


    }


    return 0;
}