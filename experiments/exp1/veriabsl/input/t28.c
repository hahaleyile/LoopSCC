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

void start(int x, int y) {
    int x1 = x;
    int y1 = y;
    while (x1 > y1) {
        x1 = x1 - 1;
        x1 = x1 + 1000;
        y1 = y1 + 1000;
    }
    while (y1 > 0) {
        y1 = y1 - 1;
    }
    while (x1 < 0) {
        x1 = x1 + 1;
    }
    __VERIFIER_assert(x1 == {2});
    __VERIFIER_assert(y1 == {3});
}

int main() {
    int x = {0};
    int y = {1};
    start(x, y);
    return 0;

}