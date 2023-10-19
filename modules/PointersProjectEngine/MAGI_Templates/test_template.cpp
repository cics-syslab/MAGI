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