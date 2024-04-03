#ifndef __DATA
#define __DATA
// Define REVERSE_LINKED_LIST to enable reverse storage (uncomment to enable)
#define REVERSE_LINKED_LIST

typedef struct DataNode DataNode;
typedef struct Data Data;

// Represents a node in the linked list.
struct DataNode {
  unsigned char number;  // '0' ~ '9' or 'A' ~ 'F'
  DataNode *next;
};

// Represents data in base 2 - 16.
struct Data {
  unsigned char base;  // indicate what base this data is
  unsigned char sign;  // indicate whether this data is signed or unsigned
                       // number. 0 means unsigned and 1 means signed.
  unsigned char number_bits;  // the number of bits can be used to represent
                              // this number in binary.
                              // The maximal number of bits is 32.
  unsigned char len;          // length of linkedList
  DataNode *data;             // represent data in LinkedList
};

int convertCharToNumber(char ch);  // return decimal number of ch in base 2 ~ 16
                                   // return -1 if ch is not a valid number
char convertNumberToChar(
    int n);  // return char representation of n in base 2 ~ 16
             // return '\0' if n is not a number of 0 ~ 15
Data convert_to_base_n(
    Data src,
    unsigned char n);  // Return a new Data that represents src in base n
int convert_to_int(Data src);  // convert data to an int
Data left_shift(Data src,
                int shift);  // Return a new Data in base 2 that represents an
                             // application of binary operator left shift on src
                             // where shift is less than src.number_bits
Data right_shift(Data src,
                 int shift);  // Return a new Data in base 2 that represents an
                              // application of binary operator right shift on
                              // src where shift is less than src.number_bits

#endif
