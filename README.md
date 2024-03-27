# Analytics Workshop

# Questions

## 1. 500,000th prime number

The first 3 prime numbers are `2`, `3`, and `5`. What is the 500,00th prime number?

_An efficient algorithm can solve this question within 10-15 seconds._

## 2. Shrek and Donkey

In the movie Shrek 2, how many times does Shrek say Donkey's name?

Speaking lines in transcripts are signified by a line starting with a character's name followed by a colon. For example, the line `Shrek: You're bothering me.` means the character `Shrek` said `You're bothering me.`

data: `shrek2.txt`

## 3. Hidden Number

In `hidden_number.csv`, the `red` x-y coordinate pairs display a secret number when plotted. What is the number?

data: `hidden_number.csv`

## 4. Cardinals and Cubs

Considering the 2000 (inclusive) - 2010 (inclusive) Major League Baseball seasons, find the difference in the average number of games won (column `W`) each season by the St. Louis Cardinals and Chicago Cubs.

Round your answer to the nearest integer.

data: `mlb_teams.csv`

## 5. Time Series - Tuesdays

Find the sum of all `value` entries where the `datetime` entry occured on a Tuesday.

Round your answer to the nearest integer.

data: `time_series.csv`

## 6. Hidden Number 2

Once more, a number is drawn out in dots by plotting a series of x-y coordinate pairs. However, many other dots are also contained in the dataset as noise. What is the hidden number?

data: `hidden_number2.csv`, `hidden_number2_mapping.csv`

## 7. Time Series - Evenings on the Weekend

Find the sum of all `value` entries where the `datetime` entry occured on a weekend (Saturday or Sunday) in between 6pm (inclusive) and 10pm (exclusive).

Round your answer to the nearest integer.

data: `time_series.csv`

## 8. St. Louis Cardinals Home runs

Considering the 2000 (inclusive) - 2010 (inclusive) Major League Baseball seasons, find the total number of home runs (column `HR`) hit by the St. Louis Cardinals.

data: `mlb_teams.csv`

## 9. Ceasar Cipher | Shrek 2

The Caesar cipher is one of the simplest and earliest known substitution ciphers, named after Julius Caesar, who is believed to have used it to communicate secretly with his generals. It is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Here's how it works:

- **Key**: The key for the Caesar cipher is an integer from 1 to 25, denoting the number of positions each letter in the plaintext is shifted.
- **Encryption**: To encrypt a message, each letter in the plaintext is shifted forward in the alphabet by the key value. For example, with a key of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on. When reaching the end of the alphabet, the letters wrap around, so 'Z' becomes 'C'. Non-alphabetic characters (such as spaces and punctuation) are left unchanged.
- **Example**: With a key of 3, the plaintext "HELLO" would be encrypted as "KHOOR".

<p align="center">
  <img
    src="./static/caesar cipher.png"
    alt="Caesar Cipher"
    width="300"
  />
</p>

Encrypt the transcript of Shrek 2 using the Caesar Cipher and a key of `12`. How many times does the series of characters `bduzoq otmdyuzs` (case insensitive) appear in the encrypted transcript?

data: `shrek2.txt`

## 10. Simulating Coefficient of Friction

When dropping a basketball on earth, the earth's gravity exerts a force on the ball downward. At the same time, air resistance exerts a frictional force upwards on the ball.

The force of gravity (downwards) is modeled as:

**Force of Gravity**: `mass * gravitional_constant`

The force of friction (upwards) can be simplified to:

**Force of Friction**: `k * velocity^2`

Therefore, the net downwards force exerted on the ball can modeled with:

**Net Force**: (`Force of Gravity`) - (`Force of Friction`)

And the overall relationship between the ball's net force, mass, and acceleration can be modeled with:

`Net Force` = `Mass of Ball` \* `Acceleration of Ball`

where `k` is a constant that describes the relationship between the frictional force and the square of the ball's velocity.

The free body diagram for this example looks like this:

<p align="center">
  <img
    src="./static/free body diagram.png"
    alt="Free Body Diagram"
    width="300"
  />
</p>

In many physics problems such as this example, the only way to solve the problem is to perform a computer simulation. **Solve for the unitless value `k`, given the following**:

- The ball is dropped from a height of `50 meters`
- The gravitational constant `g` = `9.81 m/(s^2)`
- The ball takes exactly `5 seconds` to hit the ground
- Use a simulation time step of `0.01 seconds` or less
- The ball's mass is 0.6 kg
- Assume the value of k is in between 0 and 1

**Round your answer to the nearest hundreth place, and then multiply your answer by 100.**

Example:

- k = 0.357, round to 0.360, multiply by 100 to get 36, **submit 36**
- k = 0.084, round to 0.080, multiply by 100 to get 8, **submit 8**
- k = 0.679, round to 0.680, multiple by 100 to get 68, **submit 68**
