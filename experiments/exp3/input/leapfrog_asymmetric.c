void func(int x,int y,int t)
{
    while(t>0)
    {
        if(x==y+1)
        {
            y=y+2;
        }
        else
        {
            x=x+2;
        }
        t=t-1;
    }
    return;
}

int main()
{
    return 0;
}
