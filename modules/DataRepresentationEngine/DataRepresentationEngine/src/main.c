#include <data.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
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
  printf("The data should be 010110011, and your data is ");
  for (DataNode *node = b.data; node; node = node->next) {
    printf("%c", node->number);
  }
  printf("\n\n");

  // DataNode b0 = {'5', NULL};
  // DataNode b1 = {'0', &b0};
  // DataNode b2 = {'2', &b1};

  // Data d205;
  // d205.base = 10;
  // d205.sign = 0;
  // d205.len = 3;
  // d205.number_bits = 8;
  // d205.data = &b2;

  // Data b11001101 = convert_to_base_n(d205, 2);
  // printf("The base should be 2, and your base is %d\n", b11001101.base);
  // printf("The sign should not be changed, and your sign is %d\n", b11001101.sign);
  // printf("The number_bits should not be changed, and your number_bits is %d\n", b11001101.number_bits);
  // printf("The length should be 8, and your len is %d\n", b11001101.len);
  // // printf("The data should be 11001101, and your data is "); // regular order
  // printf("The data should be 10110011, and your data is "); // reversed!
  // for (DataNode *node = b11001101.data; node; node = node->next) {
  //   printf("%c", node->number);
  // }
  // printf("\n\n");

//   Data hCD = convert_to_base_n(d205, 16);
//   printf("The base should be 16, and your base is %d\n", hCD.base);
//   printf("The sign should not be changed, and your sign is %d\n", hCD.sign);
//   printf("The number_bits should not be changed, and your number_bits is %d\n",
//          hCD.number_bits);
//   printf("The length should be 2, and your len is %d\n", hCD.len);
//   printf("The data should be CD, and your data is ");
//   for (DataNode *node = hCD.data; node; node = node->next) {
//     printf("%c", node->number);
//   }
//   printf("\n\n");

//   Data b00110100 = left_shift(d205, 2);
//   printf("The base should be 2, and your base is %d\n", b00110100.base);
//   printf("The sign should not be changed, and your sign is %d\n",
//          b00110100.sign);
//   printf("The number_bits should not be changed, and your number_bits is %d\n",
//          b00110100.number_bits);
//   printf(
//       "The length should be 6 since it cannot exceed the number_bit and"
//       " the first two 0 should not be included in the list.Your len is %d\n",
//       b00110100.len);
//   printf("The data should be 110100, and your data is ");
//   for (DataNode *node = b00110100.data; node; node = node->next) {
//     printf("%c", node->number);
//   }
//   printf("\n");

//   printf("We expect 205, and your function returns %d\n",
//          convert_to_int(b11001101));
//   b11001101.sign = 1;
//   printf("We expect -51, and your function returns %d\n",
//          convert_to_int(b11001101));
//   b11001101.number_bits = 16;
//   printf("We expect 205, and your function returns %d\n",
//          convert_to_int(b11001101));

  return 0;
}
