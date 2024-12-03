def read_from_file(filename):
  try:
    with open(filename, 'r') as file:
      data = file.readlines()
    return data
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

def findIndex(line,s):
    try:
        return line.index(s)
    except ValueError:
        return -1

filename = 'Day3/input.txt'  
file_content = read_from_file(filename)  

sum = 0
if file_content:
    for line in file_content:
        while findIndex(line,"mul(") != -1:
            i = line.index("mul(")
            line = line[:i] + line[i+4:]
            num1,num2 = "",""
            valid = True
            while line[i] != ',':
                if line[i].isdigit():
                    num1 += line[i]
                else:
                    valid = False
                    break
                i+=1
            if not valid:
                continue
            i+=1
            while line[i] != ')':
                if line[i].isdigit():
                    num2 += line[i]
                else:
                    print(line[i])
                    valid = False
                    break
                i+=1
            if line[i] == ')':
                sum += int(num1)*int(num2)
print(sum)
