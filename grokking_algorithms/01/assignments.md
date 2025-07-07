- 1.1 Suppose you have a sorted list of 128 names, and
you’re searching through it using binary search. What’s
the maximum number of steps it would take?
    ans = 2 ** 7

- 1.2 Suppose you double the size of the list. What’s the
maximum number of steps now?    
    ans = 2 ** 8

- 1.3 You have a name, and you want tuo find the
person’s phone number in the phone book.
    ans = 2 ** 8

- Give the run time for each of these scenarios in terms of Big O.
    - 1.4 You have a phone number, and you want to find
    the person’s name in the phone book. (Hint: You’ll
    have to search through the whole book!)
        ans = O(n)

    - 1.5 You want to read the numbers of every person in
    the phone book.
        ans = O(n)

    - 1.6 You want to read the numbers of just the As. (This
    is a tricky one! It involves concepts that are covered
    more in chapter 4. Read the answer—you may be
    surprised!)
        ans = O(n/26)