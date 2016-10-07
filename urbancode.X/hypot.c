float fuckoff_abs(float x);
float close_enough(float x, float g);
float better_guess(float a, float b);
float test(float x, float g);
float sqrt(float x);
float fuckoff_hypot(float x, float y);


float fuckoff_abs(float x)
{
	return x < 0 ? -x : x;
}

float close_enough(float a, float b)
{
	return fuckoff_abs(a - b) < 0.000001;
}

float better_guess(float x, float g)
{
	return ((g + x / g) / 2);
}

float test(float x, float g)
{
    while (!close_enough(x/g, g))
        g = better_guess(x, g);
    return g;
    /*
	if (close_enough(x/g, g))
		return g;
	else
		return test(x, better_guess(x, g));*/
}

float sqrt(float x)
{
	return test(x, x);
}

float fuckoff_hypot(float x, float y)
{
	return ((float)(sqrt(x*x+y*y)));
}