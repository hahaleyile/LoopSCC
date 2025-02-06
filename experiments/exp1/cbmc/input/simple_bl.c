#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)

void start(int t){
    int d=1;
    while(t>0){
        if(d*d==1){
            d=-d;
        } else {
            d=5;
        }
        t --;
    }
    assert(t=={1});
    assert(d=={2});
}


int main() {
    int t={0};
    start(t);
    return 0;
}
