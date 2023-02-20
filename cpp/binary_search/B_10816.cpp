#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int counter=0;
vector<int> n_v,m_v;
int bin(int min,int max,int target){
    if(min>max){
        return 0;
    }
    else{
        int h = (min+max)/2;
        if (target==n_v[h]){
            counter++;
        }
        if(n_v[h-1]>=target){
            // cout << h-1 << endl;
            bin(min,h-1,target);
        }
        if(n_v[h+1]<=target){
            // cout <<h+1<< endl;
            bin(h+1,max,target);
        }
       
    }
    return 0;
}
int main(){
    int n,m;
    
    cin >> n;
    for(int i=0; i<n;i++){
        int buf;
        cin >> buf;
        n_v.push_back(buf);
    }
    cin >> m;
    for(int i=0; i<m; i++){
        int buf;
        cin >> buf;
        m_v.push_back(buf);
    }
    sort(n_v.begin(),n_v.end());

    for(int i=0; i<m; i++){
        // cout << "find: "<<m_v[i]<<endl;
        bin(0,n-1,m_v[i]);
        cout << counter << " ";
        counter=0;
    }
    return 0;
}