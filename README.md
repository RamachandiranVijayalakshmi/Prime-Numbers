# Prime Numbers
- **A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself**
- **Create a function that finds how many prime numbers there are, up to the given integer.**
## Sample Code for Prime Numbers
```
prime=0
  for val in range(2, int(num+1)):
     if all(val%int!=0 for int in range(2, val)):
        prime+=1
  return prime
```
## Example OutPut
```
Enter the number:34
2 to 34 prime numbers there are: 11 numbers
```
