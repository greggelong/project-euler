# project-euler
a place to hold some code inspired by projecteuler.net 

code in python to solve the problems

code in p5js to visualize it in a more creative way.

![euler1.png](euler1.png)

[see it live here](https://editor.p5js.org/greggelong/full/2L_umf2pF)

Some fun with projecteuler.net. The site gives you “a series of challenging mathematical/computer programming problems that will require more than just mathematical insights to solve.” I solved problem one in #python3 and entered the result, which is a 6 digit number, which I am not showing because they request that you don’t share. But in addition to just a text based solution I have also visualized problem 1 using #p5js. The problem: Find the sum of all the multiples of 3 or 5 below 1000. Here multiples of 3 are red, multiples of 5 are blue, multiples of both are purple, and white are not multiples. All this plotted on a grid that varies in size from 30 to 45. I didn’t visualize the sum. I think it makes a nice pattern.

---------
![euler9.png](euler9.png)

[see it live here](https://editor.p5js.org/greggelong/full/H8vWIW8Eh)

Another visualization of a projecteuler.net problem. In #p5js This is problem nine. “A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.” The solutions for triples that equal 1000 are the two yellow dots at the bottom right of the first picture. Why are there two solutions when it says there should be one? Well, I have plotted the ‘a’ and ‘b’ as ‘x’ and ‘y’ so my brute force included when the values of ‘a’ and ‘b’ are swapped. I first solved it in python using the Diophantus method which I read about in Ian Stewarts book “Cabinet of Mathematical Curiosities” the p5js version is just brute force with for loops. #creativecoding
