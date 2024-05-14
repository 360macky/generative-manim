"""
This file houses the various formatting methods of the edoh
note that I can only guarantee that it will work properly on the josnl file of the edoh
---
e.g input:
example_str = "from manim import * class MyScene(Scene): def construct(self): heptagon = RegularPolygon(n=7, radius=3, color=GREEN) self.add(heptagon)"
print(format_edoh(example_str))

e.g output:
>>>from manim import *
class MyScene(Scene):
        def construct(self):
                heptagon = RegularPolygon(n=7, radius=3, color=GREEN)
                self.add(heptagon)

"""

import json

def format_edoh(input_str: str)->str:
    '''
    
    '''
    str_import = input_str[:19]  # "from manim import *"
    str_class = input_str[20:41]  # "class MyScene(Scene):"
    str_def = input_str[42:62]  # "def construct(self):"
    str_content = input_str[63:]  # rest of code

    space_index = [i for i, c in enumerate(str_content) if c == " "]  # find all [space] index
    filtering_index = []
    for index in space_index:
        left_str = str_content[index - 1]
        right_str = str_content[index + 1]

        # If "=" is found on the left or right, then this is an assignment statement
        if left_str == "=" or right_str == "=":continue

        # If "," found on the left or right, then this is some function argument
        if left_str == "," or right_str == ",":continue

        # If "+-*/" found on the left or right, then this is an expression
        if left_str == "*" or right_str == "*":continue
        if left_str == "+" or right_str == "+":continue
        if left_str == "-" or right_str == "-":continue
        if left_str == "/" or right_str == "/":continue
        if left_str == "//" or right_str == "//":continue
        if left_str == "**" or right_str == "**":continue
        if left_str == "%" or right_str == "%":continue

        filtering_index.append(index+1)

    # Add beginning and ending indexes, e.g[0,...,...,...,76]
    filtering_index =[0] + filtering_index + [len(str_content)] 
    filtering_context = ''
    last_index = 0
    # Slice every two indexes and then add formatting symbols
    for index in filtering_index:
        if index == 0 or last_index == len(str_content):
            last_index = index
            continue 
        else:
            #print(last_index,index)
            if filtering_context =='':
                filtering_context = '\t\t'+str_content[last_index:index]
            else:
                filtering_context = filtering_context + '\n\t\t'+str_content[last_index:index]
            last_index = index
       
    # print(str_content, space_index,filtering_index,filtering_context)

    return (str_import+'\n'
            +str_class+'\n'
            +'\t'+str_def+'\n'
            +filtering_context)


if __name__ == "__main__":
    example = "from manim import * class MyScene(Scene): def construct(self): heptagon = RegularPolygon(n=7, radius=3, color=GREEN) self.add(heptagon)"

    with open(r'D:\GitHub\generative-manim\datasets\edoh-dataset.jsonl') as file:
        file = file.readlines()
        for data_line in file:
            decode = json.loads(data_line)
            print(decode['messages'][0])
            decode['messages'][2]['content'] = format_edoh(decode['messages'][2]['content'])

            with open(r'D:\GitHub\generative-manim\datasets\edoh-dataset-format.jsonl','a') as outfile:
                outfile.writelines(json.dumps(decode)+'\n')


    
