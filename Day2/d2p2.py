def read_from_file(filename):
  try:
    with open(filename, 'r') as file:
      data = file.readlines()
    return data
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    return None

def isSafe(report):
    #report = [int(i) for i in line.split()]
    
    if sorted(report) != report and sorted(report, reverse=True) != report:
        return False
        
    for j in range(1,len(report)):
        if abs(report[j]-report[j-1])>3:
            return False
        if report[j] == report[j-1]:
            return False

    return True

filename = 'Day2/input.txt'  
file_content = read_from_file(filename)  

safe_lines = 0
if file_content:
    for line in file_content:
        report = [int(i) for i in line.split()]
        
        if isSafe(report):
            safe_lines+=1
        
        else:
            safe = False
            for j in range(len(report)):
                tmp = [i for i in report]
                tmp.pop(j)
                if isSafe(tmp):
                    safe = True
            
            if safe:
                safe_lines +=1
            
print(safe_lines)