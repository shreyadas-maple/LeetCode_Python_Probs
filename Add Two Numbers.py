def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    l1.reverse()
    l2.reverse()
    
    f_num = [str(x) for x in l1]
    s_num = [str(y) for y in l2]

    first_num = int("".join(f_num))

    second_num = int("".join(s_num))

    ans = first_num + second_num

    digits = [int(digit) for digit in str(ans)]

    digits.reverse()

    return digits

l1 = [2,4,3]
l2 = [5,6,4]

addTwoNumbers(l1, l2)
