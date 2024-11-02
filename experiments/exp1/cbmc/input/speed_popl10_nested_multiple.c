#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int x, int y, int det){
    while(x < 100){
        while(y < 30){
            if(det != 0){
                break;
            }
            y = y + 1;
        }
        x = x + 1;
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