"""
This module defines CONSTANT and ERROR
"""

DEFAULT_NAME_LIST = ['David', 'John', 'Michael', 'Paul', 'Andrew', 'Peter', 'James', 'Robert', 'Mark', 'Richard', 'Susan', 'Stephen', 'Margaret', 'Sarah', 'Christopher', 'Ian', 'Steven', 'Thomas', 'William', 'Alan', 'Anthony', 'Patricia', 'Elizabeth', 'Mary', 'Simon', 'Julie', 'Brian', 'Karen', 'Christine', 'Daniel', 'Helen', 'Martin', 'Emma', 'Linda', 'Matthew', 'Kevin', 'Jean', 'Philip', 'Jane', 'Janet', 'Lisa', 'Gary', 'Claire', 'Nicola', 'Colin', 'Joan', 'Graham', 'Jennifer', 'Barbara', 'George', 'Neil', 'Keith', 'Michelle', 'Joanne', 'Angela', 'Carol', 'Ann', 'Laura', 'Lee', 'Jacqueline', 'Sharon', 'Rebecca', 'Jonathan', 'Stuart', 'Sandra', 'Chris', 'Louise', 'Catherine', 'Anne', 'Kenneth', 'Rachel', 'Kathleen', 'Alison', 'Adam', 'Amanda', 'Deborah', 'Nicholas', 'Darren', 'Edward', 'Samantha', 'Pauline', 'Sheila', 'Victoria', 'Caroline', 'Maureen', 'Gillian', 'Wendy', 'Pamela', 'Jason', 'Raymond', 'Dorothy', 'Ronald', 'Joseph', 'Benjamin', 'Barry', 'Derek', 'Joyce', 'Maria', 'Nigel', 'Tracey', 'Valerie', 'Craig', 'Charles', 'Diane', 'Roger', 'Tony', 'Elaine', 'Sally', 'Charlotte', 'Patrick', 'June', 'Anna', 'Eileen', 'Lesley', 'Lucy', 'Roy', 'Malcolm', 'Brenda', 'Adrian', 'Terence', 'Tracy', 'Kelly', 'Irene', 'Dawn', 'Geoffrey', 'Shirley', 'Trevor', 'Timothy', 'Clare', 'Amy', 'Doreen', 'Denise', 'Natalie', 'Sylvia', 'Donna', 'Marie', 'Ruth', 'Gemma', 'Hannah', 'Scott', 'Katie', 'Lorraine', 'Mohammed', 'Leslie', 'Judith', 'Paula', 'Yvonne', 'Julia', 'Jamie', 'Alex', 'Fiona', 'Heather', 'Stephanie', 'Eric', 'Sean', 'Dennis', 'Kate', 'Dean', 'Carl', 'Kim', 'Nick', 'Gordon', 'Andrea', 'Jack', 'Alexander', 'Frank', 'Wayne', 'Kerry', 'Suzanne', 'Carole', 'Rosemary', 'Joanna', 'Luke', 'Tina', 'Emily', 'Lynn', 'Sam', 'Shaun', 'Arthur', 'Audrey', 'Betty', 'Frederick', 'Tim', 'Kathryn', 'Hayley', 'Melanie', 'Janice', 'Sophie', 'Sue', 'Jill', 'Teresa', 'Samuel', 'Frances', 'Jayne', 'Doris', 'Beverley', 'Hazel', 'Terry', 'Norman', 'Katherine', 'Rita', 'Gareth', 'Jessica', 'Robin', 'Clive', 'Alice', 'Lynne', 'Marion', 'Zoe', 'Sara', 'Donald', 'Harry', 'Marjorie', 'Kirsty', 'Debbie', 'Ryan', 'Beryl', 'Russell', 'Josephine', 'Phillip', 'Ashley', 'Douglas', 'Albert', 'Oliver', 'Henry', 'Francis', 'Lauren', 'Anita', 'Phil', 'Jenny', 'Mandy', 'Gavin', 'Jeremy', 'Bernard', 'Georgina', 'Christina', 'Cheryl', 'Lynda', 'Jon', 'Danielle', 'Rachael', 'Diana', 'Debra', 'Stanley', 'Allan', 'Natasha', 'Leanne', 'Karl', 'Vera', 'Liam', 'Matt', 'Gerald', 'Florence', 'Joe', 'Jeffrey', 'Leonard', 'Julian', 'Jo', 'Kay', 'Evelyn', 'Antony', 'Elsie', 'Gladys', 'Edith', 'Edna', 'Nathan', 'Phyllis', 'Vanessa', 'Winifred', 'Lilian', 'Ellen', 'Stacey', 'Alexandra', 'Hilary', 'Marc', 'Rose', 'Annette', 'Gail', 'Iris', 'Carolyn', 'Victor', 'Jeanette', 'Ben', 'Ross', 'Ernest', 'Martyn', 'Veronica', 'Duncan', 'Jackie', 'Lorna', 'Maurice', 'Grace', 'Abdul', 'Aaron', 'Bryan', 'Hilda', 'Sonia', 'Justin', 'Joy', 'Alfred', 'Marilyn', 'Annie', 'Theresa', 'Reginald', 'Stewart', 'Harold', 'Iain', 'Eleanor', 'Dan', 'Olive', 'Violet', 'Melissa', 'Dominic', 'Ali', 'Norma', 'Mavis', 'Vincent', 'Muriel', 'Danny', 'Bob']


class GameError(Exception):
    def __init__(self, arg=""):
        self.arg = arg