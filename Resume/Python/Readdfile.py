#files
file_path = r"C:\Users\Benja\Desktop\noteCVM\Resume\Python\employee.txt"
employee_file = open(file_path, "r+")
#employee_file = open("employee.txt", "r")# r= read, w = write, a = append at the end, r+ = read and write

print(employee_file.readable()) # readable check if you can read from the file bool
print("------------------------")
print(employee_file.read()) # read au complet
print("------------------------")
employee_file.seek(0) # Move the file pointer back to the beginning
print(employee_file.readline()) #read first line
# print(employee_file.readline()) #read second line 
print("------------------------")
employee_file.seek(0) 
print(employee_file.readlines()) 

print("------------------------")
employee_file.seek(0) 
for employee in employee_file.readlines():
    print(employee)


print("------------------------")
employee_file.write("\nToby - Human Resources") # write at the end of the file \n = new line \t = tab \b = backspace \r = carriage return \f = form feed   \ooo = octal value \xhh = hexadecimal value 
# if we add w instead of r+ it will overwrite the file
# if we add a instead of r+ it will add at the end of the file

employee_file.close()

# html file, will create a new file
index_file = open("index.html", "w")# r= read, w = write, a = append at the end, r+ = read and write
index_file.write("<p>This is HTML</p>")
index_file.close() 


