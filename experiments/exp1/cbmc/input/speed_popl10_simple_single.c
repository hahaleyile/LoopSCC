#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int x0, int det){
    int x = x0;
    while(x < 100){
        if(det){
            x = x + 1;
        } else {
            x = x + 1;
        }
    }
    assert(x == {2});
}

int main(){
    int x = {0};
    int det = {1};
    start(x,det);
    return 0;
}