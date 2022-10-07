# netsalary = grosssalary - deductions
# grosssalary = basicsalary + allowances

# allowances = hra(22% of basicsalary) + da(18% of basicsalary) +ta(10% of basicsalary)

# deductions = proftax(if basicsalary > 8000 the 200 else 150) + pf(12% of basicsalary) + insurance(8% of basicsalary)


def salaryy(Basicsalary):
    hra = (22/100)*(Basicsalary)
    da = (18/100)*(Basicsalary)
    ta = (10/100)*(Basicsalary)
    pf = (12/100)*(Basicsalary)
    insurance = (8/100)*(Basicsalary)

    allowances = hra + da + ta

    gross_salary = Basicsalary + allowances

    if Basicsalary > 8000:
        proftax = 200
    else:
        proftax = 150

    deductions = proftax + pf + insurance
    netsalary = gross_salary - deductions

    print(netsalary)
    print(gross_salary)
    print(deductions)
    print(allowances)  



bsalary = int(input("enter the salary "))
salaryy(bsalary)



    

