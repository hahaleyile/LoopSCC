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

void start(int n, int det){
    while(n > 0){
        n = n - 1;
        while(n > 0){
            if(det){
                break;
            }
            n = n - 1;
        }
    }
    __VERIFIER_assert(n == {2});
}

int main(){
    int n = {0};
    int det = {1};
    start(n, det);
    return 0;
}