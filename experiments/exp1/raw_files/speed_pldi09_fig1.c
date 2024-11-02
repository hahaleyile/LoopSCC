void start(int n)
{
  int x=0;
  int y=0;

  for (;;) { 
    if (x < n) { // s4
      y=y+1; // s5
      x=x+1;
    } else if (y > 0) // s7
      y=y-1;
    else
      break;
  }
}
