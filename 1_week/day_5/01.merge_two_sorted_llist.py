def mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    ptr1,ptr2=(head1,head2) if head1.data<head2.data else (head2,head1)
    res=ptr1
    while ptr1 and ptr2:
        while ptr1.next and ptr1.next.data<ptr2.data:
            ptr1=ptr1.next
        ptr1.next,ptr2=ptr2,ptr1.next
        ptr1=ptr1.next
    return res