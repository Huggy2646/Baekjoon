#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> n_v,m_v;
int bin(int min, int max, int target){
    int result = 0;
    int h= (min+max)/2;
    if(min>max){
        return 0;
    }
    else{
        if(n_v[h]==target)
            return 1;
        else if(n_v[h]<target)
            result = bin(h+1,max,target);
        else
            result = bin(min,h-1,target);
    }
    return result;
}
int main(){
    int n,m;
    cin >> n;
    for(int i=0; i<n; i++){
        int buf_n;
        cin >> buf_n;
        n_v.push_back(buf_n);
    }
    sort(n_v.begin(),n_v.end());
    cin >> m;
    for(int i=0; i<m; i++){
        int buf_m;
        cin >> buf_m;
        m_v.push_back(buf_m);
    }
    for(int i=0; i<m; i++){
        cout << bin(0,n-1,m_v[i])<<" ";
    }
    return 0;
}