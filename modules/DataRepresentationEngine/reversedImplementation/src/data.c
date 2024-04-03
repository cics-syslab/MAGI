#include <data.h>
#include <stdio.h>
#include <stdlib.h>

int convertCharToNumber(char ch) {
  if (ch >= '0' && ch <= '9') {
    return ch - '0';
  } else if (ch >= 'A' && ch <= 'F') {
    return ch - 'A' + 10;
  } else {
    return -1;
  }
}

char convertNumberToChar(int n) {
  if (n >= 0 && n <= 9) {
    return n + '0';
  } else if (n >= 10 && n <= 15) {
    return n - 10 + 'A';
  } else {
    return 0;
  }
}

#ifdef REVERSE_LINKED_LIST
// Private helper function to reverse a linked list
void reverseLinkedList(DataNode **head) {
    DataNode *prev = NULL;
    DataNode *current = *head;
    DataNode *next = NULL;
    while (current != NULL) {
        next = current->next;  // Store next node
        current->next = prev;  // Reverse current node's pointer
        prev = current;        // Move pointers one position ahead
        current = next;
    }
    *head = prev; // Reset head to new front of the list
}
#endif

Data convert_to_base_n(Data src, unsigned char n) {
  Data new_data;
  new_data.data = NULL;
  // PRIVATE_BEGIN
  int number = 0;
  for (DataNode *node = src.data; node; node = node->next) {
    number = number * src.base + convertCharToNumber(node->number);
  }
  int len = 0;
  if (number == 0) {
    new_data.data = (DataNode *)(malloc(sizeof(DataNode)));
    new_data.data->number = '0';
    new_data.data->next = NULL;
    len = 1;
  }

  while (number != 0) {
    DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
    newNode->number = convertNumberToChar(number % n);
    number /= n;
    newNode->next = new_data.data; // Insert new node at the beginning
    new_data.data = newNode;

    len++;
  }
  new_data.base = n;
  new_data.sign = src.sign;
  new_data.number_bits = src.number_bits;
  new_data.len = len;
  #ifdef REVERSE_LINKED_LIST
  reverseLinkedList(&new_data.data);
  #endif

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
  PUBLIC_END */
  return new_data;
}

int convert_to_int(Data src) {
  // PRIVATE_BEGIN
  int result = 0;
  Data data_base2 = convert_to_base_n(src, 2);
  #ifdef REVERSE_LINKED_LIST
  reverseLinkedList(&data_base2.data);
  #endif
  if (data_base2.sign && data_base2.len == data_base2.number_bits &&
      data_base2.data->number == '1') {
    for (DataNode *node = data_base2.data; node; node = node->next) {
      int digit = (node->number == '0') ? 1 : 0;
      result = result * 2 + digit;
    }
    return -(result + 1);
  } else {
    for (DataNode *node = data_base2.data; node; node = node->next) {
      result = result * 2 + convertCharToNumber(node->number);
    }
  }
  return result;

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
  return 0;
  PUBLIC_END */
}

Data left_shift(Data src, int n) {
  Data new_data;
  // PRIVATE_BEGIN
  new_data = convert_to_base_n(src, 2);
  #ifdef REVERSE_LINKED_LIST
  reverseLinkedList(&new_data.data);
  #endif
  int total = new_data.len + n;
  int num_remove_bits = total - new_data.number_bits;
  // find the tail
  DataNode *node;
  for (node = new_data.data; node->next; node = node->next) {
  }
  // add 0s into the tail of linkedList
  DataNode *append = NULL;
  for (int i = 0; i < n; i++) {
    DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
    newNode->number = '0';
    newNode->next = append;
    append = newNode;
  }
  node->next = append;
  int len = total;
  // remove overflow bits
  for (int i = 0; i < num_remove_bits; i++) {
    new_data.data = new_data.data->next;
    len--;
  }
  // remove head 0s
  while (new_data.data->next && new_data.data->number == '0') {
    new_data.data = new_data.data->next;
    len--;
  }
  new_data.len = len;

  #ifdef REVERSE_LINKED_LIST
  reverseLinkedList(&new_data.data);
  #endif

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
  PUBLIC_END */
  return new_data;
}

Data right_shift(Data src, int n) {
  Data new_data;
  // PRIVATE_BEGIN
  new_data = convert_to_base_n(src, 2);
  #ifdef REVERSE_LINKED_LIST
  reverseLinkedList(&new_data.data);
  #endif
  int len = new_data.len;
  if (new_data.sign && new_data.len == new_data.number_bits) {
    for (int i = 0; i < n; i++) {
      DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
      newNode->number = '1';
      newNode->next = new_data.data;
      new_data.data = newNode;
      len++;
    }
  }

  if (len <= n) {
    DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
    newNode->number = '0';
    newNode->next = NULL;
    new_data.len = 1;
    new_data.data = newNode;
    return new_data;
  }

  DataNode *node = new_data.data;
  for (int i = 0; i < len - n - 1; i++) {
    node = node->next;
  }
  node->next = NULL;
  new_data.len = len - n;
  #ifdef REVERSE_LINKED_LIST
  reverseLinkedList(&new_data.data);
  #endif

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
  PUBLIC_END */
  return new_data;
}











// #include <data.h>
// #include <stdio.h>
// #include <stdlib.h>

// int convertCharToNumber(char ch) {
//   if (ch >= '0' && ch <= '9') {
//     return ch - '0';
//   } else if (ch >= 'A' && ch <= 'F') {
//     return ch - 'A' + 10;
//   } else {
//     return -1;
//   }
// }

// char convertNumberToChar(int n) {
//   if (n >= 0 && n <= 9) {
//     return n + '0';
//   } else if (n >= 10 && n <= 15) {
//     return n - 10 + 'A';
//   } else {
//     return 0;
//   }
// }

// Data convert_to_base_n(Data src, unsigned char n) {
//   Data new_data;
//   new_data.data = NULL;
//   // PRIVATE_BEGIN
//   int number = 0;
//   for (DataNode *node = src.data; node; node = node->next) {
//     number = number * src.base + convertCharToNumber(node->number);
//   }
//   int len = 0;
//   if (number == 0) {
//     new_data.data = (DataNode *)(malloc(sizeof(DataNode)));
//     new_data.data->number = '0';
//     new_data.data->next = NULL;
//     len = 1;
//   }
//   DataNode *lastNode = NULL; // to keep track of the last node for reverse insertion
//   while (number != 0) {
//     DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
//     newNode->number = convertNumberToChar(number % n);
//     number /= n;
//     #ifdef REVERSE_LINKED_LIST // implementation if testing reverse linked list
//     if (new_data.data == NULL) {
//       newNode->next = NULL;
//       new_data.data = newNode;
//       lastNode = newNode;
//     } 
//     else {
//       lastNode->next = newNode; // append new node at the end
//       newNode->next = NULL;
//       lastNode = newNode;
//     }
//     #else
//       newNode->next = new_data.data; // Insert new node at the beginning
//       new_data.data = newNode;
//     #endif
//     len++;
//   }
//   new_data.base = n;
//   new_data.sign = src.sign;
//   new_data.number_bits = src.number_bits;
//   new_data.len = len;

//   // PRIVATE_END
//   /* PUBLIC_BEGIN
//   // TODO
//   PUBLIC_END */
//   return new_data;
// }

// int convert_to_int(Data src) {
//   // PRIVATE_BEGIN
//   int result = 0;
//   Data data_base2 = convert_to_base_n(src, 2);
//   if (data_base2.sign && data_base2.len == data_base2.number_bits &&
//       data_base2.data->number == '1') {
//     for (DataNode *node = data_base2.data; node; node = node->next) {
//       int digit = (node->number == '0') ? 1 : 0;
//       result = result * 2 + digit;
//     }
//     return -(result + 1);
//   } else {
//     for (DataNode *node = data_base2.data; node; node = node->next) {
//       result = result * 2 + convertCharToNumber(node->number);
//     }
//   }

//   return result;

//   // PRIVATE_END
//   /* PUBLIC_BEGIN
//   // TODO
//   return 0;
//   PUBLIC_END */
// }

// #ifdef REVERSE_LINKED_LIST
// Data left_shift(Data src, int n) {
//   Data new_data = convert_to_base_n(src, 2);
//   int total = new_data.len + n;
//   int num_remove_bits = total - new_data.number_bits;

//   // Add 0s to the head of the linkedList for reverse
//   for (int i = 0; i < n; i++) {
//     DataNode *newNode = (DataNode *)malloc(sizeof(DataNode));
//     newNode->number = '0';
//     // For reverse linked list, prepend zeros
//     newNode->next = new_data.data;
//     new_data.data = newNode;
//   }
//   new_data.len += n;
//   // Remove overflow bits from the end
//   DataNode **node = &new_data.data;
//   while (*node && total > new_data.number_bits) {
//     node = &(*node)->next;
//     total--;
//   }
//   if (*node) {
//     *node = NULL;
//   }
//   new_data.len = total;

//   return new_data;
// }

// Data right_shift(Data src, int n) {
//   Data new_data = convert_to_base_n(src, 2);

//   // truncate bits from the head for reverse
//   while (n > 0 && new_data.data) {
//     DataNode *temp = new_data.data;
//     new_data.data = new_data.data->next;
//     free(temp);
//     n--;
//     new_data.len--;
//   }

//   // sign extension for signed data
//   if (new_data.sign) {
//     DataNode **node = &new_data.data;
//     while (*node) {
//       node = &(*node)->next;
//     }
//     for (int i = 0; i < n; i++) {
//       *node = (DataNode *)malloc(sizeof(DataNode));
//       (*node)->number = '1';
//       (*node)->next = NULL;
//       node = &(*node)->next;
//     }
//     new_data.len += n;
//   }
//   return new_data;
// }

// #else
// Data left_shift(Data src, int n) {
//   Data new_data;
//   // PRIVATE_BEGIN
//   new_data = convert_to_base_n(src, 2);
//   int total = new_data.len + n;
//   int num_remove_bits = total - new_data.number_bits;

//   // find the tail
//   DataNode *node;
//   for (node = new_data.data; node->next; node = node->next) {
//   }

//   // add 0s into the tail of linkedList
//   DataNode *append = NULL;
//   for (int i = 0; i < n; i++) {
//     DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
//     newNode->number = '0';
//     newNode->next = append;
//     append = newNode;
//   }
//   node->next = append;
//   int len = total;

//   // remove overflow bits
//   for (int i = 0; i < num_remove_bits; i++) {
//     new_data.data = new_data.data->next;
//     len--;
//   }

//   // remove head 0s
//   while (new_data.data->next && new_data.data->number == '0') {
//     new_data.data = new_data.data->next;
//     len--;
//   }

//   new_data.len = len;

//   // PRIVATE_END
//   /* PUBLIC_BEGIN
//   // TODO
//   PUBLIC_END */
//   return new_data;
// }

// Data right_shift(Data src, int n) {
//   Data new_data;
//   // PRIVATE_BEGIN
//   new_data = convert_to_base_n(src, 2);

//   int len = new_data.len;
//   if (new_data.sign && new_data.len == new_data.number_bits) {
//     for (int i = 0; i < n; i++) {
//       DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
//       newNode->number = '1';
//       newNode->next = new_data.data;
//       new_data.data = newNode;
//       len++;
//     }
//   }

//   if (len <= n) {
//     DataNode *newNode = (DataNode *)(malloc(sizeof(DataNode)));
//     newNode->number = '0';
//     newNode->next = NULL;
//     new_data.len = 1;
//     new_data.data = newNode;
//     return new_data;
//   }

//   DataNode *node = new_data.data;
//   for (int i = 0; i < len - n - 1; i++) {
//     node = node->next;
//   }
//   node->next = NULL;
//   new_data.len = len - n;

//   // PRIVATE_END
//   /* PUBLIC_BEGIN
//   // TODO
//   PUBLIC_END */
//   return new_data;
// }
// #endif
