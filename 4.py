#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle(source,result_file):
    with open(source, "r", encoding="utf") as file:
        input_str = file.read()

        result = ''
        last_symbol = ''
        count = 0
        for i in range(0, len(input_str)):
            symbol = input_str[i]
            if symbol == last_symbol:
                count += 1
            else:
                if count != 0:
                    result+=str(count+1)+last_symbol
                    count = 0
                last_symbol = symbol
        if count != 0:
            result+=str(count+1)+last_symbol
            count = 0
    
    with open(result_file, "w", encoding="utf") as file:
        file.write(result)

def rle_(source,result_file):
    with open(source, "r", encoding="utf") as file:
        input_str = file.read()

        result = ''
        count = 1
        for i in range(0, len(input_str)):
            symbol = input_str[i]
            if symbol.isdigit():
                count = int(symbol)
            else:
                for i in range(0,count):
                    result+=symbol
                count = 1
    
    with open(result_file, "w", encoding="utf") as file:
        file.write(result)

rle_('4_input_.txt', "4_output_.txt")