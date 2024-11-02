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

void start(int n){
    int flag = 1;
    while(flag > 0){
        if(n > 0){
            n = n - 1;
            flag = 1;
        } else {
            flag = 0;
        }
    }
    __VERIFIER_assert(n == {1});
    __VERIFIER_assert(flag == {2});
}

int main(){
    int n = {0};
    start(n);
    return 0;
}