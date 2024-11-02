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

void start(int i0, int det) {
    int i = i0;
    int n = 100;
    int j;
    while (i < n) {
        while (j < n) {
            if (det) {
                j = j - 1;
                n = n - 1;
            }
            j = j + 1;
        }
        i = i + 1;
    }
    __VERIFIER_assert(i == {2});
    __VERIFIER_assert(n == {3});
    __VERIFIER_assert(j == {4});
}

int main() {
    int i = {0};
    int det = {1};
    start(i, det);
    return 0;
}
