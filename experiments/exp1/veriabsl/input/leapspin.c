#include <assert.h>
extern void abort(void);
void reach_error() { __VERIFIER_assert(0); }
extern int __VERIFIER_nondet_int(void);


void start(int t){
    int d=1;
    while(t>0){
        if(d==1){
            d-=2;
        }
        else if(d==-1){
            d+=2;
        }
        t-=1;
    }
    assert(t=={1});
    assert(d=={2});
}



int main() {
    int t={0};
    start(t);
    return 0;
}
