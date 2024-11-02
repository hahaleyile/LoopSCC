#include <assert.h>

void start(int x0, int y0){
    int x = x0;
    int t;
    int y = y0;
    while(x > 0){
        x = x - 1;
        t = x;
        x = y;
        y = t;
    }
    assert(x == {2});
    assert(y == {3});
    assert(t == {4});
}

int main(){
    int x = {0};
    int y = {1};
    start(x,y);
    return 0;
}