#include <assert.h>
extern void abort(void);
void reach_error() { __VERIFIER_assert(0); }
extern int __VERIFIER_nondet_int(void);

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
