#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int i0, int dir) {
    int i = i0;
    while (i > 0 && i < 1000000) {
        if (dir == 1) {
            i = i + 1;
        } else {
            i = i - 1;
        }
    }
    assert(i == {2});
}

int main() {
    int i = {0};
    int dir = {1};
    start(i, dir);
    return 0;
}
