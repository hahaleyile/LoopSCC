#include <assert.h>
#undef assert
#define assert(C) __CPROVER_assert((C), "assertion"); __CPROVER_assume(C)

void start(int t, int x, int y) {
    int flag = 1;
    while (t > 0) {
        if (flag == 1) {
            x++;
            flag = -1;
        } else {
            y++;
            flag = 1;
        }
        t--;
    }
    assert(t == {3});
    assert(x == {4});
    assert(y == {5});
    assert(flag == {6});
}


int main() {
    int t={0},x={1}, y={2};
    start(t, x, y);
    return 0;
}
