def students(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
    students(Name="Abednego", Programme="BSC.Computer Science", Department="FOCIS")
    students(Name="Prince", Date="25/01/2025")