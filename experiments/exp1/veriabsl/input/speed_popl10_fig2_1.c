#include <assert.h>
extern void abort(void);
void reach_error() { __VERIFIER_assert(0); }
extern int __VERIFIER_nondet_int(void);

void __VERIFIER_assert(int cond) {
  if (!(cond)) {
    ERROR: {reach_error();abort();}
  }
  return;
}

void start(int x, int y){
    while(100 > x){
        if(30 > y){
            y = y + 1;
        } else {
            x = x + 1;
        }
    }
    __VERIFIER_assert(x == {2});
    __VERIFIER_assert(y == {3});
}

int main(){
    int x = {0};
    int y = {1};
    start(x,y);
    return 0;
}
