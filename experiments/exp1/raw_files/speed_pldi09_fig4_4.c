void start(int n, int m)
{
  int i=n;

  assert(0 < m);

  while (i > 0) { // s7
    if (i < m) // s8
      i=i-1;
    else // s9
      i=i-m;
  }
}
