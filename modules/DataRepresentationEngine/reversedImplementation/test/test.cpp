#include <gtest/gtest.h>

extern "C" {
#include <data.h>
}

#define MAX_LEN 1024

#ifdef REVERSE_LINKED_LIST
// PRIVATE_BEGIN
void testReversedLinkedList(DataNode *node, const char *str, int l, int origin) {
  int i = 0;
  int j = 0;
  const char *message = origin
                            ? "The original data should not be changed"
                            : "The return data has wrong linkedList of numbers";
  int str_len = strlen(str);
  for (i = str_len - 1; node != NULL && i >= 0; node = node->next, i--) {
    EXPECT_EQ(node->number, str[i]) << message;
    j++;
  }
  // After the loop, i should be -1 for a full match, and node should be NULL.
  EXPECT_TRUE(node == NULL && i == -1) << "Mismatch or incorrect length in reverse list";
  if (!origin) {
    EXPECT_EQ(l, j)
        << "The returned data should have a linkedList with length " << j;
  }
}

TEST(ProjectTests, Convert_to_base_2) {
  DataNode b0 = {'5', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data d205;
  d205.base = 10;
  d205.sign = 0;
  d205.len = 3;
  d205.number_bits = 8;
  d205.data = &b2;

  Data b = convert_to_base_n(d205, 2);

  EXPECT_EQ(b.base, 2)
      << "The return data of convert_to_base_n function is not base 2";
  EXPECT_EQ(b.sign, 0) << "The return data of convert_to_base_n function "
                          "should have the same sign";
  EXPECT_EQ(b.number_bits, 8) << "The return data of convert_to_base_n "
                                 "function should have the same number_bits";
  EXPECT_EQ(b.len, 8) << "The return data of convert_to_base_n function should "
                         "have a linkedList with length 8";
  DataNode *node = b.data;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '0') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '0') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '0') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_TRUE(node == NULL)
      << "The return data of convert_to_base_n function has "
         "wrong linkedList of numbers";
}
TEST(ProjectTests, Convert_to_base16) {
  DataNode b0 = {'5', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = convert_to_base_n(src, 16);
  EXPECT_EQ(b.base, 16)
      << "The return data of convert_to_base_n function is not base 16";
  EXPECT_EQ(b.sign, src.sign)
      << "The return data of convert_to_base_n function "
         "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of convert_to_base_n "
         "function should have the same number_bits";
  testReversedLinkedList(b.data, "CD", b.len, 0);
  testReversedLinkedList(src.data, "502", src.len, 1);
}
TEST(ProjectTests, Convert_to_base5) {
  DataNode b0 = {'8', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'1', &b1};

  Data src;
  src.base = 10;
  src.sign = 1;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = convert_to_base_n(src, 5);
  EXPECT_EQ(b.base, 5)
      << "The return data of convert_to_base_n function is not base 5";
  EXPECT_EQ(b.sign, src.sign)
      << "The return data of convert_to_base_n function "
         "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of convert_to_base_n "
         "function should have the same number_bits";
  testReversedLinkedList(b.data, "413", b.len, 0);
  testReversedLinkedList(src.data, "801", src.len, 1);
}
TEST(ProjectTests, Convert_to_base12) {
  DataNode b0 = {'7', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'1', &b1};

  Data src;
  src.base = 8;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = convert_to_base_n(src, 12);
  EXPECT_EQ(b.base, 12)
      << "The return data of convert_to_base_n function is not base 12";
  EXPECT_EQ(b.sign, src.sign)
      << "The return data of convert_to_base_n function "
         "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of convert_to_base_n "
         "function should have the same number_bits";
  testReversedLinkedList(b.data, "5B", b.len, 0);
  testReversedLinkedList(src.data, "701", src.len, 1);
}
TEST(ProjectTests, ConvertSame) {
  DataNode b0 = {'1', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'1', &b1};

  Data src;
  src.sign = 1;
  src.len = 3;
  src.number_bits = 32;
  src.data = &b2;

  Data b;
  for (int nb = 2; nb <= 16; nb++) {
    src.base = nb;
    b = convert_to_base_n(src, nb);
    EXPECT_EQ(b.base, nb)
        << "The return data of convert_to_base_n function is not base " << nb;
    EXPECT_EQ(b.sign, src.sign)
        << "The return data of convert_to_base_n function "
           "should have the same sign";
    EXPECT_EQ(b.number_bits, src.number_bits)
        << "The return data of convert_to_base_n "
           "function should have the same number_bits";
    testReversedLinkedList(b.data, "101", b.len, 0);
  }
  testReversedLinkedList(src.data, "101", src.len, 1);
}
TEST(ProjectTests, LeftShift1) {
  DataNode b0 = {'5', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = left_shift(src, 1);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of left_shift "
         "function should have the same number_bits";
  testReversedLinkedList(b.data, "110011010", b.len, 0);
  testReversedLinkedList(src.data, "502", src.len, 1); // src should not be changed
}
TEST(ProjectTests, LeftShift3) {
  DataNode b0 = {'7', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = left_shift(src, 3);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of left_shift "
         "function should have the same number_bits";
  testReversedLinkedList(b.data, "11001111000", b.len, 0);
  testReversedLinkedList(src.data, "702", src.len, 1);
}
TEST(ProjectTests, rightShift1_unsigned) {
  DataNode b0 = {'3', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = right_shift(src, 1);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of right_shift "
         "function should have the same number_bits";
  testReversedLinkedList(b.data, "1100101", b.len, 0);
  testReversedLinkedList(src.data, "302", src.len, 1);
}

char convertNToC(int n) {
  if (n >= 0 && n <= 9) {
    return n + '0';
  } else if (n >= 10 && n <= 15) {
    return n - 10 + 'A';
  } else {
    return 0;
  }
}
Data *convert_int_to_data(int number, int n) {
  Data *new_data = (Data *)malloc(sizeof(Data));
  int len = 0;
  if (number == 0) {
    new_data->data = (DataNode *)(malloc(sizeof(DataNode)));
    new_data->data->number = '0';
    new_data->data->next = NULL;
    len = 1;
  }
  while (number != 0) {
    DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
    newNode->number = convertNToC(number % n);
    newNode->next = new_data->data;
    new_data->data = newNode;
    number /= n;
    len++;
  }

  new_data->base = n;
  new_data->len = len;
  return new_data;
}

TEST(ProjectTests, convert_to_int_unsigned) {
  Data *data;
  int r;

  for (int i = 0; i < 65535; i++) {
    data = convert_int_to_data(i, 7);
    data->number_bits = 16;
    data->sign = 0;
    r = convert_to_int(*data);
    EXPECT_EQ(r, i) << "The return value of convert_to_int should be " << i
                    << " and your function returns " << r;
  }
}

TEST(ProjectTests, convert_to_int_signed) {
  Data *data;
  int r;
  int answer;

  for (int i = 0; i < 511; i++) {
    data = convert_int_to_data(i, 13);
    data->number_bits = 10;
    data->sign = 1;
    r = convert_to_int(*data);
    EXPECT_EQ(r, i) << "The return value of convert_to_int should be " << i
                    << " and your function returns " << r;
  }

  for (int i = 512; i <= 1023; i++) {
    answer = i - 1024;
    data = convert_int_to_data(i, 13);
    data->number_bits = 10;
    data->sign = 1;
    r = convert_to_int(*data);
    EXPECT_EQ(r, answer) << "The return value of convert_to_int should be "
                         << answer << " and your function returns " << r;
  }
}

#else
void testLinkedList(DataNode *node, const char *str, int l, int origin) {
  int i;
  const char *message = origin
                            ? "The original data should not be changed"
                            : "The return data has wrong linkedList of numbers";
  for (i = 0; str[i] != '\0' && node != NULL; i++, node = node->next) {
    EXPECT_EQ(node->number, str[i]) << message;
  }
  EXPECT_TRUE(node == NULL && str[i] == '\0') << str;
  if (!origin) {
    EXPECT_EQ(l, i)
        << "The returned data should have a linkedList with length " << i;
  }
}

TEST(ProjectTests, Convert_to_base_2) {
  DataNode b0 = {'5', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data d205;
  d205.base = 10;
  d205.sign = 0;
  d205.len = 3;
  d205.number_bits = 8;
  d205.data = &b2;

  Data b = convert_to_base_n(d205, 2);

  EXPECT_EQ(b.base, 2)
      << "The return data of convert_to_base_n function is not base 2";
  EXPECT_EQ(b.sign, 0) << "The return data of convert_to_base_n function "
                          "should have the same sign";
  EXPECT_EQ(b.number_bits, 8) << "The return data of convert_to_base_n "
                                 "function should have the same number_bits";
  EXPECT_EQ(b.len, 8) << "The return data of convert_to_base_n function should "
                         "have a linkedList with length 8";
  DataNode *node = b.data;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '0') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '0') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '0') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_EQ(node->number, '1') << "The return data of convert_to_base_n "
                                  "function has wrong linkedList of numbers";
  node = node->next;
  EXPECT_TRUE(node == NULL)
      << "The return data of convert_to_base_n function has "
         "wrong linkedList of numbers";
}

TEST(ProjectTests, Convert_to_base16) {
  DataNode b0 = {'5', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = convert_to_base_n(src, 16);
  EXPECT_EQ(b.base, 16)
      << "The return data of convert_to_base_n function is not base 16";
  EXPECT_EQ(b.sign, src.sign)
      << "The return data of convert_to_base_n function "
         "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of convert_to_base_n "
         "function should have the same number_bits";
  testLinkedList(b.data, "CD", b.len, 0);
  testLinkedList(src.data, "205", src.len, 1);
}

TEST(ProjectTests, Convert_to_base5) {
  DataNode b0 = {'8', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'1', &b1};

  Data src;
  src.base = 10;
  src.sign = 1;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = convert_to_base_n(src, 5);
  EXPECT_EQ(b.base, 5)
      << "The return data of convert_to_base_n function is not base 5";
  EXPECT_EQ(b.sign, src.sign)
      << "The return data of convert_to_base_n function "
         "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of convert_to_base_n "
         "function should have the same number_bits";
  testLinkedList(b.data, "413", b.len, 0);
  testLinkedList(src.data, "108", src.len, 1);
}

TEST(ProjectTests, Convert_to_base12) {
  DataNode b0 = {'7', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'1', &b1};

  Data src;
  src.base = 8;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = convert_to_base_n(src, 12);
  EXPECT_EQ(b.base, 12)
      << "The return data of convert_to_base_n function is not base 12";
  EXPECT_EQ(b.sign, src.sign)
      << "The return data of convert_to_base_n function "
         "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of convert_to_base_n "
         "function should have the same number_bits";
  testLinkedList(b.data, "5B", b.len, 0);
  testLinkedList(src.data, "107", src.len, 1);
}

TEST(ProjectTests, Convert_to_base9) {
  DataNode b0 = {'D', NULL};
  DataNode b1 = {'B', &b0};
  DataNode b2 = {'A', &b1};

  Data src;
  src.base = 14;
  src.sign = 1;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = convert_to_base_n(src, 9);
  EXPECT_EQ(b.base, 9)
      << "The return data of convert_to_base_n function is not base 9";
  EXPECT_EQ(b.sign, src.sign)
      << "The return data of convert_to_base_n function "
         "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of convert_to_base_n "
         "function should have the same number_bits";
  testLinkedList(b.data, "2823", b.len, 0);
  testLinkedList(src.data, "ABD", src.len, 1);
}

TEST(ProjectTests, Convert0) {
  DataNode b2 = {'0', NULL};

  Data src;
  src.base = 14;
  src.sign = 0;
  src.len = 1;
  src.number_bits = 4;
  src.data = &b2;

  Data b;
  for (int nb = 2; nb <= 16; nb++) {
    b = convert_to_base_n(src, nb);
    EXPECT_EQ(b.base, nb)
        << "The return data of convert_to_base_n function is not base " << nb;
    EXPECT_EQ(b.sign, src.sign)
        << "The return data of convert_to_base_n function "
           "should have the same sign";
    EXPECT_EQ(b.number_bits, src.number_bits)
        << "The return data of convert_to_base_n "
           "function should have the same number_bits";
    testLinkedList(b.data, "0", b.len, 0);
  }
  testLinkedList(src.data, "0", src.len, 1);
}

TEST(ProjectTests, Convert1) {
  DataNode b2 = {'1', NULL};

  Data src;
  src.base = 11;
  src.sign = 0;
  src.len = 1;
  src.number_bits = 4;
  src.data = &b2;

  Data b;
  for (int nb = 2; nb <= 16; nb++) {
    b = convert_to_base_n(src, nb);
    EXPECT_EQ(b.base, nb)
        << "The return data of convert_to_base_n function is not base " << nb;
    EXPECT_EQ(b.sign, src.sign)
        << "The return data of convert_to_base_n function "
           "should have the same sign";
    EXPECT_EQ(b.number_bits, src.number_bits)
        << "The return data of convert_to_base_n "
           "function should have the same number_bits";
    testLinkedList(b.data, "1", b.len, 0);
  }
  testLinkedList(src.data, "1", src.len, 1);
}

TEST(ProjectTests, ConvertSame) {
  DataNode b0 = {'1', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'1', &b1};

  Data src;
  src.sign = 1;
  src.len = 3;
  src.number_bits = 32;
  src.data = &b2;

  Data b;
  for (int nb = 2; nb <= 16; nb++) {
    src.base = nb;
    b = convert_to_base_n(src, nb);
    EXPECT_EQ(b.base, nb)
        << "The return data of convert_to_base_n function is not base " << nb;
    EXPECT_EQ(b.sign, src.sign)
        << "The return data of convert_to_base_n function "
           "should have the same sign";
    EXPECT_EQ(b.number_bits, src.number_bits)
        << "The return data of convert_to_base_n "
           "function should have the same number_bits";
    testLinkedList(b.data, "101", b.len, 0);
  }
  testLinkedList(src.data, "101", src.len, 1);
}

TEST(ProjectTests, LeftShift1) {
  DataNode b0 = {'5', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = left_shift(src, 1);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of left_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "110011010", b.len, 0);
  testLinkedList(src.data, "205", src.len, 1);
}

TEST(ProjectTests, LeftShift3) {
  DataNode b0 = {'7', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = left_shift(src, 3);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of left_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "11001111000", b.len, 0);
  testLinkedList(src.data, "207", src.len, 1);
}

TEST(ProjectTests, LeftShift1_overflow) {
  DataNode b0 = {'7', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = left_shift(src, 1);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of left_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "10011110", b.len, 0);
  testLinkedList(src.data, "207", src.len, 1);
}

TEST(ProjectTests, LeftShift3_overflow) {
  DataNode b0 = {'5', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = left_shift(src, 3);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of left_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "1101000", b.len, 0);
  testLinkedList(src.data, "205", src.len, 1);
}

TEST(ProjectTests, LeftShiftN_overflow) {
  DataNode b0 = {'4', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = left_shift(src, 7);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of left_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "0", b.len, 0);
  testLinkedList(src.data, "204", src.len, 1);
}

TEST(ProjectTests, rightShift1_unsigned) {
  DataNode b0 = {'3', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = right_shift(src, 1);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of right_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "1100101", b.len, 0);
  testLinkedList(src.data, "203", src.len, 1);
}

TEST(ProjectTests, rightShift5_unsigned) {
  DataNode b0 = {'3', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 0;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = right_shift(src, 5);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of right_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "110", b.len, 0);
  testLinkedList(src.data, "203", src.len, 1);
}

TEST(ProjectTests, rightShift1_signed) {
  DataNode b0 = {'3', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 1;
  src.len = 3;
  src.number_bits = 16;
  src.data = &b2;

  Data b = right_shift(src, 1);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of right_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "1100101", b.len, 0);
  testLinkedList(src.data, "203", src.len, 1);
}

TEST(ProjectTests, rightShift5_signed) {
  DataNode b0 = {'3', NULL};
  DataNode b1 = {'0', &b0};
  DataNode b2 = {'2', &b1};

  Data src;
  src.base = 10;
  src.sign = 1;
  src.len = 3;
  src.number_bits = 8;
  src.data = &b2;

  Data b = right_shift(src, 5);
  EXPECT_EQ(b.base, 2)
      << "The return data of left_shift function should always be base 2";
  EXPECT_EQ(b.sign, src.sign) << "The return data of the function "
                                 "should have the same sign";
  EXPECT_EQ(b.number_bits, src.number_bits)
      << "The return data of right_shift "
         "function should have the same number_bits";
  testLinkedList(b.data, "11111110", b.len, 0);
  testLinkedList(src.data, "203", src.len, 1);
}

char convertNToC(int n) {
  if (n >= 0 && n <= 9) {
    return n + '0';
  } else if (n >= 10 && n <= 15) {
    return n - 10 + 'A';
  } else {
    return 0;
  }
}

Data *convert_int_to_data(int number, int n) {
  Data *new_data = (Data *)malloc(sizeof(Data));
  int len = 0;
  if (number == 0) {
    new_data->data = (DataNode *)(malloc(sizeof(DataNode)));
    new_data->data->number = '0';
    new_data->data->next = NULL;
    len = 1;
  }
  while (number != 0) {
    DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
    newNode->number = convertNToC(number % n);
    newNode->next = new_data->data;
    new_data->data = newNode;
    number /= n;
    len++;
  }

  new_data->base = n;
  new_data->len = len;
  return new_data;
}

TEST(ProjectTests, convert_to_int_unsigned) {
  Data *data;
  int r;

  for (int i = 0; i < 65535; i++) {
    data = convert_int_to_data(i, 7);
    data->number_bits = 16;
    data->sign = 0;
    r = convert_to_int(*data);
    EXPECT_EQ(r, i) << "The return value of convert_to_int should be " << i
                    << " and your function returns " << r;
  }
}

TEST(ProjectTests, convert_to_int_signed) {
  Data *data;
  int r;
  int answer;

  for (int i = 0; i < 511; i++) {
    data = convert_int_to_data(i, 13);
    data->number_bits = 10;
    data->sign = 1;
    r = convert_to_int(*data);
    EXPECT_EQ(r, i) << "The return value of convert_to_int should be " << i
                    << " and your function returns " << r;
  }

  for (int i = 512; i <= 1023; i++) {
    answer = i - 1024;
    data = convert_int_to_data(i, 13);
    data->number_bits = 10;
    data->sign = 1;
    r = convert_to_int(*data);
    EXPECT_EQ(r, answer) << "The return value of convert_to_int should be "
                         << answer << " and your function returns " << r;
  }
}

TEST(ProjectTests, test_all) {
  Data *data;
  int r;
  int answer;

  for (int i = 0; i < 255; i++) {
    data = convert_int_to_data(i, 13);
    data->number_bits = 9;
    data->sign = 1;
    for (int base = 2; base <= 16; base++) {
      Data new_data = convert_to_base_n(*data, base);
      r = convert_to_int(new_data);
      EXPECT_EQ(r, i) << "The return value should be " << i
                      << " and your function returns " << r;
    }
  }

  for (int i = 256; i <= 511; i++) {
    answer = i - 512;
    data = convert_int_to_data(i, 3);
    data->number_bits = 9;
    data->sign = 1;
    for (int base = 2; base <= 16; base++) {
      Data new_data = convert_to_base_n(*data, base);
      r = convert_to_int(new_data);
      EXPECT_EQ(r, answer) << "The return value should be " << answer
                           << " and your function returns " << r;
      for (int shift = 1; shift <= 8; shift++) {
        int sr = answer >> shift;
        Data shift_data = right_shift(new_data, shift);
        r = convert_to_int(shift_data);
        EXPECT_EQ(r, sr) << "The return value should be " << sr
                         << " and your function returns " << r;
      }
      new_data.sign = 0;
      r = convert_to_int(new_data);
      EXPECT_EQ(r, i) << "The return value should be " << i
                      << " and your function returns " << r;
      for (int shift = 1; shift <= 8; shift++) {
        int sr = i >> shift;
        Data shift_data = right_shift(new_data, shift);
        r = convert_to_int(shift_data);
        EXPECT_EQ(r, sr) << "The return value should be " << sr
                         << " and your function returns " << r;
      }
    }
  }
}
#endif

// PRIVATE_END

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
