#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int x0, int y0, int det0){
    int x = x0;
    int y = y0;
    int det = det0;
    while(x > y){
        if(det){
            y = y + 1;
        } else {
            x = x - 1;
        }
    }
    assert(x == {3});
    assert(y == {4});
}

int main(){
    int x = {0};
    int y = {1};
    int det = {2};
    start(x,y,det);
    return 0;
}