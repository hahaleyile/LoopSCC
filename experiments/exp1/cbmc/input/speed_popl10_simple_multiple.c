#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int x0, int y0){
    int x = x0;
    int y = y0;
    while(x < 100){
        if(y < 30){
            y = y + 1;
        } else {
            x = x + 1;
        }
    }
    assert(x == {2});
    assert(y == {3});
}

int main(){
    int x = {0};
    int y = {1};
    start(x,y);
    return 0;
}