#include <gtest/gtest.h>

extern "C" {
#include <{_PROJECT_NAME_}.h>
}

#define MAX_LEN 1024

const char* names[5] = {"{_DESCRIPTOR1_}", "{_DESCRIPTOR2_}", "{_ITEM1_}", "{_ITEM2_}", "{_ITEM3_}"};
{_CONTAINER_} {_PROJECT_NAME_}[2];
{_ITEM_}Data {_ITEM_}[4];

// PRIVATE_BEGIN
const char* private_{_{_CONTAINER_}_NAMES_}[4] = {"Excellent", "Great", "Fair", "Poor"};
const char* private_{_ITEM_NAMES_}[10] = {"X", "Y", "Z",  "A",  "B",
                                  "C", "D", "AB", "AX", "DC"};
{_CONTAINER_} private_dataset[4];
{_ITEM_}Data private_{_ITEM_}[20];
{_ITEM_}Data private_{_ITEM_}_backup[20];
// PRIVATE_END

class basicDatabaseEnvironment : public testing::Environment {
 public:
  virtual void SetUp() {
    {_PROJECT_NAME_}[0].name = (char*)malloc(4);
    strcpy({_PROJECT_NAME_}[0].name, names[0]);
    {_PROJECT_NAME_}[0].list = NULL;
    {_PROJECT_NAME_}[1].name = (char*)malloc(5);
    strcpy({_PROJECT_NAME_}[1].name, names[1]);
    {_PROJECT_NAME_}[1].list = NULL;

    {_ITEM_}[0].{_CONTAINER_} = (char*)malloc(4);
    {_ITEM_}[0].{_ITEM_}_name = (char*)malloc(5);
    strcpy({_ITEM_}[0].{_CONTAINER_}, names[0]);
    strcpy({_ITEM_}[0].{_ITEM_}_name, names[2]);
        {_ITEM_}[1].{_CONTAINER_} = (char*)malloc(4);
    {_ITEM_}[1].{_ITEM_}_name = (char*)malloc(4);
    strcpy({_ITEM_}[1].{_CONTAINER_}, names[0]);
    strcpy({_ITEM_}[1].{_ITEM_}_name, names[3]);
    {_ITEM_}[2].{_CONTAINER_} = (char*)malloc(5);
    {_ITEM_}[2].{_ITEM_}_name = (char*)malloc(4);
    strcpy({_ITEM_}[2].{_CONTAINER_}, names[1]);
    strcpy({_ITEM_}[2].{_ITEM_}_name, names[3]);
    {_ITEM_}[3].{_CONTAINER_} = (char*)malloc(5);
    {_ITEM_}[3].{_ITEM_}_name = (char*)malloc(7);
    strcpy({_ITEM_}[3].{_CONTAINER_}, names[1]);
    strcpy({_ITEM_}[3].{_ITEM_}_name, names[4]);

    // PRIVATE_BEGIN
    for (int i = 0; i < 4; i++) {
      private_dataset[i].name = (char*)malloc(strlen(private_cnames[i]));
      strcpy(private_dataset[i].name, private_cnames[i]);
      private_dataset[i].list = NULL;
    }

    for (int i = 0; i < 10; i++) {
      private_{_ITEM_}[i].{_ITEM_}_name = (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}[i].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}[i].{_CONTAINER_} = (char*)malloc(strlen(private_cnames[i % 4]));
      strcpy(private_{_ITEM_}[i].{_CONTAINER_}, private_cnames[i % 4]);

      private_{_ITEM_}_backup[i].{_ITEM_}_name =
          (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}_backup[i].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}_backup[i].{_CONTAINER_} =
          (char*)malloc(strlen(private_cnames[i % 4]));
      strcpy(private_{_ITEM_}_backup[i].{_CONTAINER_}, private_cnames[i % 4]);
    }
    for (int i = 0; i < 5; i++) {
      private_{_ITEM_}[i + 10].{_ITEM_}_name =
          (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}[i + 10].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}[i + 10].{_CONTAINER_} =
          (char*)malloc(strlen(private_cnames[(i + 2) % 4]));
      strcpy(private_{_ITEM_}[i + 10].{_CONTAINER_}, private_cnames[(i + 2) % 4]);

      private_{_ITEM_}_backup[i + 10].{_ITEM_}_name =
          (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}_backup[i + 10].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}_backup[i + 10].{_CONTAINER_} =
          (char*)malloc(strlen(private_cnames[(i + 2) % 4]));
      strcpy(private_{_ITEM_}_backup[i + 10].{_CONTAINER_},
             private_cnames[(i + 2) % 4]);
    }
    for (int i = 0; i < 3; i++) {
      private_{_ITEM_}[i + 15].{_ITEM_}_name =
          (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}[i + 15].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}[i + 15].{_CONTAINER_} =
          (char*)malloc(strlen(private_cnames[(i + 1) % 4]));
      strcpy(private_{_ITEM_}[i + 15].{_CONTAINER_}, private_cnames[(i + 1) % 4]);

      private_{_ITEM_}_backup[i + 15].{_ITEM_}_name =
          (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}_backup[i + 15].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}_backup[i + 15].{_CONTAINER_} =
          (char*)malloc(strlen(private_cnames[(i + 1) % 4]));
      strcpy(private_{_ITEM_}_backup[i + 15].{_CONTAINER_},
             private_cnames[(i + 1) % 4]);
    }
    for (int i = 0; i < 2; i++) {
      private_{_ITEM_}[i + 18].{_ITEM_}_name =
          (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}[i + 18].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}[i + 18].{_CONTAINER_} =
          (char*)malloc(strlen(private_cnames[(i + 3) % 4]));
      strcpy(private_{_ITEM_}[i + 18].{_CONTAINER_}, private_cnames[(i + 3) % 4]);

      private_{_ITEM_}_backup[i + 18].{_ITEM_}_name =
          (char*)malloc(strlen(private_fnames[i]));
      strcpy(private_{_ITEM_}_backup[i + 18].{_ITEM_}_name, private_fnames[i]);
      private_{_ITEM_}_backup[i + 18].{_CONTAINER_} =
          (char*)malloc(strlen(private_cnames[(i + 3) % 4]));
      strcpy(private_{_ITEM_}_backup[i + 18].{_CONTAINER_},
             private_cnames[(i + 3) % 4]);
    }
    // PRIVATE_END
  }
};

void reset_dataset() {
  dataset[0].list = NULL;
  dataset[1].list = NULL;
}

TEST(ProjectTests, {_CONTAINER_}_add_first) {
  reset_dataset();
  int result;
  result = {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  ASSERT_STREQ((dataset[0].list)->{_ITEM_}->{_ITEM_}_name, "{_ITEM1_}")
      << "The first item in {_CONTAINER_} 'New' should be {_ITEM1_}.";
}

TEST(ProjectTests, {_CONTAINER_}_add_none) {
  reset_dataset();
  int result;
  result = {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "Apple");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";
}

TEST(ProjectTests, {_CONTAINER_}_add_multiple) {
  reset_dataset();
  int result;
  result = {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}");
  result = {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "Pen");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  ASSERT_STREQ((dataset[0].list)->next->{_ITEM_}->{_ITEM_}_name, "Pen")
      << "The second item in {_CONTAINER_} 'New' should be Pen.";
  ASSERT_STREQ((dataset[1].list)->{_ITEM_}->{_ITEM_}_name, "Pen")
      << "The first item in {_CONTAINER_} 'Used' should be Pen.";
}

TEST(ProjectTests, {_CONTAINER_}_remove_second_item) {
  reset_dataset();
  {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}");
  {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "Pen");
  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(dataset, 2, "New", "Pen");
  EXPECT_TRUE(result_{_ITEM_} == &{_ITEM_}[1])
      << "The returned {_ITEM_} should be the second {_ITEM_} in the {_ITEM_} list.";
  ASSERT_STREQ((dataset[0].list)->{_ITEM_}->{_ITEM_}_name, "{_ITEM1_}")
      << "The first item in {_CONTAINER_} 'New' should be {_ITEM1_}.";
  ASSERT_STREQ((dataset[1].list)->{_ITEM_}->{_ITEM_}_name, "Pen")
      << "The first item in {_CONTAINER_} 'Used' should be Pen.";
  EXPECT_TRUE((dataset[0].list)->next == NULL)
      << "The {_CONTAINER_} 'New' should have only one item";
}

TEST(ProjectTests, {_CONTAINER_}_remove_none) {
  reset_dataset();
  {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}");
  {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "Pen");
  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(dataset, 2, "New", "Pen");
  result_{_ITEM_} = {_CONTAINER_}_remove(dataset, 2, "New", "Pen");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned result should be NULL";
}

TEST(ProjectTests, {_CONTAINER_}_remove_first_item) {
  reset_dataset();
  {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}");
  {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "Pen");
  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(dataset, 2, "Used", "Pen");
  EXPECT_TRUE(result_{_ITEM_} == &{_ITEM_}[2])
      << "The returned {_ITEM_} should be the third {_ITEM_} in the {_ITEM_} list.";
  ASSERT_STREQ((dataset[0].list)->{_ITEM_}->{_ITEM_}_name, "{_ITEM1_}")
      << "The first item in {_CONTAINER_} 'New' should be {_ITEM1_}.";
  ASSERT_STREQ((dataset[0].list)->next->{_ITEM_}->{_ITEM_}_name, "Pen")
      << "The second item in {_CONTAINER_} 'New' should be Pen.";
  EXPECT_TRUE(dataset[1].list == NULL) << "The {_CONTAINER_} 'Used' should be empty";
}

TEST(ProjectTests, Change_{_ITEM_}_not_included) {
  reset_dataset();
  {_ITEM_}Data* result_{_ITEM_} =
      {_CONTAINER_}_change(dataset, 2, {_ITEM_}, 4, "Laptop", "Used", "New");
  EXPECT_TRUE(result_{_ITEM_} == &{_ITEM_}[3])
      << "The returned {_ITEM_} should be the forth {_ITEM_} in the {_ITEM_} list.";
  ASSERT_STREQ({_ITEM_}[3].{_CONTAINER_}, "New")
      << "The {_CONTAINER_} of Laptop should be changed to 'New'.";
}

TEST(ProjectTests, Change_{_ITEM_}_with_incorrect_{_CONTAINER_}) {
  reset_dataset();
  {_ITEM_}Data* result_{_ITEM_} =
      {_CONTAINER_}_change(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}", "Used", "New");
  EXPECT_TRUE(result_{_ITEM_} == NULL)
      << "The returned result of changing {_ITEM1_} from 'Used' to 'New' should be "
         "NULL since there is no Used {_ITEM1_}.";

  result_{_ITEM_} = {_CONTAINER_}_change(dataset, 2, {_ITEM_}, 4, "Laptop", "New", "Old");
  EXPECT_TRUE(result_{_ITEM_} == NULL)
      << "The returned result of changing {_ITEM1_} from 'Used' to 'Old' should be "
         "NULL because there is no {_CONTAINER_} Old in the dataset.";
}

TEST(ProjectTests, Change_{_ITEM_}_to_duplicate_{_CONTAINER_}) {
  reset_dataset();
  {_ITEM_}Data* result_{_ITEM_} =
      {_CONTAINER_}_change(dataset, 2, {_ITEM_}, 4, "Pen", "Used", "New");
  EXPECT_TRUE(result_{_ITEM_} == NULL)
      << "The returned result of changing Pen from 'Used' to 'New' should be "
         "NULL since there is a New Pen exist in the list.";
  ASSERT_STREQ({_ITEM_}[2].{_CONTAINER_}, "Used")
      << "The {_CONTAINER_} of Used Pen should not be changed.";
}

TEST(ProjectTests, Change_{_ITEM_}_included) {
  reset_dataset();
  {_CONTAINER_}_add(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}");
  {_ITEM_}Data* result_{_ITEM_} =
      {_CONTAINER_}_change(dataset, 2, {_ITEM_}, 4, "{_ITEM1_}", "New", "Used");
  EXPECT_TRUE(result_{_ITEM_} == &{_ITEM_}[0])
      << "The returned {_ITEM_} should be the first {_ITEM_} in the {_ITEM_} list.";
  ASSERT_STREQ({_ITEM_}[0].{_CONTAINER_}, "Used")
      << "The {_CONTAINER_} of {_ITEM1_} should be changed to Used";
  ASSERT_STREQ((dataset[1].list)->{_ITEM_}->{_ITEM_}_name, "{_ITEM1_}")
      << "{_ITEM1_} should be the first item of dataset[1].";
  EXPECT_TRUE(dataset[0].list == NULL)
      << "The dataset[0].list should be NULL because the {_CONTAINER_} New has no "
         "item.";
}

// PRIVATE_BEGIN

void resetdataset() {
  for (int i = 0; i < 4; i++) {
    private_dataset[i].list = NULL;
  }
}

int grader_add({_CONTAINER_} dataset[], int number_of_categories, {_ITEM_}Data {_ITEM_}[],
               int number_of_{_ITEM_}, const char* {_ITEM_}_name) {
  int modified = 0;
  for (int i = 0; i < number_of_{_ITEM_}; i++) {
    if (strncmp({_ITEM_}[i].{_ITEM_}_name, {_ITEM_}_name, MAX_LEN) == 0) {
      {_ITEM_}Node* newNode = ({_ITEM_}Node*)(malloc(sizeof({_ITEM_}Node)));
      newNode->{_ITEM_} = &{_ITEM_}[i];
      for (int j = 0; j < number_of_categories; j++) {
        if (strncmp(dataset[j].name, newNode->{_ITEM_}->{_CONTAINER_}, MAX_LEN) == 0) {
          // add node into this {_CONTAINER_}
          {_ITEM_}Node* preNode = NULL;
          {_ITEM_}Node* curNode = dataset[j].list;
          while (curNode && strncmp(newNode->{_ITEM_}->{_ITEM_}_name,
                                    curNode->{_ITEM_}->{_ITEM_}_name, MAX_LEN) > 0) {
            preNode = curNode;
            curNode = curNode->next;
          }

          if (curNode && strncmp(newNode->{_ITEM_}->{_ITEM_}_name,
                                 curNode->{_ITEM_}->{_ITEM_}_name, MAX_LEN) == 0) {
            break;
          }

          newNode->next = curNode;
          if (preNode != NULL) {
            preNode->next = newNode;
          } else {
            dataset[j].list = newNode;
          }
          modified = 1;
        }
      }
    }
  }
  return modified;
}

{_ITEM_}Data* grader_remove({_CONTAINER_} dataset[], int number_of_categories,
                        const char* {_CONTAINER_}, const char* {_ITEM_}_name) {
  for (int j = 0; j < number_of_categories; j++) {
    if (strncmp(dataset[j].name, {_CONTAINER_}, MAX_LEN) == 0) {
      {_ITEM_}Node* preNode = NULL;
      {_ITEM_}Node* curNode = dataset[j].list;
      while (curNode &&
             strncmp({_ITEM_}_name, curNode->{_ITEM_}->{_ITEM_}_name, MAX_LEN) != 0) {
        preNode = curNode;
        curNode = curNode->next;
      }

      if (curNode) {
        if (preNode) {
          preNode->next = curNode->next;
        } else {
          dataset[j].list = curNode->next;
        }
        {_ITEM_}Data* result = curNode->{_ITEM_};
        free(curNode);
        return result;
      }
    }
  }
  // Cannot find the {_CONTAINER_} or the {_ITEM_} in the {_CONTAINER_}
  return NULL;
}

void test{_ITEM_}NameImmutablilty({_ITEM_}Data* private_{_ITEM_}) {
  for (int i = 0; i < 20; i++) {
    EXPECT_TRUE(strcmp(private_{_ITEM_}[i].{_ITEM_}_name,
                       private_{_ITEM_}_backup[i].{_ITEM_}_name) == 0)
        << "The {_ITEM_} names in the array should not be changed";
  }
}

void testLinkedList({_ITEM_}Node* node, int index[], int l) {
  int i;
  for (i = 0; i < l && node != NULL; i++, node = node->next) {
    // printf("TEST: %s vs %s\n", node->{_ITEM_}->{_ITEM_}_name,
    // private_{_ITEM_}[index[i]].{_ITEM_}_name);
    EXPECT_TRUE(node->{_ITEM_} == &private_{_ITEM_}[index[i]])
        << "The dataset has incorrect nodes or order of nodes in the "
           "linkedList";
  }

  EXPECT_TRUE(node == NULL) << "One or more {_CONTAINER_} in the dataset have a "
                               "longer linkedList than expected "
                            << l;
  EXPECT_EQ(l, i) << "One or more {_CONTAINER_} in the dataset have a shorter "
                     "linkedList than expected "
                  << l;
}

int contains({_ITEM_}Node* head, const char* {_ITEM_}name) {
  for ({_ITEM_}Node* cur = head; cur; cur = cur->next) {
    if (!strncmp(cur->{_ITEM_}->{_ITEM_}_name, {_ITEM_}name, MAX_LEN)) {
      return 1;
    }
  }
  return 0;
}

TEST(ProjectTests, {_CONTAINER_}_add_one_with_same_name) {
  int result;
  resetdataset();
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  int c1[] = {0};
  int c2[] = {15};
  int c3[] = {10};
  int c4[] = {18};
  testLinkedList(private_dataset[0].list, c1, 1);
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4, 1);
  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_add_two_with_same_name) {
  int result;
  resetdataset();
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  int c1[] = {0, 12};
  int c2[] = {15};
  int c3[] = {10, 2};
  int c4[] = {18, 17};
  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 2);
  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_add_duplicate_{_ITEM_}) {
  int result;
  resetdataset();
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0 since "
                          "it should not add the same {_ITEM_} into the dataset";
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0 since "
                          "it should not add the same {_ITEM_} into the dataset";
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0 since "
                          "it should not add the same {_ITEM_} into the dataset";
  int c1[] = {0, 12};
  int c2[] = {15};
  int c3[] = {10, 2};
  int c4[] = {18, 17};
  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 2);
  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_add_multiple_with_same_name) {
  int result;
  resetdataset();
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "A");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  int c1[] = {0, 12};
  int c2[] = {13, 15};
  int c3[] = {10, 2};
  int c4[] = {3, 18, 17};
  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2, 2);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 3);
  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_add_multiple_unique) {
  int result;
  resetdataset();
  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "C");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "AB");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "XA");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "AX");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "DC");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "BC");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "D");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  int c1[] = {8};
  int c2[] = {5, 9};
  int c3[] = {6};
  int c4[] = {7};
  testLinkedList(private_dataset[0].list, c1, 1);
  testLinkedList(private_dataset[1].list, c2, 2);
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4, 1);
  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_add_all_{_ITEM_}) {
  int result;
  resetdataset();

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "C");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "AB");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "A");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "Y");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "XYZ");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "XA");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "AX");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "DC");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "B");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "BC");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "D");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  int c1[] = {8, 4, 0, 19, 12};
  int c2[] = {13, 5, 9, 15, 1};
  int c3[] = {14, 6, 10, 16, 2};
  int c4[] = {3, 7, 18, 11, 17};
  testLinkedList(private_dataset[0].list, c1, 5);
  testLinkedList(private_dataset[1].list, c2, 5);
  testLinkedList(private_dataset[2].list, c3, 5);
  testLinkedList(private_dataset[3].list, c4, 5);
  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_remove_only_with_same_name) {
  int result;
  resetdataset();
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  int c1[] = {0};
  int c2[] = {15};
  int c3[] = {10};
  int c4[] = {18};
  testLinkedList(private_dataset[0].list, c1, 1);
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4, 1);

  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[0])
      << "The returned {_ITEM_} is incorrect.";
  EXPECT_TRUE(private_dataset[0].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4, 1);

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[15])
      << "The returned {_ITEM_} is incorrect.";
  EXPECT_TRUE(private_dataset[0].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[1].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4, 1);

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[18])
      << "The returned {_ITEM_} is incorrect.";
  EXPECT_TRUE(private_dataset[0].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[1].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[3].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  testLinkedList(private_dataset[2].list, c3, 1);

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Fair", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[10])
      << "The returned {_ITEM_} is incorrect.";
  EXPECT_TRUE(private_dataset[0].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[1].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[2].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[3].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";

  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_remove_not_exist) {
  resetdataset();

  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "X");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poo", "X");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";

  {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  {_CONTAINER_}_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  int c1[] = {0, 12};
  int c2[] = {15};
  int c3[] = {10, 2};
  int c4[] = {18, 17};
  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 2);

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "Y");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poo", "Z");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "Z");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";

  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 2);

  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_remove_duplicate) {
  resetdataset();

  grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  grader_add(private_dataset, 4, private_{_ITEM_}, 20, "AB");
  int c1[] = {0};
  int c2[] = {15};
  int c3[] = {10};
  int c4[] = {7, 18};
  testLinkedList(private_dataset[0].list, c1, 1);
  testLinkedList(private_dataset[1].list, c2, 1);
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4, 2);

  {_CONTAINER_}_remove(private_dataset, 4, "Great", "X");
  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "X");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";

  testLinkedList(private_dataset[0].list, c1, 1);
  EXPECT_TRUE(private_dataset[1].list == NULL)
      << "The {_CONTAINER_} should be empty after the first remove.";
  ;
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4, 2);

  {_CONTAINER_}_remove(private_dataset, 4, "Poor", "X");
  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "X");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";
  int c4_removeX[] = {7};

  testLinkedList(private_dataset[0].list, c1, 1);
  EXPECT_TRUE(private_dataset[1].list == NULL)
      << "The {_CONTAINER_} should be empty after the first remove.";
  ;
  testLinkedList(private_dataset[2].list, c3, 1);
  testLinkedList(private_dataset[3].list, c4_removeX, 1);

  {_CONTAINER_}_remove(private_dataset, 4, "Poor", "AB");
  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "AB");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned {_ITEM_} should be NULL.";

  testLinkedList(private_dataset[0].list, c1, 1);
  EXPECT_TRUE(private_dataset[1].list == NULL)
      << "The {_CONTAINER_} should be empty after the first remove.";
  ;
  testLinkedList(private_dataset[2].list, c3, 1);
  EXPECT_TRUE(private_dataset[3].list == NULL)
      << "The {_CONTAINER_} should be empty after the first remove.";
  ;

  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_remove_multiple_with_same_name) {
  int result;
  resetdataset();
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "A");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";
  int c1[] = {0, 12};
  int c2[] = {13, 15};
  int c3[] = {10, 2};
  int c4[] = {3, 18, 17};
  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2, 2);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 3);

  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[0])
      << "The returned {_ITEM_} is incorrect.";
  int c1removeX[] = {12};
  testLinkedList(private_dataset[0].list, c1removeX, 1);
  testLinkedList(private_dataset[1].list, c2, 2);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 3);

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[15])
      << "The returned {_ITEM_} is incorrect.";
  int c2removeX[] = {13};
  testLinkedList(private_dataset[0].list, c1removeX, 1);
  testLinkedList(private_dataset[1].list, c2removeX, 1);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 3);

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[18])
      << "The returned {_ITEM_} is incorrect.";
  int c4removeX[] = {3, 17};
  testLinkedList(private_dataset[0].list, c1removeX, 1);
  testLinkedList(private_dataset[1].list, c2removeX, 1);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4removeX, 2);

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Fair", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[10])
      << "The returned {_ITEM_} is incorrect.";
  int c3removeX[] = {2};
  testLinkedList(private_dataset[0].list, c1removeX, 1);
  testLinkedList(private_dataset[1].list, c2removeX, 1);
  testLinkedList(private_dataset[2].list, c3removeX, 1);
  testLinkedList(private_dataset[3].list, c4removeX, 2);

  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, {_CONTAINER_}_remove_all) {
  int result;
  resetdataset();
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "C");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "AB");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "A");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "Y");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "XYZ");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "XA");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "AX");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "DC");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "B");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "BC");
  EXPECT_EQ(result, 0) << "The return value of {_CONTAINER_}_add should be 0";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "D");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "Z");
  EXPECT_EQ(result, 1) << "The return value of {_CONTAINER_}_add should be 1";

  int c1[] = {8, 4, 0, 19, 12};
  int c2[] = {13, 5, 9, 15, 1};
  int c3[] = {14, 6, 10, 16, 2};
  int c4[] = {3, 7, 18, 11, 17};
  testLinkedList(private_dataset[0].list, c1, 5);
  testLinkedList(private_dataset[1].list, c2, 5);
  testLinkedList(private_dataset[2].list, c3, 5);
  testLinkedList(private_dataset[3].list, c4, 5);

  {_ITEM_}Data* result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[0])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "Y");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[1])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Fair", "Z");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[2])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "A");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[3])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "B");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[4])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "C");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[5])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Fair", "D");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[6])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "AB");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[7])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "AX");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[8])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "DC");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[9])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Fair", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[10])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "Y");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[11])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "Z");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[12])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "A");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[13])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Fair", "B");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[14])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Great", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[15])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Fair", "Y");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[16])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "Z");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[17])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Poor", "X");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[18])
      << "The returned {_ITEM_} is incorrect.";

  result_{_ITEM_} = {_CONTAINER_}_remove(private_dataset, 4, "Excellent", "Y");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[19])
      << "The returned {_ITEM_} is incorrect.";

  EXPECT_TRUE(private_dataset[0].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[1].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[2].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";
  EXPECT_TRUE(private_dataset[3].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";

  test{_ITEM_}NameImmutablilty(private_{_ITEM_});
}

TEST(ProjectTests, Change_{_ITEM_}_not_included_advance) {
  {_ITEM_}Data* result_{_ITEM_};
  resetdataset();

  for (int j = 1; j < 5; j++) {
    for (int i = 0; i < 5; i++) {
      result_{_ITEM_} = {_CONTAINER_}_change(
          private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
          private_cnames[(i + j) % 4], private_cnames[(i + j + 1) % 4]);
      EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[i + 5])
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }

  int result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");

  for (int j = 1; j < 5; j++) {
    for (int i = 0; i < 5; i++) {
      result_{_ITEM_} = {_CONTAINER_}_change(
          private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
          private_cnames[(i + j) % 4], private_cnames[(i + j + 1) % 4]);
      EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[i + 5])
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }

  result_{_ITEM_} = grader_remove(private_dataset, 4, "Great", "X");

  for (int j = 1; j < 5; j++) {
    for (int i = 0; i < 5; i++) {
      result_{_ITEM_} = {_CONTAINER_}_change(
          private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
          private_cnames[(i + j) % 4], private_cnames[(i + j + 1) % 4]);
      EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[i + 5])
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "Y");

  for (int j = 1; j < 5; j++) {
    for (int i = 0; i < 5; i++) {
      result_{_ITEM_} = {_CONTAINER_}_change(
          private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
          private_cnames[(i + j) % 4], private_cnames[(i + j + 1) % 4]);
      EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[i + 5])
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }
}

TEST(ProjectTests, Change_{_ITEM_}_with_incorrect_{_CONTAINER_}_advance) {
  {_ITEM_}Data* result_{_ITEM_};
  resetdataset();
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                    private_fnames[i], private_cnames[j], "X");
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }

  for (int i = 0; i < 5; i++) {
    result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                  private_fnames[i + 5], private_cnames[i % 4],
                                  private_cnames[(i + 3) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";

    result_{_ITEM_} = {_CONTAINER_}_change(
        private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
        private_cnames[(i + 2) % 4], private_cnames[(i + 1) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";
  }

  int result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                    private_fnames[i], private_cnames[j], "X");
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }

  for (int i = 0; i < 5; i++) {
    result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                  private_fnames[i + 5], private_cnames[i % 4],
                                  private_cnames[(i + 3) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";

    result_{_ITEM_} = {_CONTAINER_}_change(
        private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
        private_cnames[(i + 2) % 4], private_cnames[(i + 1) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";
  }

  result_{_ITEM_} = grader_remove(private_dataset, 4, "Great", "X");

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                    private_fnames[i], private_cnames[j], "X");
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }

  for (int i = 0; i < 5; i++) {
    result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                  private_fnames[i + 5], private_cnames[i % 4],
                                  private_cnames[(i + 3) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";

    result_{_ITEM_} = {_CONTAINER_}_change(
        private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
        private_cnames[(i + 2) % 4], private_cnames[(i + 1) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";
  }

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "Y");

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                    private_fnames[i], private_cnames[j], "X");
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
    }
  }

  for (int i = 0; i < 5; i++) {
    result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20,
                                  private_fnames[i + 5], private_cnames[i % 4],
                                  private_cnames[(i + 3) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";

    result_{_ITEM_} = {_CONTAINER_}_change(
        private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
        private_cnames[(i + 2) % 4], private_cnames[(i + 1) % 4]);
    EXPECT_TRUE(result_{_ITEM_} == NULL)
        << "The returned result of the change with incorrect {_CONTAINER_} should "
           "be NULL.";
  }
}

TEST(ProjectTests, Change_{_ITEM_}_to_duplicate_{_CONTAINER_}_advance) {
  {_ITEM_}Data* result_{_ITEM_};
  resetdataset();

  for (int i = 0; i < 4; i++) {
    for (int j = i + 1; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "X",
                                    private_cnames[i], private_cnames[j]);
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change to duplicate {_CONTAINER_} should "
             "be NULL.";
    }
  }

  int result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  for (int i = 0; i < 4; i++) {
    for (int j = i + 1; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "X",
                                    private_cnames[i], private_cnames[j]);
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change to duplicate {_CONTAINER_} should "
             "be NULL.";
    }
  }

  result_{_ITEM_} = grader_remove(private_dataset, 4, "Great", "X");
  for (int i = 0; i < 4; i++) {
    for (int j = i + 1; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "X",
                                    private_cnames[i], private_cnames[j]);
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change to duplicate {_CONTAINER_} should "
             "be NULL.";
    }
  }

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "Y");
  for (int i = 0; i < 4; i++) {
    for (int j = i + 1; j < 4; j++) {
      result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "Y",
                                    private_cnames[i], private_cnames[j]);
      EXPECT_TRUE(result_{_ITEM_} == NULL)
          << "The returned result of the change to duplicate {_CONTAINER_} should "
             "be NULL.";
    }
  }

  result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "Z",
                                "Poor", "Excellent");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned result of the change to "
                                      "duplicate {_CONTAINER_} should be NULL.";

  result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "B",
                                "Excellent", "Fair");
  EXPECT_TRUE(result_{_ITEM_} == NULL) << "The returned result of the change to "
                                      "duplicate {_CONTAINER_} should be NULL.";
}

TEST(ProjectTests, Change_{_ITEM_}_included_advance) {
  {_ITEM_}Data* result_{_ITEM_};
  resetdataset();

  int result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "AB");
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "C");
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "AX");
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "DC");
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "D");

  for (int j = 1; j < 5; j++) {
    for (int i = 0; i < 5; i++) {
      result_{_ITEM_} = {_CONTAINER_}_change(
          private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
          private_cnames[(i + j) % 4], private_cnames[(i + j + 1) % 4]);
      EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[i + 5])
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
      EXPECT_TRUE(contains(private_dataset[(i + j + 1) % 4].list,
                           private_fnames[i + 5]));
    }
  }

  result_{_ITEM_} = grader_remove(private_dataset, 4, "Great", "C");
  for (int j = 1; j < 5; j++) {
    for (int i = 1; i < 5; i++) {
      result_{_ITEM_} = {_CONTAINER_}_change(
          private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
          private_cnames[(i + j) % 4], private_cnames[(i + j + 1) % 4]);
      EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[i + 5])
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
      EXPECT_TRUE(contains(private_dataset[(i + j + 1) % 4].list,
                           private_fnames[i + 5]));
    }
  }

  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "X");
  for (int j = 1; j < 3; j++) {
    for (int i = 1; i < 5; i++) {
      result_{_ITEM_} = {_CONTAINER_}_change(
          private_dataset, 4, private_{_ITEM_}, 20, private_fnames[i + 5],
          private_cnames[(i + j) % 4], private_cnames[(i + j + 1) % 4]);
      EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[i + 5])
          << "The returned result of the change with incorrect {_CONTAINER_} should "
             "be NULL.";
      EXPECT_TRUE(contains(private_dataset[(i + j + 1) % 4].list,
                           private_fnames[i + 5]));
    }
  }
  result = grader_add(private_dataset, 4, private_{_ITEM_}, 20, "C");

  int c1[] = {6, 0};
  int c2[] = {7, 5, 15};
  int c3[] = {8, 10};
  int c4[] = {9, 18};
  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2, 3);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4, 2);

  result_{_ITEM_} = grader_remove(private_dataset, 4, "Poor", "X");
  result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "DC",
                                "Poor", "Great");
  EXPECT_TRUE(result_{_ITEM_} == &private_{_ITEM_}[9])
      << "The returned result of the change with incorrect {_CONTAINER_} should be "
         "NULL.";

  int c2_addDC[] = {7, 5, 9, 15};
  testLinkedList(private_dataset[0].list, c1, 2);
  testLinkedList(private_dataset[1].list, c2_addDC, 4);
  testLinkedList(private_dataset[2].list, c3, 2);
  EXPECT_TRUE(private_dataset[3].list == NULL)
      << "The {_CONTAINER_} should be empty after removing the only item.";

  result_{_ITEM_} = {_CONTAINER_}_change(private_dataset, 4, private_{_ITEM_}, 20, "D",
                                "Excellent", "Poor");
  int c1_update[] = {0};
  int c4_update[] = {6};
  testLinkedList(private_dataset[0].list, c1_update, 1);
  testLinkedList(private_dataset[1].list, c2_addDC, 4);
  testLinkedList(private_dataset[2].list, c3, 2);
  testLinkedList(private_dataset[3].list, c4_update, 1);
}

// PRIVATE_END

int main(int argc, char** argv) {
testing:
  AddGlobalTestEnvironment(new basicDatabaseEnvironment);
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}