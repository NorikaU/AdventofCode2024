def read_from_file(filename):
  """Reads data from a file and returns it as a string.

  Args:
    filename: The name of the file to read from.

  Returns:
    The contents of the file as a string.
  """

  try:
    with open(filename, 'r') as file:
      data = file.readlines()
    return data
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

filename = 'Day1/inputd1.txt'
file_content = read_from_file(filename)
list1,list2 = [],[]

sum = 0
if file_content:
    for line in file_content:
        x,y, = line.split()
        list1.append(int(x))
        list2.append(int(y))

    for i in list1:
        sum += i*list2.count(i)
        
        
print(sum)
