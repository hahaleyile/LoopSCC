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

void start(int i, int k){
    int temp = i;
    while(temp > 100){
        temp = temp - 1;
    }
    temp = temp + k + 50;
    while(temp >= 0){
        temp = temp - 1;
    }
    __VERIFIER_assert(temp == {2});
}

int main(){
    int i = {0};
    int k = {1};
    start(i, k);
    return 0;
}
