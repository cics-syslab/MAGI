// note that in these two lines, the "substitute" should be in all-caps
#ifndef __{_PROJECT_NAME_}
#define __{_PROJECT_NAME_}

typedef struct {_CONTAINER_} {_CONTAINER_};
typedef struct {_LINKED_LIST_} {_LINKED_LIST_};
typedef struct {_CONTAINER_TYPE_} {_CONTAINER_TYPE_};

// Represents a {_CONTAINER_}.
struct {_CONTAINER_} {
  char* name;
  {_LINKED_LIST_}* list;
};

// Represents a node in the linked list.
struct {_LINKED_LIST_} {
  {_CONTAINER_TYPE_}* {_ITEM_};
  {_LINKED_LIST_}* next;
};

// Represents a {_ITEM_} and its {_CONTAINER_}.
struct {_CONTAINER_TYPE_} {
  char* {_ITEM_}_name;
  char* {_CONTAINER_};
};

int {_CONTAINER_}_add({_CONTAINER_} {_PROJECT_NAME_}[], int number_of_{_CONTAINER_}, {_CONTAINER_TYPE_} {_ITEM_}[],
                 int number_of_{_ITEM_}, const char* {_ITEM_}_name);
{_CONTAINER_TYPE_}* {_CONTAINER_}_remove({_CONTAINER_} {_PROJECT_NAME_}[], int number_of_{_CONTAINER_},
                          const char* {_CONTAINER_}, const char* {_ITEM_}_name);
{_CONTAINER_TYPE_}* {_CONTAINER_}_change({_CONTAINER_} {_PROJECT_NAME_}[], int number_of_{_CONTAINER_},
                          {_CONTAINER_TYPE_} {_ITEM_}[], int number_of_{_ITEM_},
                          const char* {_ITEM_}_name, const char* old_{_CONTAINER_},
                          const char* new_{_CONTAINER_});

#endif