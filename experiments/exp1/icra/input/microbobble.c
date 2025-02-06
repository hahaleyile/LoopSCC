#include <assert.h>


void start(int t, int b){
    int flag=1;
    while(t>0){
        if(flag==1){
            b-=1;
            flag=0;
        }
        else if(flag==0){
            b+=1;
            flag=1;
        }
        t-=1;
    }
    assert(t == {2});
    assert(b == {3});
    assert(flag == {4});
}


int main() {
    int t={0}, b={1};
    start(t, b);
    return 0;
}