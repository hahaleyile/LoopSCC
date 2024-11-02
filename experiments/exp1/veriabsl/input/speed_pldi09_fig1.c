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
void start(int x0, int y0) {
    int x = x0;
    int y = y0;
    while (1) {
        if (x < 100) {
            y = y + 1;
            x = x + 1;
        } else if (y > 0) {
            y = y - 1;
        } else {
            break;
        }
    }
    __VERIFIER_assert(x=={2});
    __VERIFIER_assert(y=={3});
}

int main() {
    int x ={0},y={1};
    start(x, y);
    return 0;
}
