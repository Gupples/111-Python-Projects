"""
This is a document to get some practice in for making and using classes. I will
have 3 teachers; each with a name, a subject they teach, and a classroom they
teach in. The first set will be wrong, but then fixed later, and the list
restated.

Notes to self:
NOTATION FOR OTHER PROGRAMMERS!!!
"_" prefix = Only use/modify this property if you know what you're doing.
"__" prefix = DO NOT USE!!!
When writing, it's okay. If you're modifying someone else's work, FOLLOW.
"""

class Teacher():
    # Constructor.
    def __init__(self, name, subject, room):
        self.name = name
        self.subject = subject
        self.room = room

    # Define Getters
    # Getter for name.
    @property
    def name(self):
        return self.__name

    # Getter for subject.
    @property
    def subject(self):
        return self.__subject

    # Getter for room.
    @property
    def room(self):
        return self.__room


    # Define Setters
    # Setter for name.
    @name.setter
    def name(self, value):
        self.__name = value

    # Setter for subject
    @subject.setter
    def subject(self, value):
        self.__subject = value

    # Setter for room 
    @room.setter
    def room(self, value):
        self.__room = value
    
    # Change __str__ so it automatically returns the right string.
    # VVV Tells the object what to print if the program tries to print it.
    def __str__(self) -> str:
        return f"{self.name} teaches {self.subject} in room {self.room}."

def meet_teachers(list: list):
    """
    This will read off a list of teachers and tell you who they are, what they
    teach, and where they teach it. 

    Parameters:
        Teachers (list): The list of the teachers
    Returns:
        nothing.
    """
    for item in list:
        print(item)
    print()


def main():
    # Declare 3 teachers.
    teacher1 = Teacher("Mr. Einstein", "Science", 116)
    teacher2 = Teacher("Mr. Miyagi", "Cooking", 225)
    teacher3 = Teacher("Prof. Snape", "Potions", 731)

    # Make our list of teachers
    teachers = [teacher1, teacher2, teacher3]

    # Read list of teachers.
    meet_teachers(teachers)

    print("Hold on; that's not right. Here's the actual list of teachers and",
    "what they teach.\n")

    # Fix list of teachers
    teacher1.name = "Ms. Frizzle"
    teacher1.room = 242

    teacher2.subject = "P.E."
    teacher2.room = 105
    
    teacher3.name = "Prof. McGonnagal"
    teacher3.subject = "Transfiguration"



    # Read correct list of teachers.
    meet_teachers(teachers)
    
if __name__ == "__main__":
    main()