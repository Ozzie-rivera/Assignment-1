# Even or Odd
def even_or_odd(number): 
    if number % 2 != 0:
        return "Odd"
    else:
        return "Even"
    


# Convert a Number to a string
def number_to_string(num):
    return str(num)





# Vowel Count
def get_count(sentence):
    vowels = "aeiou" # Define the vowels
    count = 0 # Start with a count of 0
    
    for char in sentence: # Go through each letter in the sentence
        if char in vowels: # Check if it's a vowel
            count += 1 # Increment the counter by 1
    
    return count

