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

void start(int i0){
    int i = i0;
    while(i > 0){
        if(i < 1000000){
            i = i - 1;
        } else {
            i = i - 1000000;
        }
    }
    __VERIFIER_assert(i == {1});
}

int main(){
    int i = {0};
    start(i);
    return 0;
}