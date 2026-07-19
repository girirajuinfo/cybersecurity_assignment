#include <stdio.h>

int main() {
    int port = 80;
    int *ptr = &port;

    printf("Port: %d\n", port);
    printf("Using pointer: %d\n", *ptr);

    *ptr = 443;

    printf("New Port: %d\n", port);

    return 0;
}
