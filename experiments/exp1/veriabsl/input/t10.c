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

void start(int x0, int y0, int det0){
    int x = x0;
    int y = y0;
    int det = det0;
    while(x > y){
        if(det){
            y = y + 1;
        } else {
            x = x - 1;
        }
    }
    __VERIFIER_assert(x == {3});
    __VERIFIER_assert(y == {4});
}

int main(){
    int x = {0};
    int y = {1};
    int det = {2};
    start(x,y,det);
    return 0;
}