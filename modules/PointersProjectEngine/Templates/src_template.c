#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <{_PROJECT_NAME_}.h>

// PRIVATE_BEGIN
#define MAX_LENGTH 1024
// PRIVATE_END

int {_CONTAINER_}_add({_CONTAINER_TYPE_} {_PROJECT_NAME_}[], int number_of_{_CONTAINER_}, {_ITEM_TYPE_} {_ITEM_}[],
                 int number_of_{_ITEM_}, const char* {_ITEM_}_name) {
  // PRIVATE_BEGIN
  int modified = 0;
  for (int i = 0; i < number_of_{_ITEM_}; i++) {
    if (strncmp({_ITEM_}[i].{_ITEM_}_name, {_ITEM_}_name, MAX_LENGTH) == 0) {
      {_LINKED_LIST_}* newNode = ({_LINKED_LIST_}*)(malloc(sizeof({_LINKED_LIST_})));
      newNode->{_ITEM_} = &{_ITEM_}[i];
      for (int j = 0; j < number_of_{_CONTAINER_}; j++) {
        if (strncmp({_PROJECT_NAME_}[j].name, newNode->{_ITEM_}->{_CONTAINER_}, MAX_LENGTH) ==
            0) {
          // add node into this {_CONTAINER_}
          {_LINKED_LIST_}* preNode = NULL;
          {_LINKED_LIST_}* curNode = {_PROJECT_NAME_}[j].list;
          while (curNode && strncmp(newNode->{_ITEM_}->{_ITEM_}_name,
                                    curNode->{_ITEM_}->{_ITEM_}_name, MAX_LENGTH) > 0) {
            preNode = curNode;
            curNode = curNode->next;
          }

          if (curNode && strncmp(newNode->{_ITEM_}->{_ITEM_}_name,
                                 curNode->{_ITEM_}->{_ITEM_}_name, MAX_LENGTH) == 0) {
            break;
          }

          newNode->next = curNode;
          if (preNode != NULL) {
            preNode->next = newNode;
          } else {
            _PROJECT_NAME_[j].list = newNode;
          }
          modified = 1;
        }
      }
    }
  }
  return modified;

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
return 0;
  // PUBLIC_END */
}

{_ITEM_TYPE_}* {_CONTAINER_}_remove({_CONTAINER_TYPE_} {_PROJECT_NAME_}[], int number_of_{_CONTAINER_},
                          const char* {_CONTAINER_}, const char* {_ITEM_}_name) {
  // PRIVATE_BEGIN
  for (int j = 0; j < number_of_{_CONTAINER_}; j++) {
    if (strncmp({_PROJECT_NAME_}[j].name, {_CONTAINER_}, MAX_LENGTH) == 0) {
      {_LINKED_LIST_}* preNode = NULL;
      {_LINKED_LIST_}* curNode = {_PROJECT_NAME_}[j].list;
      while (curNode &&
             strncmp({_ITEM_}_name, curNode->{_ITEM_}->{_ITEM_}_name, MAX_LENGTH) != 0) {
        preNode = curNode;
        curNode = curNode->next;
      }

      if (curNode) {
        if (preNode) {
          preNode->next = curNode->next;
        } else {
          {_PROJECT_NAME_}[j].list = curNode->next;
        }
        {_ITEM_TYPE_}* result = curNode->{_ITEM_};
        free(curNode);
        return result;
      }
    }
  }
  // Cannot find the {_CONTAINER_} or the {_ITEM_} in the {_CONTAINER_}
  return NULL;

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
return NULL;
  // PUBLIC_END */
}

{_ITEM_TYPE_}* {_CONTAINER_}_change({_CONTAINER_} {_PROJECT_NAME_}[], int number_of_{_CONTAINER_},
                          {_ITEM_TYPE_} {_ITEM_}s[], int number_of_{_ITEM_}s, // translates to: FileData files[], int number_of_files,
                          const char* {_ITEM_}_name, const char* old_{_CONTAINER_}, // const char* file_name, const char* old_category,
                          // categories vs category
                          //use gives _ITEM_
                          //your program should automatically {_ITEM_name_}
                          const char* new_{_CONTAINER_}) {
  // PRIVATE_BEGIN
  char exist = 0;
  {_ITEM_TYPE_}* target_{_ITEM_} = NULL;

  for (int j = 0; j < number_of_{_CONTAINER_}; j++) {
    if (strncmp({_PROJECT_NAME_}[j].name, new_{_CONTAINER_}, MAX_LENGTH) == 0) {
      exist = 1;
      break;
    }
  }
  if (!exist) {
    return NULL;
  }

  exist = 0;
  for (int i = 0; i < number_of_{_ITEM_}s; i++) {
    if (strncmp({_ITEM_}s[i].{_ITEM_}_name, {_ITEM_}_name, MAX_LENGTH) == 0 &&
        strncmp({_ITEM_}s[i].{_CONTAINER_}, old_{_CONTAINER_}, MAX_LENGTH) == 0) {
      target_{_ITEM_} = &{_ITEM_}s[i];
    }
    if (strncmp({_ITEM_}s[i].{_ITEM_}_name, {_ITEM_}_name, MAX_LENGTH) == 0 &&
        strncmp({_ITEM_}s[i].{_CONTAINER_}, new_{_CONTAINER_}, MAX_LENGTH) == 0) {
      exist = 1;
    }
  }

  if (!exist && target_{_ITEM_}) {
    for (int j = 0; j < number_of_{_CONTAINER_}; j++) {
      if (strncmp({_PROJECT_NAME_}[j].name, old_{_CONTAINER_}, MAX_LENGTH) == 0) {
        exist = 0;
        {_LINKED_LIST_}* curNode = {_PROJECT_NAME_}[j].list;
        while (curNode) {
          if (strncmp({_ITEM_}_name, curNode->{_ITEM_}->{_ITEM_}_name, MAX_LENGTH) == 0) {
            exist = 1;
            break;
          }
          curNode = curNode->next;
        }
        break;
      }
    }

    if (exist) {
      {_CONTAINER_}_remove({_PROJECT_NAME_}, number_of_{_CONTAINER_}, old_{_CONTAINER_}, {_ITEM_}_name);
    }

    strcpy(target_{_ITEM_}->{_CONTAINER_}, new_{_CONTAINER_});

    if (exist) {
      {_LINKED_LIST_}* newNode = ({_LINKED_LIST_}*)(malloc(sizeof({_LINKED_LIST_})));
      newNode->{_ITEM_} = target_{_ITEM_};
      for (int j = 0; j < number_of_{_CONTAINER_}; j++) {
        if (strncmp({_PROJECT_NAME_}[j].name, new_{_CONTAINER_}, MAX_LENGTH) == 0) {
          // add node into this {_CONTAINER_}
          {_LINKED_LIST_}* preNode = NULL;
          {_LINKED_LIST_}* curNode = {_PROJECT_NAME_}[j].list;
          while (curNode && strncmp(newNode->{_ITEM_}->{_ITEM_}_name,
                                    curNode->{_ITEM_}->{_ITEM_}_name, MAX_LENGTH) > 0) {
            preNode = curNode;
            curNode = curNode->next;
          }

          newNode->next = curNode;
          if (preNode != NULL) {
            preNode->next = newNode;
          } else {
            {_PROJECT_NAME_}[j].list = newNode;
          }
          break;
        }
      }
    }

    return target_{_ITEM_};
  }

  return NULL;

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
return NULL;
  // PUBLIC_END */
}
