#include <assert.h>
extern void abort(void);
void reach_error() { __VERIFIER_assert(0); }
extern int __VERIFIER_nondet_int(void);

void start(int t, int x, int y) {
    while (t > 0) {
        if (x > y) {
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
