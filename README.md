Honestly, it seems like no method worked particularly well, but certainly some went better thatn others
My second commit definitely worked the best, with the title table having 8790 collisions and the quote table having 7463 collisions. The title table had 1 empty space, and the quote table had no empty spaces. And constructing both tables took 1056 seconds
This commit, I used the DJB Hash function that I had found online, and the collision handling of linear probing. 

The second best commit was either 3 or 5, depending on whether you're aiming for less collisions or less empty space. 
Commit 3 had 8944 collisions in the title table, and 8224 in the quote table, whereas Commit 5 had 9687 in the title table and 8929 in the quote table, so if we're going for less collisions, 3 wins over 5. 
But, if we wanted less empty space, commit 5 had 236 empty spaces in the title table, and the quote table had 231, where commit 3 had 1943 in the title table and 1223 in the quote table.
Time is neglible, commit 3 took .83 seconds and 5 took .85 seconds. 
For both of these I used the DJB hash function, and linked lists, but for 5 I gave the linked list a size limit of 2, to decrease the amount of empty space, and mixed it with linear probing. 

The second worst commit was Commit 1, with 13328 collisions in the title table and 13770 in the quote table, althught it had no empty space, and it took 52.72 seconds. 
This commit I had tried making my own hash function and linear probing, and my hash function was not very good. 

The worst commit was commit 4. 
Although it did well on space, with the title table having 1 empty space (not sure how or why) and the quote table having none. 
It did the worst with collisions, however, at 14995 collisions in both tables, and taking 231.04 seconds to construct both tables. 
This commit I used a method I had found online called "Double Hashing" where you essentially keep hashing the key until it finds an empty space, 
clearly this method either does not work, or I did it wrong, and I have a feeling it was probably the latter. 
