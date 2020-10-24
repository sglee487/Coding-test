#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <algorithm>
#define INF 1e9

using namespace std;

void printarr(int arr[],int len){
  for (int i=0;i<len;i++){
    cout << arr[i] << " ";
  }
  cout << endl;
};

int TestCase;
int N, M, C;
vector<pair<int, int>> graph[100001];
int d[100001];
void dijkstra(int start){
  priority_queue<pair<int, int>> pq;
  pq.push({0,start});
  d[start] = 0;
  while (!pq.empty()){
    int dist = -pq.top().first;
    int now = pq.top().second;
    pq.pop();
    if (d[now] < dist) continue;
    for (int i=0; i < graph[now].size(); i++){
      int cost = dist + graph[now][i].second;
      if (cost < d[graph[now][i].first]){
        d[graph[now][i].first] = cost;
        pq.push({-cost,graph[now][i].first});
      }
    }
  }
}

int main(){
  ifstream cin;

  cin.open("최단경로-전보.txt");
  cin >> TestCase;
  for (int TC=0; TC<TestCase; TC++){
    cin >> N >> M >> C;
    for (int i=0; i < M; i++){
      int X, Y, Z;
      cin >> X >> Y >> Z;
      graph[X].push_back({Y,Z});
    }
    fill(d, d+100001, INF);
    dijkstra(C);
    // printarr(d,N+1);
    int count = 0;
    int maxvalue = 0;
    for (int i=1; i <= N; i++){
      if (d[i] != 0 && d[i] != INF){
        count++;
        maxvalue = max(d[i],maxvalue);
      }
    }
    cout << count << ' ' << maxvalue << '\n';
  }
  
}
