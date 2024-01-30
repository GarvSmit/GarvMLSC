#include <stdio.h>
#include <unistd.h>

void printProgressBar(int progress, int total) {
    const int barWidth = 50;
    float percentage = ((float)progress / total) * 100;
    int bars = (int)(percentage * barWidth / 100);

    printf("[");
    for (int i = 0; i < barWidth; ++i) {
        if (i < bars) {
            printf("=");
        } else {
            printf(" ");
        }
    }

    printf("] %.2f%%\r", percentage);
    fflush(stdout);
}

int main() {
    const int totalIterations = 100;

    for (int i = 0; i <= totalIterations; ++i) {
        printProgressBar(i, totalIterations);
        usleep(100000); // Sleep for 100 milliseconds (adjust as needed)
    }

    printf("\nProgress complete!\n");

    return 0;
}
