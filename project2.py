filename =input("input the filename:")
x= filename.split(".")
f=x[-1]
print(f)

file_ext= {
          "py":"python",
          "cpp":"c++",
          "jsp":"java", 
          "htm":"html"}

x= file_ext.get(f)
print("the extension of the file is:",x)
  
