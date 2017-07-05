# def-acp
Python implementation of the Deferred Acceptance Algorithm as described in http://www.nber.org/papers/w13225

# Basic Description
Input files: 
Set_A: comma seperated list of members of Set A (example - A1,A2,A3,...,A_n)

Set_B: comma seperated list of members of Set B (example - B1,B2,B3,...,B_n)

A_choice: comma seperated ordered choice list (in increasing order) over members of Set_B. The first element on each line is the member of set_A whose choices are being enumerated.
example(\n
A1,B2,B3,B7\n
A2,B1,B9,B3\n
.
.
)

B_choice: comma seperated ordered choice list (in increasing order) over members of Set_A. The first element on each line is the member of set_B whose choices are being enumerated. There is also an option for members of Set_B to choose more than one candidate from Set_A. That number is the last entry in the ordered list. No number implies a single choice.
example(
B1,A3,A1,A10,A8,3
B2,A1,A4,A7,A2
B3,A3,A9,A18,A100,4
.
.
.
)

The algorithm is as follows:
In each iteration of the algorithm:
1. Each member of Set_B makes an offer to the highest ordered member(s) of Set_A from its list that have not already rejected its offer. For eg. in the first iteration B1 makes an offer to A3,A1,A10 - the first 3 highest ranked members in its choice list-, and B2 makes an offer to A1.
2. Each member of Set_A evaluates all the offers it has received in the current iteration. For eg. A1 evaluates offers from B1 and B2 (among others). 
3. Each member of Set_A "tentatively accepts" the offer from the highest ranked Set_B member in its choice list, and rejects all others. For eg. A1 "tentatively accepts" the offer from B2, and reject all others (Why? because B2 is a higher order choice than B1).
4. If a member of Set_B receives a "tentative accept" for ALL its required number of candidates, it shall not make any further offers in the next iteration. If it receives a "tentative accept" for only a partial number of required candidates from Set_A, then it shall make new offers for the remaining number of candidates from its ordered choice list that did not reject it in the current iteration. If there are no more candidates left to make offers to (even though it has not been accepted by its required number of candidates), it shall not participate in the next iteration.

The algorithm shall stop iterating if no more proposals are there to be made by Set_B members. At that point, members of Set_A shall immediately accept all the tentative offers, and the program terminates with a matching. The matching produced as output will be in the form of following two files:

Match_A_B: comma seperated list of Set_B members matched to Set_A members.
example(
A1,B2
A1,B9
.
.
.
)

Match_B_A: command seperated list of Set_A members matched to Set_B members. The number at the end of the list indicates how many members from Set_A remained unmatched. No number implies all were matched.

example(
B1,A10,A8,1
B2,A1
.
.
.
)

# Usage
$python def-acp.py [path to input files]

