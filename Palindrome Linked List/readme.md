Palindrome Linked List: https://leetcode.com/problems/palindrome-linked-list/

Method 1:
+ Create a list of numbers.
+ Compare it with its reverse form.

Method 2:
+ Find midpoint of linked list.
   + slow moves 1 step and fast moves 2 step.
   + so when fast reaches end, slow is at mid point.
+ While finding mid point, also reverse first half of list.
   + 1->2->3 => 1<-2<-3
+ Compare first half and second half.
