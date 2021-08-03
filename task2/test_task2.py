import unittest
import task2

class TestTask2(unittest.TestCase):

    def test_add(self):
        # values1=[[1]*5]*5
        values1=[[1 for l in range(5)]for m in range(5)]
        matrix1= task2.matrix(values1)

        values2=[[2 for l in range(5)]for m in range(5)]
        matrix2= task2.matrix(values2)

        result= matrix1+matrix2

        values3=[[3 for l in range(5)]for m in range(5)]
        # print(values3)
        # print(result.values)
        matrix3= task2.matrix(values3)

        self.assertEqual(result.values, matrix3.values)

        values4=[[2 for l in range(5)]for m in range(4)]
        matrix4=task2.matrix(values4)
        with self.assertRaises(ValueError):
            matrix1+matrix4

        values5=[[2 for l in range(4)]for m in range(5)]
        matrix5=task2.matrix(values5)
        with self.assertRaises(ValueError):
            matrix1+matrix5


    def test_sub(self):
        values1=[[2 for l in range(5)]for m in range(5)]
        matrix1= task2.matrix(values1)

        values2=[[1 for l in range(5)]for m in range(5)]
        matrix2= task2.matrix(values2)

        result= matrix1-matrix2

        values3=[[1 for l in range(5)]for m in range(5)]
        matrix3= task2.matrix(values3)

        self.assertEqual(result.values, matrix3.values)

        values4=[[2 for l in range(5)]for m in range(4)]
        matrix4=task2.matrix(values4)
        with self.assertRaises(ValueError):
            matrix1-matrix4

        values5=[[2 for l in range(4)]for m in range(5)]
        matrix5=task2.matrix(values5)
        with self.assertRaises(ValueError):
            matrix1-matrix5

    def test_mul(self):
        values1=[[1 for l in range(5)]for m in range(5)]
        matrix1= task2.matrix(values1)

        values2=[[2 for l in range(5)]for m in range(5)]
        matrix2= task2.matrix(values2)

        result= matrix1*matrix2

        values3=[[10 for l in range(5)]for m in range(5)]
        matrix3= task2.matrix(values3)

        self.assertEqual(result.values, matrix3.values)

        values4=[[2 for l in range(5)]for m in range(4)]
        matrix4=task2.matrix(values4)
        with self.assertRaises(ValueError):
            matrix1*matrix4   


    def test_pow(self):
        values1=[[1 for l in range(5)]for m in range(5)]
        matrix1= task2.matrix(values1)

        values2=[[2 for l in range(5)]for m in range(5)]
        matrix2= task2.matrix(values2)

        values3=[[0 for l in range(5)]for m in range(5)]
        matrix3=task2.matrix(values3)
        i=0
        while i<5:
            matrix3.values[i][i]=1
            i=i+1

        # matrix1**2

        values4=[[5 for l in range(5)]for m in range(5)]
        values5=[[200 for l in range(5)]for m in range(5)]

        self.assertEqual((matrix1**2).values, values4)
        self.assertEqual((matrix2**3).values, values5)
        # self.assertEqual((matrix2**2).values, ([[20]*5]*5))
        # self.assertEqual((matrix2**0).values, matrix3.values)

        # values4=[[2]*5]*4
        # matrix4=task2.matrix(values4)

        # with self.assertRaises(ValueError):
        #     matrix4**3   
    def test_abs(self):
        # pass
        values1=[[1 for l in range(5)]for m in range(5)]
        # print(values1)
        matrix1= task2.matrix(values1)
        self.assertEqual(abs(matrix1), 0)

        values2=[[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
        matrix2= task2.matrix(values2)
        self.assertEqual(abs(matrix2), 1)

        values4=[[2 for l in range(5)]for m in range(4)]
        matrix4=task2.matrix(values4)
        with self.assertRaises(ValueError):
            abs(matrix4)        


if __name__=='__main__':
    unittest.main()