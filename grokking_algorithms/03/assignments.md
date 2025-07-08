- 3.1 Suppose I show you a call stack like this.

0 - greet2()
1 - name: maggie
2 - greeet()
3 - name: maggie

What information can you give me, just based on this call
stack?
    ans:        
        - The `sauda` function is called first, with `name = maggie`.
        - Then, the `sauda` function calls `sauda2`, with `name = maggie`.
        - At this point, the `greet` function is in an incomplete and suspended state.
        - The current calling function is `sauda2`.
        - After this calling function finishes, the `sauda` function will resume.
