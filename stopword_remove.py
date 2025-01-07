
            
import os     
stopwords = ['the', 'is', 'and', 'to', 'a', 'of', 'in', 'that', 'it', 'on']
input_path=input("Enter the path of the input text file: ") # else '/Users/sami/Documents/edge course/INDIA VS AUS 4th Test.txt'  # Replace path of text file here
output_path=input("Enter the path of the input text file: ") # else '/Users/sami/Documents/edge course'  # Replace the path of output_file
if output_path.endswith('.txt'):
       final_output_path = output_path
else:
       final_output_path=os.path.join(output_path,'cleaned_text.txt')
print(final_output_path)

with open(final_output_path,'w') as p: 
       p.write('')
with open(input_path,'r') as f:
       content=f.read().split('\n') 
       for i in range(len(content)):
              line=content[i].split(' ')
              line.append('\n')
            #   print(line)
              with open(final_output_path,'a') as p: 
                     for j in range(len(line)):
                            match=False
                            for word in stopwords:
                                   if line[j] == word or line[j] == word.capitalize():
                                         match= True

                            if match == False:
                                    if line[j] == '\n':
                                         p.write(line[j]) 
                                    
                                    elif line[j].find('.') != -1 :
                                                if line[j].endswith('.') is not True:
                                                       sub_line=line[j].split('.')
                                                       for k in range(2):
                                                              sub_match=False
                                                              for word in stopwords:
                                                                  if sub_line[k] == word or sub_line[k] == word.capitalize():
                                                                       sub_match= True
                                                              if sub_match == False:
                                                                       if k == 0:
                                                                          p.write(sub_line[0]+'.')
                                                                       else:
                                                                          p.write(sub_line[1]+' ')
                                                
                                                else:
                                                      p.write(line[j]+' ')  
                                               
                                               
                                                
                                    else:
                                          p.write(line[j]+' ')  
                                     




                 