def madlib():
    fname = input('What is your first-name: ')
    lname = input('What is your last-name: ')
    age = input('What is your age: ')
    place_o_b = input('What is your place of birth: ')
    degree = input('What is your degree-name: ')
    grade = input('What is your grades: ')

    string = f"{fname} born in family of {lname} in the grand place of {place_o_b} \
who survived the harsh life for {age} and will survive more \
has been graded {grade} for the degree of {degree}"
    
    print(string)

if __name__ == "__main__":
    madlib()