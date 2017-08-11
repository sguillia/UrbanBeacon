
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

typedef struct	urban_s
{
		float lat;
		float lon;
		float alt;
		unsigned char str[19];
		unsigned char active;
}				urban_t;

int main()
{
	urban_t test;

	memset(&test.str, 0, 19);
	test.lat = 4.5;
	test.lon = 6.7;
	test.alt = 8.9;
	test.str[0] = 'o';
	test.str[1] = 'k';
	test.str[2] = '\0';
	test.active = 10;

	int fd = open("data", O_CREAT | O_WRONLY | O_TRUNC, 0644);
	if (fd < 0)
		exit(1);
	int ret = write(fd, &test, sizeof(urban_t));
	printf("%d bytes written\n", ret);
	close(fd);

	return (0);
}
