#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Project Name.h>

// PRIVATE_BEGIN
#define MAX_LENGTH 1024
// PRIVATE_END

int Container_add(Container Type Project Name[], int number_of_Container,  Item Type[],
                 int number_of_Item Type, const char* Item Type_name) {
  // PRIVATE_BEGIN
  int modified = 0;
  for (int i = 0; i < number_of_Item Type; i++) {
    if (strncmp(Item Type[i].Item Type_name, Item Type_name, MAX_LENGTH) == 0) {
      * newNode = (*)(malloc(sizeof()));
      newNode->Item Type = &Item Type[i];
      for (int j = 0; j < number_of_Container; j++) {
        if (strncmp(Project Name[j].name, newNode->Item Type->Container, MAX_LENGTH) ==
            0) {
          // add node into this Container
          * preNode = NULL;
          * curNode = Project Name[j].list;
          while (curNode && strncmp(newNode->Item Type->Item Type_name,
                                    curNode->Item Type->Item Type_name, MAX_LENGTH) > 0) {
            preNode = curNode;
            curNode = curNode->next;
          }

          if (curNode && strncmp(newNode->Item Type->Item Type_name,
                                 curNode->Item Type->Item Type_name, MAX_LENGTH) == 0) {
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

* Container_remove(Container Type Project Name[], int number_of_Container,
                          const char* Container, const char* Item Type_name) {
  // PRIVATE_BEGIN
  for (int j = 0; j < number_of_Container; j++) {
    if (strncmp(Project Name[j].name, Container, MAX_LENGTH) == 0) {
      * preNode = NULL;
      * curNode = Project Name[j].list;
      while (curNode &&
             strncmp(Item Type_name, curNode->Item Type->Item Type_name, MAX_LENGTH) != 0) {
        preNode = curNode;
        curNode = curNode->next;
      }

      if (curNode) {
        if (preNode) {
          preNode->next = curNode->next;
        } else {
          Project Name[j].list = curNode->next;
        }
        * result = curNode->Item Type;
        free(curNode);
        return result;
      }
    }
  }
  // Cannot find the Container or the Item Type in the Container
  return NULL;

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
return NULL;
  // PUBLIC_END */
}

* Container_change(Container Project Name[], int number_of_Container,
                           Item Types[], int number_of_Item Types, // translates to: FileData files[], int number_of_files,
                          const char* Item Type_name, const char* old_Container, // const char* file_name, const char* old_category,
                          // categories vs category
                          //use gives _ITEM_
                          //your program should automatically 
                          const char* new_Container) {
  // PRIVATE_BEGIN
  char exist = 0;
  * target_Item Type = NULL;

  for (int j = 0; j < number_of_Container; j++) {
    if (strncmp(Project Name[j].name, new_Container, MAX_LENGTH) == 0) {
      exist = 1;
      break;
    }
  }
  if (!exist) {
    return NULL;
  }

  exist = 0;
  for (int i = 0; i < number_of_Item Types; i++) {
    if (strncmp(Item Types[i].Item Type_name, Item Type_name, MAX_LENGTH) == 0 &&
        strncmp(Item Types[i].Container, old_Container, MAX_LENGTH) == 0) {
      target_Item Type = &Item Types[i];
    }
    if (strncmp(Item Types[i].Item Type_name, Item Type_name, MAX_LENGTH) == 0 &&
        strncmp(Item Types[i].Container, new_Container, MAX_LENGTH) == 0) {
      exist = 1;
    }
  }

  if (!exist && target_Item Type) {
    for (int j = 0; j < number_of_Container; j++) {
      if (strncmp(Project Name[j].name, old_Container, MAX_LENGTH) == 0) {
        exist = 0;
        * curNode = Project Name[j].list;
        while (curNode) {
          if (strncmp(Item Type_name, curNode->Item Type->Item Type_name, MAX_LENGTH) == 0) {
            exist = 1;
            break;
          }
          curNode = curNode->next;
        }
        break;
      }
    }

    if (exist) {
      Container_remove(Project Name, number_of_Container, old_Container, Item Type_name);
    }

    strcpy(target_Item Type->Container, new_Container);

    if (exist) {
      * newNode = (*)(malloc(sizeof()));
      newNode->Item Type = target_Item Type;
      for (int j = 0; j < number_of_Container; j++) {
        if (strncmp(Project Name[j].name, new_Container, MAX_LENGTH) == 0) {
          // add node into this Container
          * preNode = NULL;
          * curNode = Project Name[j].list;
          while (curNode && strncmp(newNode->Item Type->Item Type_name,
                                    curNode->Item Type->Item Type_name, MAX_LENGTH) > 0) {
            preNode = curNode;
            curNode = curNode->next;
          }

          newNode->next = curNode;
          if (preNode != NULL) {
            preNode->next = newNode;
          } else {
            Project Name[j].list = newNode;
          }
          break;
        }
      }
    }

    return target_Item Type;
  }

  return NULL;

  // PRIVATE_END
  /* PUBLIC_BEGIN
  // TODO
return NULL;
  // PUBLIC_END */
}