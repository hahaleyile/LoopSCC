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

void start(int x0, int det){
    int x = x0;
    while(x < 100){
        if(det){
            x = x + 1;
        } else {
            x = x + 1;
        }
    }
    __VERIFIER_assert(x == {2});
}

int main(){
    int x = {0};
    int det = {1};
    start(x,det);
    return 0;
}