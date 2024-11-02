#include <assert.h>

void start(int n){
    int flag = 1;
    while(flag > 0){
        flag = 0;
        while(n > 0){
            n = n - 1;
            flag = 1;
        }
    }
    assert(flag == {1});
    assert(n == {2});
}

int main(){
    int n = {0};
    start(n);
    return 0;
}
