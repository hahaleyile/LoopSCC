#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)

void start(int t, int x, int y) {
    while(t > 0) {
        if(x == y + 1) {
            y += 2;  // Increment y by 2
        } else {
            x += 2;  // Increment x by 2
        }
        t--;
    }
    
    assert(t == {3});
    assert(x == {4});
    assert(y == {5});
}


int main() {
    int t={0},x={1}, y={2};
    start(t, x, y);
    return 0;
}
