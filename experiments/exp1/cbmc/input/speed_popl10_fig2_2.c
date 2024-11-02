#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)


void start(int x, int z) {
    while (x < 100) {
        if (z > x) {
            x = x + 1;
        } else {
            z = z + 1;
        }
    }
    assert(x == {2});
    assert(z == {3});
}

int main() {
    int x = {0};
    int z = {1};
    start(x, z);
    return 0;
}
