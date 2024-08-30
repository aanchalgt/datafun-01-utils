''' ITERATION 3

Module: Datapulse Analytics - Insight at your fingertips.

In this iteration, we will declare some more variables.
We are going to convert our custom byline to a multiline f-string to make it easy to display the new information.'''



#####################################
#Declare global variables - we will display this information at the end in a smarter byline 
####################################

#boolean variable to indicate the field of company is a Global CRO
company_field : bool = True
#Integer variable for the number of years in operation
years_in_operation: int = 16
#List of strings representing the services offered by the company
services_offered: list = ["Data Analysis", "Machine Learning", "Clinical Research"]
#List of floats representing individual client satisfaction scores 
client_satisfaction_scores: list = [4.8, 4.9, 4.7, 5.0, 4.9]


#####################################
# Declare a global variable named byline.
# Making it a multiline f-string to show our information.
#####################################

byline: str = f"""
-----------------------------------------------------
Datapulse Analytics - Insight at your fingertips.
-----------------------------------------------------
Is a Global CRO:    {company_field}
Years in operation: {years_in_operation}
Services offered:   {services_offered}
Client rating:      {client_satisfaction_scores}
"""

#####################################
# Define the get_byline() Function.
#####################################

def get_byline() -> str:
   '''Return a byline for my analytics projects.'''
   return byline

#####################################
# Define a main() function for this module.
#####################################



def main() -> None:
    '''Print results of get_byline() when main() is called'''
    print(get_byline())


#####################################
# Conditional Execution 
#####################################

if __name__ == '__main__':
    main()
