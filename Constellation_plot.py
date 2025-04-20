void save_constellation(const char* filename) {
    FILE *f = fopen(filename, "w");
    if (f == NULL) {
        printf("Error opening constellation file.\n");
        return;
    }

    for (int i = 0; i < N; i++) {
        fprintf(f, "%f,%f\n", noisy_I[i], noisy_Q[i]);
    }

    fclose(f);
}
