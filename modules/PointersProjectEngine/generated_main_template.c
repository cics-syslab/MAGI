#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Project Name.h>

int main() {
  char* names[5] = {"Descriptor1", "Descriptor2", "Item1", "Item2", "Item3"};
  Container Project Name[2];
  Container Type Item Types[4];
  Project Name[0].name = (char*)malloc(4); // however, note that the malloc arguments are different, 
  // ... so use string length (strlen(name) + 1)
  strcpy(Project Name[0].name, names[0]);
  Project Name[0].list = NULL;
  Project Name[1].name = (char*)malloc(5);
  strcpy(Project Name[1].name, names[1]);
  Project Name[1].list = NULL;

  Item Types[0].Container = (char*)malloc(4);
  Item Types[0].Item Type_name = (char*)malloc(5);
  strcpy(Item Types[0].Container, names[0]);
  strcpy(Item Types[0].Item Type_name, names[2]);
  Item Types[1].Container = (char*)malloc(4);
  Item Types[1].Item Type_name = (char*)malloc(4);
  strcpy(Item Types[1].Container, names[0]);
  strcpy(Item Types[1].Item Type_name, names[3]);
  Item Types[2].Container = (char*)malloc(5);
  Item Types[2].Item Type_name = (char*)malloc(4);
  strcpy(Item Types[2].Container, names[1]);
  strcpy(Item Types[2].Item Type_name, names[3]);
  Item Types[3].Container = (char*)malloc(5);
  Item Types[3].Item Type_name = (char*)malloc(7);
  strcpy(Item Types[3].Container, names[1]);
  strcpy(Item Types[3].Item Type_name, names[4]);

  int result;
  printf("\n=======  Test Container_add  ========\n\n");
  result = Container_add(Project Name, 2, Item Types, 4, "Item1");
  printf("The result should be 1 and your result is %i\n", result);
  printf(
      "The first item in Container 'Descriptor1' is Item1. In your Project Name, it is %s.\n",
      (Project Name[0].list)->Item Type->Item Type_name);

  result = Container_add(Project Name, 2, Item Types, 4, "Apple");
  printf("The result should be 0 and your result is %i\n", result);

  result = Container_add(Project Name, 2, Item Types, 4, "Item2");
  printf("The result should be 1 and your result is %i\n", result);
  printf(
      "The Second item in Container 'Descriptor1' is Item2. In your Project Name, it is %s.\n",
      (Project Name[0].list)->next->Item Type->Item Type_name);
  printf(
      "The first item in Container 'Descriptor2' is Item2. In your Project Name, it is %s.\n",
      (Project Name[1].list)->Item Type->Item Type_name);

  printf("\n=======  Test Container_remove  ========\n\n");

  Container Type* result_Item Type = Container_remove(Project Name, 2, "Descriptor1", "Item2");
  int comparison_result = (result_Item Type == &Item Types[1]);
  printf(
      "The comparison result should be 1 because the returned Item Type should be "
      "the second Item Type in the Item Type list. Your result is %i.\n",
      comparison_result);

  result_Item Type = Container_remove(Project Name, 2, "Descriptor1", "Item2");
  printf(
      "The returned result of removing Descriptor1 Item2 again should be NULL(nil). Your "
      "result is %p.\n",
      result_Item Type);

  result_Item Type = Container_remove(Project Name, 2, "Descriptor2", "Item2");
  comparison_result = (result_Item Type == &Item Types[2]);
  printf(
      "The comparison result should be 1 because the returned Item Type should be "
      "the third Item Type in the Item Type list. Your result is %i.\n",
      comparison_result);
  printf(
      "The Project Name[1].list should be NULL(nil) because the Container Descriptor2 has "
      "no item. Your result is %p.\n",
      Project Name[1].list);

  printf("\n=======  Test Container_change  ========\n\n");

  result_Item Type = Container_change(Project Name, 2, Item Types, 4, "Item1", "Descriptor2", "Descriptor1");
  comparison_result = (result_Item Type == &Item Types[3]);
  printf(
      "The comparison result should be 1 because the returned Item Type should be "
      "the forth Item Type in the Item Type list. Your result is %i.\n",
      comparison_result);
  printf(
      "The Container of Item1 should be changed to 'Descriptor1', and your Item1's "
      "Container is '%s'.\n",
      Item Types[3].Container);

  result_Item Type = Container_change(Project Name, 2, Item Types, 4, "Item1", "Descriptor2", "Descriptor1");
  printf(
      "The returned result of changing Item1 from 'Descriptor2' to 'Descriptor1' should be "
      "NULL(nil). Your result is %p.\n",
      result_Item Type);

  result_Item Type = Container_change(Project Name, 2, Item Types, 4, "Item1", "Descriptor1", "Old");
  printf(
      "The returned result of changing Item1 from 'Descriptor2' to 'Old' should be "
      "NULL(nil) because there is no Container Old in the Project Name. Your result "
      "is %p.\n",
      result_Item Type);

  result_Item Type = Container_change(Project Name, 2, Item Types, 4, "Item2", "Descriptor2", "Descriptor1");
  printf(
      "The returned result of changing Item2 from 'Descriptor2' to 'Descriptor1' should be "
      "NULL(nil). Your result is %p.\n",
      result_Item Type);
  printf(
      "The Container of Item2 should not be changed from 'Descriptor2' since the list "
      "aleady has Item2 in Container 'Descriptor1'. Your result Container is '%s'.\n",
      Item Types[2].Container);

  result_Item Type = Container_change(Project Name, 2, Item Types, 4, "Item1", "Descriptor1", "Descriptor2");
  comparison_result = (result_Item Type == &Item Types[0]);
  printf(
      "The comparison result should be 1 because the returned Item Type should be "
      "the first Item Type in the Item Type list. Your result is %i.\n",
      comparison_result);
  printf(
      "The Container of Item1 should be changed to 'Descriptor2', and your Item1's "
      "Container is '%s'.\n",
      Item Types[0].Container);
  printf("Item1 should be the first item of Project Name[1]. Your result is %s.\n",
         (Project Name[1].list)->Item Type->Item Type_name);
  printf(
      "The Project Name[0].list should be NULL(nil) because the Container Descriptor1 has "
      "no item. Your result is %p.\n",
      Project Name[0].list);

  return 0;
}