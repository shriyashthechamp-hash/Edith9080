# Priority Welfare Eligibility (complex)

# Difficulty: Hard — lots of precedence rules
# Problem: Decide which single welfare scheme (if any) a person gets. Rules (priority A > C > B):

# Scheme A if: gender == "female" AND 21 ≤ age ≤ 65 AND (income ≤ 250000 OR (income ≤ 350000 AND has_disability == True)) AND (single_parent == True OR number_of_children ≥ 2)

# Scheme C if: age ≥ 60 AND income ≤ 300000

# Scheme B if: income ≤ 200000 AND 18 ≤ age ≤ 60 AND has_disability == False
# Return the highest priority scheme name or "Not eligible".

# Input: gender age income has_disability single_parent number_of_children
# Example: female 30 240000 True True 1 → Output: Scheme A

gender = input()
age = int(input())
income = int(input())
has_disability = input()
single_parent = input()
number_of_childern = int(input())

if gender == "Female " and age >= 21 and age <= 65 and income(income <= 250000 or (income <= 350000 and has_disability == True)) and (single_parent == True or number_of_children >= 2):
    print("Scheme A")

elif income <= 200000 and age >= 18 and age <= 60 and has_disability == False:
    print("Scheme B")

elif age >= 60 and income <= 300000:
    print("Scheme C")
    



