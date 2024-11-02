#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int n, int det){
    while(n > 0){
        n = n - 1;
        while(n > 0){
            if(det){
                break;
            }
            n = n - 1;
        }
    }
    assert(n == {2});
}

int main(){
    int n = {0};
    int det = {1};
    start(n, det);
    return 0;
}