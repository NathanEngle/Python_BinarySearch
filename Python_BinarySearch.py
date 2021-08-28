#Nathan Engle
#August 26, 2021
#Program Description: A Python-based implementation of a merge sort and binary search. A simple menu system gives the options of sorting/searching a list of numbers or words.
#Sample data provided consists of 2000 random integers and 2000 random words

from sys import exit as sys_exit
def main():
    while True: #run forever
        print("Binary Search")
        print("Enter 1 to search a list of numbers")
        print("Enter 2 to search a list of words")
        print("Enter 3 to exit the program")

        user_choice = input()

        if user_choice == "1":
            f_numbers = open("numbers.txt", "r")
            list_of_numbers = list(map(int, f_numbers.readlines())) #cast every line of numbers.txt to an int and return it as a list
            merge_sort(list_of_numbers)

            print("Enter value to search: ", end = "")
            user_val = input()
            found = binary_search(list_of_numbers, int(user_val))
            if found:
                print("value was found!")
            else:
                print("value was not found")

        elif user_choice == "2":
            f_words = open("words.txt", "r")

            #different method of reading file
            #this ignores the \n at the end of each word
            list_of_words = f_words.read().splitlines()
            merge_sort(list_of_words)

            print("Enter value to search: ", end = "")
            user_val = input()
            found = binary_search(list_of_words, user_val)
            if found:
                print("value was found!")
            else:
                print("value was not found")
        elif user_choice == "3":
            print("Exiting program...")
            sys_exit(0) #proper safe exit
        else:
            print("Your choice of " + user_choice + " was not understood")


def merge_sort(arr):
    if len(arr) > 1:
        #find the midpoint, and split the list
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        #recursively call merge_sort on the newly split lists until they are of size 1
        merge_sort(left)
        merge_sort(right)

        #iterators
        itr_left = 0
        itr_right = 0
        itr_main = 0

        #while left and right have elements, compare to each other and add the smaller value to arr
        while (itr_left < len(left) and itr_right < len(right)):
            if left[itr_left] < right[itr_right]:
                arr[itr_main] = left[itr_left]
                itr_left += 1
            else:
                arr[itr_main] = right[itr_right]
                itr_right += 1
            itr_main += 1

        #these two loops are used when left and right are not the same length
        #simple clean up in which the remaining elements of either list are appended to arr
        while (itr_left < len(left)):
            arr[itr_main] = left[itr_left]
            itr_left += 1
            itr_main += 1

        while (itr_right < len(right)):
            arr[itr_main] = right[itr_right]
            itr_right += 1
            itr_main += 1


def binary_search(arr, value):
    if len(arr) == 1:
        return arr[0] == value
    
    mid = len(arr) // 2
    value_at_mid = arr[mid]
    if (value_at_mid) > value:
        return binary_search(arr[:mid], value)
    elif value_at_mid < value:
        return binary_search(arr[mid:], value)
    else: #mid has been found to be equal to value
        return True

if __name__ == "__main__":
    main()