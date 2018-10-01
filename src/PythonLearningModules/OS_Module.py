import os

#List all available inbuild options
#print(dir(os))

#Get the current working directory
print(os.getcwd())
#os.chdir('E:\Python\Eclips_python_workspace\MyFisrtProject\src')

#print(os.listdir('E:\Python'))

os.chdir('E:\Python\practice')
#os.mkdir('test3')
print(os.listdir('E:\Python\practice'))
os.rmdir('test3')
print(os.listdir('E:\Python\practice'))