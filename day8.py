


from typing import List


class Display():

    def __init__(self, numbers: List[str], output: List[str]) -> None:
        self.numbers = numbers
        self.output = output
        self.dict_numbers = dict()
        self.dict_values = dict()
        self.decoded_output = []

        self._order_numbers()
        self._decode_ez_numbers()
        self._decode_len6_numbers()
        self._decode_len5_numbers()
        self._decode_output()

    def _order_numbers(self):
        self.numbers[:] = [''.join(sorted(number)) for number in self.numbers]
        self.output[:] = [''.join(sorted(number)) for number in self.output]

    def _decode_ez_numbers(self):
        for number in self.numbers:
            if len(number)==2:
                self.dict_numbers[number] = 1
                self.dict_values['1'] = number
            elif len(number)==4:
                self.dict_numbers[number] = 4
                self.dict_values['4'] = number
            elif len(number)==3:
                self.dict_numbers[number] = 7
                self.dict_values['7'] = number
            elif len(number)==7:
                self.dict_numbers[number] = 8
                self.dict_values['8'] = number

    def _decode_len6_numbers(self):
        for number in self.numbers:
            if len(number) == 6:
                if 0 in [c in number for c in self.dict_values['1']]:
                    self.dict_numbers[number] = 6
                    self.dict_values['6'] = number
                elif 0 in [c in number for c in self.dict_values['4']]:
                    self.dict_numbers[number] = 0
                    self.dict_values['0'] = number
                else:
                    self.dict_numbers[number] = 9
                    self.dict_values['9'] = number

    def _decode_len5_numbers(self):
        for number in self.numbers:
            if len(number) == 5:
                if 0 not in [c in self.dict_values['6'] for c in number]:
                    self.dict_numbers[number] = 5
                    self.dict_values['5'] = number
                elif 0 not in [c in self.dict_values['9'] for c in number]:
                    self.dict_numbers[number] = 3
                    self.dict_values['3'] = number
                else:
                    self.dict_numbers[number] = 2
                    self.dict_values['2'] = number

    def _decode_output(self):
        for number in self.output:
            if number in self.dict_numbers:
                self.decoded_output.append(self.dict_numbers[number])      
            else:
                self.decoded_output.append(None)








archivo = './Inputs/example8.txt'
archivo = './Inputs/input8.txt'

with open(archivo) as data:
    displays = [line.split('|') for line in data]


numbers = [line[0].split() for line in displays]
outputs = [line[1].split() for line in displays]

displays[:] = [Display(number, output) for number, output in zip(numbers, outputs)]

decoded_output = [disp.decoded_output for disp in displays]

count_1478 = sum( [sum(output.count(number) for output in decoded_output) for number in [1,4,7,8]])

numbers = [number[0]*1000+number[1]*100+number[2]*10+number[3] for number in decoded_output]

print(sum(numbers))