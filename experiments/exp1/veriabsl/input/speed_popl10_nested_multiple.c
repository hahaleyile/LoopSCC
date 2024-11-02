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

void start(int x, int y, int det){
    while(x < 100){
        while(y < 30){
            if(det != 0){
                break;
            }
            y = y + 1;
        }
        x = x + 1;
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