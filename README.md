# IMG_python_assignment

This Assignment consists of following tasks:- 
1. Get AC on following questions using python 3
  a. http://codeforces.com/problemset/problem/118/A
  b. http://codeforces.com/problemset/problem/160/A
  c. http://codeforces.com/problemset/problem/263/A
2. Create a matrix class using nested lists
   Create following functions (use magic methods wherever possible) 
      Add
      Subtract
      Multiply
      Determinant (only for square matrices)
      Exponentiation
   Create proper unit tests to ensure all functions are working

3. WEB SCRAPING (optional for designers)
  1. Create a mysql database with table “user”. The only condition for the table is that it should have a column “username” and rows with “username”(facebook usernames) . Simply you should have a table with the given usernames.
  2. Create a decorator for functions with a parameter username which checks if the particular username exists in the above defined table, runs the function if it exists, throws an exception otherwise.
  3. Create a class “Person” with a constructor that instantiates its object with the mandatory argument “name” and the optional arguments “work”(list) and “city”(string). The class should also have a function show() which prints “My name is {self.name} and my current city is {self.city}”. 
  Note: If the parameters work is not passed, the object parameter work must not be assigned (i.e. obj.work should throw an exception) and if the parameter city is not passed then self.city should be stored as “Roorkee”.
  4. Create a function scrap(username) which scrapes the name(string), current city(string), work(list) and favourites(dictionary) from the facebook page (https://en-gb.facebook.com/{username}), prints the dictionary corresponding to the favourites (if there exists any, else instead of showing empty dictionary prints that there are no favourites), then instantiate an object of class “Person” (described above) with required parameter “name” and optional parameters “city”(current city, scraped above) and “work”(same).
  Note: If there is empty list corresponding to work or there is no current city, the parameters must not be passed).
  5. Then finally create a check in the above made function scrap(username) that if we have already scraped the data corresponding to the given username, then instead of scraping the data again, run the function show() corresponding to the object that we created initially when we ran the method scrap(username)
  Create proper unittests for testing your code.
