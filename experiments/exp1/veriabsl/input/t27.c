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

void start(int n, int y) {
    while (n < 0) {
        n = n + 1;
        y = y + 1000;
        while (y >= 100) {
            y = y - 100;
        }
    }
    __VERIFIER_assert(n == {2});
    __VERIFIER_assert(y == {3});
}

int main() {
    int n = {0};
    int y = {1};
    start(n, y);
    return 0;
}