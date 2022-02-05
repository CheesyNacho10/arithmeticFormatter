from arithmetic_arranger import *

# Correct test
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print("\n")
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
print("\n")
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
print("\n")
arithmetic_arranger(["12 + 33", "2453 - 23", "1 + 235", "200 - 1"], True)
print("\n")

# Fail tests
arithmetic_arranger(["12 + 33", "2453 - 23", "1 + 235", "200 - 1","32 + 698", "3801 - 2", "45 + 43"], True)
arithmetic_arranger(["121235 + 12323133", "25344453 - 123323", "1234342 + 265435", "22342300 - 1566"], True)
arithmetic_arranger(["12 / 33", "2453 * 23", "1 / 235", "200 * 1"], True)
arithmetic_arranger(["aD + c#", "hgf - sd", "two + three", "four - one"], True)