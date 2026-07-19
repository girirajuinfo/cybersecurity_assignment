#include <stdio.h>
#include <string.h>

int main() {
    char buffer[16];

    printf("Enter input: ");
    fgets(buffer, sizeof(buffer), stdin);

    printf("You entered: %s\n", buffer);

    return 0;
}

/*
Answers:

1. What happens with long input?
If input is longer than buffer, extra characters are not stored (safe handling).

2. Why is gets() dangerous?
It does not check size → causes buffer overflow.

3. Fix:
Use fgets() which limits input size.
*/
