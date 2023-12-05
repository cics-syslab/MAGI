#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <{_PROJECT_NAME_}.h>

int main() {
  char* names[5] = {"{_DESCRIPTOR1_}", "{_DESCRIPTOR2_}", "{_ITEM1_}", "{_ITEM2_}", "{_ITEM3_}"};
  {_CONTAINER_} {_PROJECT_NAME_}[2];
  {_CONTAINER_TYPE_} {_ITEM_}s[4];
  {_PROJECT_NAME_}[0].name = (char*)malloc(4); // however, note that the malloc arguments are different, 
  // ... so use string length (strlen(name) + 1)
  strcpy({_PROJECT_NAME_}[0].name, names[0]);
  {_PROJECT_NAME_}[0].list = NULL;
  {_PROJECT_NAME_}[1].name = (char*)malloc(5);
  strcpy({_PROJECT_NAME_}[1].name, names[1]);
  {_PROJECT_NAME_}[1].list = NULL;

  {_ITEM_}s[0].{_CONTAINER_} = (char*)malloc(4);
  {_ITEM_}s[0].{_ITEM_}_name = (char*)malloc(5);
  strcpy({_ITEM_}s[0].{_CONTAINER_}, names[0]);
  strcpy({_ITEM_}s[0].{_ITEM_}_name, names[2]);
  {_ITEM_}s[1].{_CONTAINER_} = (char*)malloc(4);
  {_ITEM_}s[1].{_ITEM_}_name = (char*)malloc(4);
  strcpy({_ITEM_}s[1].{_CONTAINER_}, names[0]);
  strcpy({_ITEM_}s[1].{_ITEM_}_name, names[3]);
  {_ITEM_}s[2].{_CONTAINER_} = (char*)malloc(5);
  {_ITEM_}s[2].{_ITEM_}_name = (char*)malloc(4);
  strcpy({_ITEM_}s[2].{_CONTAINER_}, names[1]);
  strcpy({_ITEM_}s[2].{_ITEM_}_name, names[3]);
  {_ITEM_}s[3].{_CONTAINER_} = (char*)malloc(5);
  {_ITEM_}s[3].{_ITEM_}_name = (char*)malloc(7);
  strcpy({_ITEM_}s[3].{_CONTAINER_}, names[1]);
  strcpy({_ITEM_}s[3].{_ITEM_}_name, names[4]);

  int result;
  printf("\n=======  Test {_CONTAINER_}_add  ========\n\n");
  result = {_CONTAINER_}_add({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "{_ITEM1_}");
  printf("The result should be 1 and your result is %i\n", result);
  printf(
      "The first item in {_CONTAINER_} '{_DESCRIPTOR1_}' is {_ITEM1_}. In your {_PROJECT_NAME_}, it is %s.\n",
      ({_PROJECT_NAME_}[0].list)->{_ITEM_}->{_ITEM_}_name);

  result = {_CONTAINER_}_add({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "Apple");
  printf("The result should be 0 and your result is %i\n", result);

  result = {_CONTAINER_}_add({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "{_ITEM2_}");
  printf("The result should be 1 and your result is %i\n", result);
  printf(
      "The Second item in {_CONTAINER_} '{_DESCRIPTOR1_}' is {_ITEM2_}. In your {_PROJECT_NAME_}, it is %s.\n",
      ({_PROJECT_NAME_}[0].list)->next->{_ITEM_}->{_ITEM_}_name);
  printf(
      "The first item in {_CONTAINER_} '{_DESCRIPTOR2_}' is {_ITEM2_}. In your {_PROJECT_NAME_}, it is %s.\n",
      ({_PROJECT_NAME_}[1].list)->{_ITEM_}->{_ITEM_}_name);

  printf("\n=======  Test {_CONTAINER_}_remove  ========\n\n");

  {_CONTAINER_TYPE_}* result_{_ITEM_} = {_CONTAINER_}_remove({_PROJECT_NAME_}, 2, "{_DESCRIPTOR1_}", "{_ITEM2_}");
  int comparison_result = (result_{_ITEM_} == &{_ITEM_}s[1]);
  printf(
      "The comparison result should be 1 because the returned {_ITEM_} should be "
      "the second {_ITEM_} in the {_ITEM_} list. Your result is %i.\n",
      comparison_result);

  result_{_ITEM_} = {_CONTAINER_}_remove({_PROJECT_NAME_}, 2, "{_DESCRIPTOR1_}", "{_ITEM2_}");
  printf(
      "The returned result of removing {_DESCRIPTOR1_} {_ITEM2_} again should be NULL(nil). Your "
      "result is %p.\n",
      result_{_ITEM_});

  result_{_ITEM_} = {_CONTAINER_}_remove({_PROJECT_NAME_}, 2, "{_DESCRIPTOR2_}", "{_ITEM2_}");
  comparison_result = (result_{_ITEM_} == &{_ITEM_}s[2]);
  printf(
      "The comparison result should be 1 because the returned {_ITEM_} should be "
      "the third {_ITEM_} in the {_ITEM_} list. Your result is %i.\n",
      comparison_result);
  printf(
      "The {_PROJECT_NAME_}[1].list should be NULL(nil) because the {_CONTAINER_} {_DESCRIPTOR2_} has "
      "no item. Your result is %p.\n",
      {_PROJECT_NAME_}[1].list);

  printf("\n=======  Test {_CONTAINER_}_change  ========\n\n");

  result_{_ITEM_} = {_CONTAINER_}_change({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "{_ITEM1_}", "{_DESCRIPTOR2_}", "{_DESCRIPTOR1_}");
  comparison_result = (result_{_ITEM_} == &{_ITEM_}s[3]);
  printf(
      "The comparison result should be 1 because the returned {_ITEM_} should be "
      "the forth {_ITEM_} in the {_ITEM_} list. Your result is %i.\n",
      comparison_result);
  printf(
      "The {_CONTAINER_} of {_ITEM1_} should be changed to '{_DESCRIPTOR1_}', and your {_ITEM1_}'s "
      "{_CONTAINER_} is '%s'.\n",
      {_ITEM_}s[3].{_CONTAINER_});

  result_{_ITEM_} = {_CONTAINER_}_change({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "{_ITEM1_}", "{_DESCRIPTOR2_}", "{_DESCRIPTOR1_}");
  printf(
      "The returned result of changing {_ITEM1_} from '{_DESCRIPTOR2_}' to '{_DESCRIPTOR1_}' should be "
      "NULL(nil). Your result is %p.\n",
      result_{_ITEM_});

  result_{_ITEM_} = {_CONTAINER_}_change({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "{_ITEM1_}", "{_DESCRIPTOR1_}", "Old");
  printf(
      "The returned result of changing {_ITEM1_} from '{_DESCRIPTOR2_}' to 'Old' should be "
      "NULL(nil) because there is no {_CONTAINER_} Old in the {_PROJECT_NAME_}. Your result "
      "is %p.\n",
      result_{_ITEM_});

  result_{_ITEM_} = {_CONTAINER_}_change({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "{_ITEM2_}", "{_DESCRIPTOR2_}", "{_DESCRIPTOR1_}");
  printf(
      "The returned result of changing {_ITEM2_} from '{_DESCRIPTOR2_}' to '{_DESCRIPTOR1_}' should be "
      "NULL(nil). Your result is %p.\n",
      result_{_ITEM_});
  printf(
      "The {_CONTAINER_} of {_ITEM2_} should not be changed from '{_DESCRIPTOR2_}' since the list "
      "aleady has {_ITEM2_} in {_CONTAINER_} '{_DESCRIPTOR1_}'. Your result {_CONTAINER_} is '%s'.\n",
      {_ITEM_}s[2].{_CONTAINER_});

  result_{_ITEM_} = {_CONTAINER_}_change({_PROJECT_NAME_}, 2, {_ITEM_}s, 4, "{_ITEM1_}", "{_DESCRIPTOR1_}", "{_DESCRIPTOR2_}");
  comparison_result = (result_{_ITEM_} == &{_ITEM_}s[0]);
  printf(
      "The comparison result should be 1 because the returned {_ITEM_} should be "
      "the first {_ITEM_} in the {_ITEM_} list. Your result is %i.\n",
      comparison_result);
  printf(
      "The {_CONTAINER_} of {_ITEM1_} should be changed to '{_DESCRIPTOR2_}', and your {_ITEM1_}'s "
      "{_CONTAINER_} is '%s'.\n",
      {_ITEM_}s[0].{_CONTAINER_});
  printf("{_ITEM1_} should be the first item of {_PROJECT_NAME_}[1]. Your result is %s.\n",
         ({_PROJECT_NAME_}[1].list)->{_ITEM_}->{_ITEM_}_name);
  printf(
      "The {_PROJECT_NAME_}[0].list should be NULL(nil) because the {_CONTAINER_} {_DESCRIPTOR1_} has "
      "no item. Your result is %p.\n",
      {_PROJECT_NAME_}[0].list);

  return 0;
}