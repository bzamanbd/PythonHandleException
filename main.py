try:
    f= open('myFile.txt','r')
    f.write('hello python') 
    f.close()
except IOError as e: 
    print('some error occurred',e)
finally:
    print("Process is done")
