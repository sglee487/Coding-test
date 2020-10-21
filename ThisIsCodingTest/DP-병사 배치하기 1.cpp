#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <algorithm>

using namespace std;

int TestCase;
int n;
vector<int> v;

void printarr(int arr[],int len){
  for (int i=0;i<len;i++){
    cout << arr[i] << " ";
  }
  cout << endl;
};

int main(){
  ifstream cin;

  cin.open("DP-병사 배치하기.txt");
  cin >> TestCase;
  for (int TC=0; TC<TestCase; TC++){
    cin >> n;
    for (int i=0; i<n; i++){
      int x;
      cin >> x;
      v.push_back(x);
    }

    reverse(v.begin(), v.end());

    int C[n+1];
    for (int i=0; i<n+1; i++){
      C[i] = 10000001;
    }
    C[0] = 0;
    int LIS[n];
    for (int i=0; i<n;i++){
      LIS[i] = 1;
    }

    int c_index = 0;
    int num;
    for (int i=0;i<n;i++){
      num = v[i];
      c_index = lower_bound(C, C+n, num) - C;
      C[c_index] = num;
      LIS[i] = c_index;
      // c_index = lower_bound(C,C+1,0);
      // printarr(C,n+1);
      // printarr(LIS,n);
    }
    // printarr(LIS,n);
    cout << n-*max_element(LIS, LIS + n) << endl;
  }
  
}