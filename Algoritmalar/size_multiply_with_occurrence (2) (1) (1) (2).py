'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a  of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t,z):
    #Write your alghoritm here.
    max_multiply_value = 0
    max_substring = ""

    # Step 1: Generate all possible substring of t
    substrings = set() # to avoid duplicate values --> set
    n = len(t)
    for i in range(n): #start index
        for j in range(i+1,n+1): #end index
            substrings.add(t[i:j]) #slicing string to substrings
            #print(substrings)
    
    # Step 2: Count occurrences of each substring in z 
    for substring in substrings:
        count_occurrences = z.count(substring)
        # Step 3:Multiply the length of the substring by the count of occurrences in z.
        multiply_value = len(substring) * count_occurrences
        # Step 4: Update max_multiply_value 
        if multiply_value > max_multiply_value:
            max_multiply_value = multiply_value
            max_substring = substring
        # Step 5: Print the solution
    print(f"{max_substring} is a substring of t, and it occurs {z.count(max_substring)} times in z, len({max_substring}) x {z.count(max_substring)} = {max_multiply_value} is the solution")
    #return max_multiply_value, max_substring 


if __name__ == '__main__':
    solution = find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    #print("Solution:", solution)
