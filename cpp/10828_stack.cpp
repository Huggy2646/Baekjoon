#include <iostream>
#include <string>
using namespace std;

class Stack{
    int top_index=-1;
    int * stack;
    public:
        Stack(int n){stack= new int[n];}
        void push(int x){
            stack[++top_index]=x;
        }
        void pop(){
            if(top_index==-1){
                cout<<top_index<<endl;
            }
            else{
                cout << stack[top_index]<<endl;
                stack[top_index--]=0;
            }
        }
        void size(){
            cout << top_index+1<<endl;
        }
        void empty(){
            if(top_index==-1) cout << 1<<endl;
            else cout <<0<<endl;
        }
        void top(){
            if(top_index==-1) cout << -1<<endl;
            else cout << stack[top_index]<<endl;
        }

};

int main(){
    int n=0;
    string cmd="";
    cin >> n;
    cin.ignore();
    Stack stack(n);
    for(int i=0; i<n;i++){
        getline(cin,cmd,'\n');
        
        int index=cmd.find(" ");
        if(index==-1){
            if(cmd=="pop") stack.pop();
            else if(cmd=="size") stack.size();
            else if(cmd=="empty") stack.empty();
            else if(cmd=="top") stack.top();
        }
        else{
            string push=cmd.substr(0,index+1);
            int digit = stoi(cmd.substr(index+1));
            stack.push(digit);
            // cout <<"command: "<<push<<" digit: "<<digit<<endl;
        }
    }
    return 0;
}