
##   this application is used to convert a password according to the munged rules
## Munge my password
##Common words should still be avoided to be used as passwords. This challenge is about coding a very simple program that munges a given password
##(Modify Until Not Guessed Easily).
##Input
##A word, which is a string written in the alphabet abcdefghijklmnopqrstuvwxyz. It does not matter if the letters are lowercase or uppercase.
##Munging
##1.	Change any repeated sequence of a same letter to itself preceded by the number of times the letter was repeated (LLLL with 4L)
##2.	Change the first a with @
##3.	Change the first b with 8
##4.	Change the first c with (
##5.	Change the first d with 6
##6.	Change the first e with 3
##7.	Change the first f with #
##8.	Change the first g with 9
##9.	Change the first h with #
##10.	Change the first i with 1
##11.	Change the second i with !
##12.	Change the first k with <
##13.	Change the first l with 1
##14.	Change the second l with i
##15.	Change the first o with 0
##16.	Change the first q with 9
##17.	Change the first s with 5
##18.	Change the second s with $
##19.	Change the first t with +
##20.	Change the first v with >
##21.	Change the second v with <
##22.	Change the first w with uu
##23.	Change the second w with 2u
##24.	Change the first x with %
##25.	Change the first y with ?
##Rule 1 must be applied the needed number of times until it is not possible to apply it more. After that the rest of the rules are applied.
##Output The munged word
##Examples
##•	codegolf --> (0639o1#
##•	programming --> pr09r@2m1ng
##•	puzzles --> pu2z135
##•	passwords --> p@25uu0r6$
##•	wwww --> 4uu
##•	aaaaaaaaaaa --> 11a
##•	lllolllolll --> 3103io3l
##•	jjjmjjjj --> 3jm4j
import re
import tkinter
S =re.sub(r'(.)\1+', lambda m: str(len(m.group(0))) + m.group(1), input())
for a,b in zip('abcdefghiiklloqsstvvxyww',[*'@8(63#9#1!<1i095$+><%?','uu','2u']):S=S.replace(a,b,1)
for a,b in zip('ABCDEFGHIIKLLOQSSTVVXYWW',[*'@8(63#9#1!<1i095$+><%?','UU','2U']):S=S.replace(a,b,1)
print(S)
