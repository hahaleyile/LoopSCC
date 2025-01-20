void func(int t)
{
    int d=1;
    while(t>0)
    {
        if(d==1)
        {
            d-=2;
        }
        else if(d==-1)
        {
            d+=2;
        }
        t-=1;
    }
    return;
}

int main()
{
    return 0;
}
