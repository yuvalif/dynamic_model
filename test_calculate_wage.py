from unittest import TestCase
import gross_to_net


class TestGrossToNet(TestCase):
    def test_calculate_tax(self):
        reduced_income = 10000
        row_number = 1
        result = gross_to_net.calculate_tax(reduced_income, row_number)
        print(result)

    def test_calculate_eict(self):
        wage = 10000
        row_number = 1
        kids = 1
        result = gross_to_net.calculate_eict(wage, row_number, kids)
        print(result)

    def test_gross_to_net_single(self):
        wage = 10000
        row_number = 1
        kids = 1
        exemptions = gross_to_net.ded_and_ex[row_number][4]
        deductions = gross_to_net.ded_and_ex[row_number][2]
        result = gross_to_net.gross_to_net_single(row_number, kids, wage, exemptions, deductions)
        print(result)

    def test_gross_to_net_married(self):
        wage_w = 10000
        wage_h = 10000
        row_number = 1
        kids = 1
        exemptions = gross_to_net.ded_and_ex[row_number][3]
        deductions = gross_to_net.ded_and_ex[row_number][1]
        result = gross_to_net.gross_to_net_married(row_number, kids, wage_h, wage_w, exemptions, deductions)
        print(result)

    def test_gross_to_net(self):
        wage_w = 10000
        wage_h = 10000
        kids = 1
        t = 1
        age_index = 1
        result = gross_to_net.gross_to_net(kids, wage_h, wage_w, t, age_index)
        print(result)