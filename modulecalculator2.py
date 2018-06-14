'''
Created on 2018. 6. 12.

@author: jinhee
'''
def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readTimes(line, index):
    token = {'type': 'TIMES'}
    return token, index + 1

def readDivide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readTimes(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)    
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def tokenize2(tokens):
    index = 0;
    while index < len(tokens): 
        if tokens[index]['type'] == 'TIMES':
            tokens[index-1]['number'] *= tokens[index+1]['number']
            del(tokens[index])
            del(tokens[index])
        elif tokens[index]['type'] == 'DIVIDE':
            tokens[index-1]['number'] /= tokens[index+1]['number']*1.0
            del(tokens[index])
            del(tokens[index])
        else: index+=1
            
    return tokens                        


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    tokens2 = tokenize2(tokens)
    actualAnswer = evaluate(tokens2)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)


# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    test("3.0+4*2-1/5", 10.8)
    test("1", 1)
    test("3*4.0*2.1+5-2.1/2", 29.15)
    print "==== Test finished! ====\n"

runTest()

while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokens2 = tokenize2(tokens)
    answer = evaluate(tokens2)
    print "answer = %f\n" % answer