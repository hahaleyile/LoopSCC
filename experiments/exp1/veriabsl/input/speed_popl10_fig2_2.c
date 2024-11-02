#include <assert.h>
extern void abort(void);
#include <assert.h>
void reach_error() { __VERIFIER_assert(0); }
extern int __VERIFIER_nondet_int(void);

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: {reach_error();abort();}
  }
  return;
}

void start(int x, int z) {
    while (x < 100) {
        if (z > x) {
            x = x + 1;
        } else {
            z = z + 1;
        }
    }
    __VERIFIER_assert(x == {2});
    __VERIFIER_assert(z == {3});
}

int main() {
    int x = {0};
    int z = {1};
    start(x, z);
    return 0;
}
