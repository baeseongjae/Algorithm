#include <iostream>
using namespace std;

int main()
{
    int arr[9]={0};
    int max;
    int index;

    for(int i=0;i<9;i++){
        cin>>arr[i];
    }
    max = arr[0];
    index = 1;

    for(int i=0;i<9;i++){
        if(max<arr[i+1]){
            max=arr[i+1];
            index=i+1+1;
        }
    }
    cout<<max<<'\n'<<index<<'\n';
}