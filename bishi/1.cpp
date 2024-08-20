#include <stdio.h>
#include <stdbool.h>

bool isValid(char *s)
{
  char mp[128] = {};
  mp[')'] = '(';
  mp[']'] = '[';
  mp['}'] = '{';

  int top = 0;
  for (int i = 0; s[i]; i++)
  {
    char c = s[i];
    if (mp[c] == 0)
    {
      s[top++] = c;
    }
    else if (top == 0 || s[--top] != mp[c])
    {
      return false;
    }
  }
  return top == 0;
}

int main()
{
  char input[] = "{[()]}";
  if (isValid(input))
  {
    printf("Valid\n");
  }
  else
  {
    printf("Invalid\n");
  }
  return 0;
}
