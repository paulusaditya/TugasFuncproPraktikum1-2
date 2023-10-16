List<String> reverseList(List<String> arr) {
  if (arr.isEmpty) {
    return [];
  } else {
    return [arr.last] + reverseList(arr.sublist(0, arr.length - 1));
  }
}
void main() {
  List<String> mylist = ['abc', 'def', 'efg'];
  List<String> reversedList = reverseList(mylist);
  print(reversedList);
}
