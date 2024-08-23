#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fullname(first_name, last_name):
    return first_name + " " + last_name

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = fullname(first_name, last_name)

    print("Full name:", full_name)

if __name__ == "__main__":
    main()


# In[ ]:





# In[2]:


def string_alternative(input_str):
    return input_str[::2]

input_str = "Good evening"
result = string_alternative(input_str)
print(result) 


# In[ ]:





# In[6]:


from collections import defaultdict

def count_words_in_line(line):
    words = line.split()
    word_count = defaultdict(int)
    
    for word in words:
        word_count[word] += 1
    
    return word_count

with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    overall_word_count = defaultdict(int)

    lines = infile.readlines()

    for line in lines:
        outfile.write(line)
        line_word_count = count_words_in_line(line.strip())
        
        for word, count in line_word_count.items():
            overall_word_count[word] += count

    outfile.write("\nWord_Count:\n")
    for word, count in overall_word_count.items():
        outfile.write(f"{word}: {count}\n")


# In[ ]:





# In[ ]:


heights_in_inches = []

n = int(input("Enter the number of customers: "))

for i in range(n):
    height = float(input(f"Enter height of customer {i+1} in inches: "))
    heights_in_inches.append(height)

heights_in_cm = []

for height in heights_in_inches:
    height_in_cm = height * 2.54
    heights_in_cm.append(round(height_in_cm, 2))

print("Heights in inches:", heights_in_inches)
print("Heights in centimeters:", heights_in_cm)


# In[ ]:





# In[ ]:


heights_in_inches = [float(input(f"Enter height of customer {i+1} in inches: ")) for i in range(int(input("Enter the number of customers: ")))]

heights_in_cm = [round(height * 2.54, 2) for height in heights_in_inches]

print("Heights in inches:", heights_in_inches)
print("Heights in centimeters:", heights_in_cm)


# In[ ]:




