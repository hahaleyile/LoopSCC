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

void start(int y0, int z0){
    int y = y0;
    int z = z0;
    while(z > y){
        y = y + 1;
    }
    while(y > 2){
        y = y - 3;
    }
    __VERIFIER_assert(y == {2});
}

int main(){
    int y = {0};
    int z = {1};
    start(y,z);
    return 0;
}