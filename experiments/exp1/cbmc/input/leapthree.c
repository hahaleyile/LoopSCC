#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)

void start(int t){
    int x=2, y=1;
    while(t > 0){
        if(x - y == 1){
            y += 2;  // Increment y by 2
        } else if(y - x == 1){
            x += 2;  // Increment x by 2
        }
        t--;
    }
    assert(t=={1});
    assert(x=={2});
    assert(y=={3});
}


int main() {
    int t={0};
    start(t);
    return 0;
}
