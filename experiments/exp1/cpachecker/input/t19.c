#include <assert.h>

void start(int i, int k){
    int temp = i;
    while(temp > 100){
        temp = temp - 1;
    }
    temp = temp + k + 50;
    while(temp >= 0){
        temp = temp - 1;
    }
    assert(temp == {2});
}

int main(){
    int i = {0};
    int k = {1};
    start(i, k);
    return 0;
}
