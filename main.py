import starfleet;

x = '';

while x != 'cmd(_close_)':
  x = starfleet.library(input('Search for '));
  print('Result:');
  print(x);
