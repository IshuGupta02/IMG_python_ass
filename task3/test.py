"""Test file for task3.py"""
import json
import unittest
import requests
import mysql.connector
from bs4 import BeautifulSoup
import task3
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import email_pass

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=email_pass.mysql,
    database="python_assignment",
    auth_plugin="mysql_native_password"
)
mydb_fake = mysql.connector.connect(
    host="localhost",
    user="root",
    password=email_pass.mysql,
    database="fake_python_assignment",
    auth_plugin="mysql_native_password"
)

USER_N="radhikagarg1601"
URL= "https://m.facebook.com/"+USER_N+"/about"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
mycursor = mydb_fake.cursor()
mycursor.execute("SELECT * FROM user where username=\'"+USER_N+"\'")
myresult1 = mycursor.fetchall()
for x in myresult1:
    name_ans=x[1]
    city_ans= x[2]
    work_ans= json.loads(x[3])


class Test(unittest.TestCase):
    """Contains methods to check
    functioning of methods of task3.py"""
    def test_scrap(self):
        """testing scrap function of task3.py"""

        usname="random"
        with self.assertRaises(ValueError):
            task3.scrap(usname)

        usname="utkarsh.parkhi.1"
        self.assertEqual(task3.scrap(usname), "Task completed!")

        usname="radhikagarg1601"
        self.assertEqual(task3.scrap(usname), "Task completed!")

    def test_check(self):
        """Testing check function of task3.py"""

        username1="anshul.d.sharma.7"
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT * FROM user where username=\'"+username1+"\'")
        myresult = mycursor1.fetchall()
        previous= task3.check(myresult)
        self.assertEqual(previous, None)

        username1="radhikagarg1601"
        mycursor1.execute("SELECT * FROM user where username=\'"+username1+"\'")
        myresult = mycursor1.fetchall()
        previous= task3.check(myresult)
        self.assertEqual(previous.name, name_ans)
        self.assertEqual(previous.city, city_ans)
        self.assertEqual(previous.work, work_ans)

    def test_find_work(self):
        """Testing find_work function of task3.py"""

        list_ans= task3.find_work(USER_N, soup)
        self.assertEqual(list_ans, work_ans)

    def test_find_name(self):
        """Testing find_name function of task3.py"""

        name= task3.find_name(USER_N, soup)
        self.assertEqual(name, name_ans)

    def test_find_city(self):
        """Testing find_city function of task3.py"""

        city= task3.find_city(USER_N, soup)
        self.assertEqual(city, city_ans)

    def test_show(self):
        """
        """
        person=task3.Person(name= "Ishu Gupta")
        expected_ans = "My name is Ishu Gupta and my current city is Roorkee\n"
        with patch('sys.stdout', new = StringIO()) as fake_out:
            person.show()
            self.assertEqual(fake_out.getvalue(), expected_ans)

if __name__=='__main__':

    unittest.main()
