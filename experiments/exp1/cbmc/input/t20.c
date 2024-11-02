#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int x, int y){
    while(x < y){
        x = x + 1;
    }
    while(y < x){
        y = y + 1;
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