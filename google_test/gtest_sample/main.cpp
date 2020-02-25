#include <stdio.h>
#include "gtest/gtest.h"

#if 0
int main(int argc, char **argv) {

	printf("I am Demo App!\n");

	return 0;
}
#endif

TEST(TestSuite, TestCase11)
{
	EXPECT_EQ(1,1);
}

TEST(TestSuite2, TestCase21)
{
	EXPECT_EQ(6,6);
	EXPECT_EQ(7,7);
	EXPECT_EQ(8,8);
	EXPECT_EQ(1,1);
}

TEST(TestSuite2, TestCase22)
{
}

