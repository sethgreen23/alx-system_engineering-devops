#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - main function
 * @argc: count argument
 * @argv: arguments
 *
 * Return: 0 on success
 */
int main(int argc, char **argv)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			exit(EXIT_FAILURE);
		}
		if (pid == 0)
		{
			printf("Zombie process created, PID: %ld\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - infinite loop
 *
 * Return: nothing
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
