"""Milestone Lab 1: Luhn's Algorithm
Given: A series of credit card numbers
Return: Run Luhn's algorithm and other basic checks in order to verify that the credit card numbers are valid. 
*Note: I do have some previous coding experience, so let me know if something is not explained well and I will create additional comments.
References:
 1) Python Crash Course, 1st Ed, chapter 10
 2) https://www.guru99.com/reading-and-writing-files-in-python.html for help reading and writing to files
 3) https://stackoverflow.com/questions/28387169/python-iterate-and-change-elements-of-a-list for help in interating through CC list and editing results list
 4) https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca for help with absolute path issues 
 """

 #Read CC Number from user input or a file
    #use 'with open()' to open file 
    #Check length 
    #print error if length is not correct
    #create a list of strings. 
        #Each CC number is a single string. 
        #Each string is a single entry in the list. 

#Opens up the absolulte path to the testCCNums file
#Change the file path to whatever you need to run the appropriate file
with open(r"C:\Users\Matt's PC\Desktop\2021 Spring School Docs\ENGR 1100 Computational Innovation\Computational_Innovation_Homework\Module 5\Luhns_Algo_Lab\testCCNums.txt", "r") as CC_nums:
    CC_nums_list = CC_nums.readlines() #Takes each line from the imported file and puts it into a list

results_list = [] #Creates an empty list. This list will contain the type of card and its validity to the corresponding index of the CC_nums_list. These lists will be combined at the end.
for i in range(len(CC_nums_list)): #loops through the list of credit car numbers and strips the newline character from it
   CC_nums_list[i] = CC_nums_list[i].strip('\n')
   if len(CC_nums_list[i]) == 15 or len(CC_nums_list[i]) == 16: #This checks the length of the credit card number. If it is not 15 or 16 numerals long, it places an invalid length error into the corresponding spot on the results list.
      results_list.append("")
   else:
      results_list.append(" --------INVALID LENGTH")

 #Figure out type of CC accurately
    #Use if statements to ID CC type
    #If CC starts with 34 or 37 (IE index 0 is 3 and index 1 is 4 or 7)== American Express
    #If CC starts wtih 51-55 (inclusive) (IE index 0 is 5 and index 1 is 1-5) == Mastercard
    #If CC starts with 4 == Visa

#Loops through the CC_nums_list and, if the cc is the appropriate length, checks which type of card it is, and records it in the results_list.
for card in CC_nums_list:
    if len(card) == 16 or len(card)==15:
        if card[0] == '4':
            results_list[CC_nums_list.index(card)] = '--------VISA:'
        elif card[0] =='3' and (card[1]=='4' or card[1]=='7'):
            results_list[CC_nums_list.index(card)] = '--------AMERICAN EXPRESS:'
        elif card[0] == '5' and (card[1]=='1' or card[1]=='2' or card[1]=='3' or card[1]=='4' or card[1]=='5' ):
            results_list[CC_nums_list.index(card)] = '--------MASTERCARD:'
        else:
            pass

 #Run Luhn's Algorithm
    #Start at index [-2]
    #Take every other number from right to left
    #Stop when appropriate given the length of the string (avoid out of bounds error)
    #Multiply each of those numbers by 2
    #Add each new number together, treating multiple digits as two numbers (IE if 6*2 = 12, add them together 1+2=3)
    #Add each digit from the original list that was not already mulitplied and added together
    #Check if final sum is a multiple of 10. If yes, then valid. If not, then invalid
    
#loops through the CC_nums_list and applies Luhn's Algorithm
for card in CC_nums_list:
    if len(card) == 16 or len(card)==15:
        length = len(card)
        if length == 16:
            #The following takes each index, from -2 to -16, turns it into an int, multiplies it by 2, then turns it back into a string, then puts all the numerals back together.
            new_var_evens = str(int(card[-2])*2)+str(int(card[-4])*2)+str(int(card[-6])*2)+str(int(card[-8])*2)+str(int(card[-10])*2)+str(int(card[-12])*2)+str(int(card[-14])*2)+str(int(card[-16])*2)
            #The following just takes all the remaining numerals and adds them up.
            new_var_odds = int(card[-1])+int(card[-3])+int(card[-5])+int(card[-7])+int(card[-9])+int(card[-11])+int(card[-13])+int(card[-15])
        elif length == 15:
            #Does the same thing as line 65 but it only goes from indexes -2 to -14
            new_var_evens = str(int(card[-2])*2)+str(int(card[-4])*2)+str(int(card[-6])*2)+str(int(card[-8])*2)+str(int(card[-10])*2)+str(int(card[-12])*2)+str(int(card[-14])*2)
            new_var_odds = int(card[-1])+int(card[-3])+int(card[-5])+int(card[-7])+int(card[-9])+int(card[-11])+int(card[-13])+int(card[-15])
        evens_list = list(new_var_evens) #This takes the new_var_evens variable, calculated above, and creates a new list from it. Each digit is a separate index in the list. This is in order to add up all of the digits in the event one of the digits*2 is more than 1 digit.
        total_evens = 0
        #The following loop adds every digit together from the evens_list
        for i in evens_list:
            total_evens = total_evens + int(i)
        test_sum = total_evens + new_var_odds #Add up the remaining digits from the cc number.
        if test_sum%10 == 0: #Test to see if the new number is evenly divisible by 10
            results_list[CC_nums_list.index(card)] = results_list[CC_nums_list.index(card)] + " Valid" #adds "valid" to the corresponding results_list index if appropriate
        else:
            results_list[CC_nums_list.index(card)] = results_list[CC_nums_list.index(card)] + " Invalid" #otherwise adds "invalid" to the corresponding results_list

 #Output valid and invalid numbers
    #For each CC number, label it appropriately with the following format:
    # "################--------VISA:VALID" AKA CC number, 8 hyphens, CC name, "VALID"/"INVALID NUMBER"

#Creates a final list
final_list = []
#Loops through the CC_nums_list and adds the corresponding results_list to create the final list
for i in range(len(CC_nums_list)):
    final_list.append(CC_nums_list[i]+results_list[i])
print(final_list)

#writes the final list to the new .txt file called final_cc_list.txt. 
#Change the path as needed to produce the file in the appropriate location.
f = open(r"C:\Users\Matt's PC\Desktop\2021 Spring School Docs\ENGR 1100 Computational Innovation\Computational_Innovation_Homework\Module 5\Luhns_Algo_Lab\final_cc_list.txt", 'w+')
for i in range(len(CC_nums_list)): #Writes each number and the valid/invalid statement to a new line on the new text file.
    f.write(final_list[i] + '\n')
f.close() #Closes the new file.
