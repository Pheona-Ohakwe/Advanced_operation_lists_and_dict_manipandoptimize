# Lesson 1: Assignment | Lists and Dictionaries


# Advanced Operations on Python Lists
# Objective: Understand Python lists by exploring more complex operations, such as list comprehension, slicing, and sorting, and analyzing their time and space complexities.

# Problem Statement: Delve deeper into Python lists and master advanced operations. Implement various complex tasks using lists and analyze their efficiency in terms of time and space complexities.

# Task 1

# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter. Analyze the time and space complexity of this operation.
def squares_list(n):
    # Using list comprehension to create a list of squares of numbers from 1 to n
    squares = [i * i for i in range(1, n+1)]
    return squares


# Task 2

# Implement a function that has 3 parameters representing a list and 2 indices that will reverse a sublist within the list from index i to j (inclusive).
def reverse_sublist(lst, i, j):
    # Check if i and j are within valid bounds
    if i < 0 or j < 0 or i >= len(lst) or j >= len(lst) or i > j:
        raise ValueError("Invalid indices")

    # Reverse the sublist from index i to j
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


# Task 3

# Implement a function to merge two sorted lists into a single sorted list without using the built-in sorted function of list.sort method. 
# Expected Outcomes:

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    # Traverse both lists and compare elements
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append remaining elements of list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Append remaining elements of list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list





# Dictionary Manipulation and Optimization
# Objective: Understand Python dictionaries by exploring advanced manipulation techniques and optimization strategies.

# Problem Statement: Explore advanced manipulation techniques and optimization strategies for Python dictionaries. Implement various dictionary operations and optimize them for improved performance.

# Task 1

# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary
# dict_1 = {"a": 1, "b": 2, "c": 3}
# dict_2 = {"b": 4, "c": 5, "d": 6}
# # Expected Output
# {"a": 1, "b": 4, "c": 5, "d": 6}
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of dict1 to preserve its original content
    for key, value in dict2.items():
        merged_dict[key] = value  # Update or add key-value pairs from dict2
    
    return merged_dict

# Example usage:
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}

merged_dict = merge_dictionaries(dict_1, dict_2)
print(merged_dict)



# Task 2

# Implement a function to find the difference of two dictionaries, i.e., keys that are only in one of the dictionaries along with their values. 
# dict_1 = {"a": 1, "b": 2, "c": 3}
# dict_2 = {"b": 4, "c": 5, "d": 6}
# # Expected Output
# {"a": 1, "d": 6}
def dict_difference(dict1, dict2):
    diff_dict = {}
    
    # Check keys in dict1 that are not in dict2
    for key in dict1:
        if key not in dict2:
            diff_dict[key] = dict1[key]
    
    # Check keys in dict2 that are not in dict1
    for key in dict2:
        if key not in dict1:
            diff_dict[key] = dict2[key]
    
    return diff_dict

# Example usage:
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 4, "c": 5, "d": 6}

difference = dict_difference(dict_1, dict_2)
print(difference)


# Task 3
# Implement a function to count the frequency of each unique word in a list using a dictionary. *Bonus* Ignore case 
def count_word_frequency(word_list):
    word_freq = {}
    
    for word in word_list:
        # Convert the word to lowercase to ignore case sensitivity
        word = word.lower()
        
        # Update the frequency dictionary
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

# Example usage:
words = ["Apple", "apple", "banana", "Banana", "apple", "cherry"]
frequency = count_word_frequency(words)
print(frequency)
