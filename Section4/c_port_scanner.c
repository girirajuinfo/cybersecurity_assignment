#include <stdio.h>
#include <string.h>
#include <arpa/inet.h>
#include <unistd.h>

int scan_port(int port) {
    int sock;
    struct sockaddr_in target;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) return -1;

    target.sin_family = AF_INET;
    target.sin_port = htons(port);
    target.sin_addr.s_addr = inet_addr("127.0.0.1");

    int result = connect(sock, (struct sockaddr *)&target, sizeof(target));

    close(sock);

    if (result == 0)
        return 1;
    else
        return 0;
}

int main() {
    int ports[] = {22, 80, 443, 3306};

    printf("Scanning localhost (127.0.0.1)...\n");

    for (int i = 0; i < 4; i++) {
        if (scan_port(ports[i]))
            printf("Port %d: OPEN\n", ports[i]);
        else
            printf("Port %d: CLOSED\n", ports[i]);
    }

    return 0;
}
