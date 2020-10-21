// 메모장 입력으로 받기
 #include <fstream>

int main(void) {
     테스트 케이스(Test Case) 입력
     ifstream cin;

     cin.open("DP-금광.txt");

     cin >> testCase;
     }
// 원래
 ifstream fin;

 fin.open("DP-금광.txt");

 fin >> testCase;
// 이래야 하지만 문제는 콘솔 cin으로 받으니까 변수 덮어 씌운거임

// 이진탐색 내장함수
//https://blockdmask.tistory.com/168
// 파이썬의 bisect
// lower_bound = bisect_left
// upper_boud = bisect_right
using namespace std;
#include<algorithm> //헤더파일
int main(void){
    int arr[10] = {1, 2, 4, 5, 6, 6, 7, 7, 7, 9};

    cout << "lower_bound(6) : " << lower_bound(arr, arr + 10, 6) - arr + 1<< endl;
    cout << "lower_bound(7) : " << lower_bound(arr, arr + 10, 7) - arr + 1<< endl;
    cout << "lower_bound(8) : " << lower_bound(arr, arr + 10, 8) - arr + 1<< endl;
    cout << "lower_bound(9) : " << lower_bound(arr, arr + 10, 9) - arr + 1<< endl;
    return 0;
}

int main(void){
    int arr[10] = {1, 2, 4, 5, 6, 6, 7, 7, 7, 9};

    cout << "upper_bound(6) : " << upper_bound(arr, arr + 10, 6) - arr + 1<< endl;
    cout << "upper_bound(7) : " << upper_bound(arr, arr + 10, 7) - arr + 1<< endl;
    cout << "upper_bound(8) : " << upper_bound(arr, arr + 10, 8) - arr + 1<< endl;
    cout << "upper_bound(9) : " << upper_bound(arr, arr + 10, 9) - arr + 1<< endl;
    return 0;
}

// 배열 출력 함수
void printarr(int arr[],int len){
  for (int i=0;i<len;i++){
    cout << arr[i] << " ";
  }
  cout << endl;
};
printarr(LIS,n);

// 배열 원소 최소, 최대값 출력
//http://blog.naver.com/kks227/220246803499
#include <iostream>
#include <algorithm>
using namespace std;

int main(){

 int size;
 cin >> size;

 int *arr = new int[size];
 for(int i=0; i<size; i++){
  cin >> arr[i];
 }
 cout << "max값: " << *max_element(arr, arr+size) << endl;
 cout << "min값: " << *min_element(arr, arr+size) << endl;

 delete[] arr;
 return 0;
}

// 입력 빠르게 받기
//https://shjz.tistory.com/31
#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int num;
    cin>>num;
    for(int i=1;i<=num;i++){
        cout<<i<<'\n';
    }
    return 0;
}
