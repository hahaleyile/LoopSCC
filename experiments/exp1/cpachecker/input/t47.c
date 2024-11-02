#include <assert.h>

void start(int n){
    int flag = 1;
    while(flag > 0){
        if(n > 0){
            n = n - 1;
            flag = 1;
        } else {
            flag = 0;
        }
    }
    assert(n == {1});
    assert(flag == {2});
}

int main(){
    int n = {0};
    start(n);
    return 0;
}