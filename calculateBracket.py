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
    token = {'type': 'PLUS', 'rank': 10}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS', 'rank': 10}
    return token, index + 1

def readTimes(line, index):
    token = {'type': 'TIMES', 'rank': 20}
    return token, index + 1

def readDivide(line, index):
    token = {'type': 'DIVIDE', 'rank': 20}
    return token, index + 1

def readLeft(line, index):
    token = {'type': 'LEFT', 'rank': 0}
    return token, index + 1

def readRight(line, index):
    token = {'type': 'RIGHT'}
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
        elif line[index] == '(':
            (token, index) = readLeft(line, index) 
        elif line[index] == ')':
            (token, index) = readRight(line, index)          
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def postfix(tokens):    
    index = 0
    queue = []
    stack = []
    
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            queue.append(tokens[index])
        elif tokens[index]['type'] == "LEFT":
            stack.append(tokens[index])
        elif tokens[index]['type'] == "RIGHT":
            while stack != [] and stack[-1]['type'] != "LEFT":
                queue.append(stack.pop())
            stack.pop()
        else:
            while stack !=[] and stack[-1]['rank'] >= tokens[index]['rank']:
                queue.append(stack.pop())
            stack.append(tokens[index])
            
    while stack:          
            queue.append(stack.pop())
            
    return queue       


def evaluate(tokens):
    OP = ("*", "/", "+", "-",)
    FUNC = {"*": lambda x, y: y*x, 
            "/": lambda x, y: y/x,
            "+": lambda x, y: y+x,
            "-": lambda x, y: y-x,}
    
    stack =[]
    
    for item in tokens:
        if item not in OP:
            stack.append(item)
        else:
            x= stack.pop()
            y= stack.pop()
            stack.append(FUNC[item](x,y))
               
    return stack


def test(line, expectedAnswer):
    tokens = tokenize(line)
    postTokens = postfix(tokens)
    print tokens
    actualAnswer = evaluate(postTokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)


# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    test("3.0+4*2-1/5", 10.8)
    print "==== Test finished! ====\n"

runTest()

while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    postTokens = postfix(tokens)
    answer = evaluate(postTokens)
    print "answer = %f\n" % answer