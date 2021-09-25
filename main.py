import starfleet;


x = 0;
print("Welcome to the interactive Starfleet Ship Library.");

while x != 1:
    x = starfleet.library(input("Name / Regristrierungnummer: "));
    print(x);
