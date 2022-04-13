class student():
    def __init__(self, name, math_score, language_score):
        self.name = name
        self.math_score = math_score
        self.language_score = language_score
    
    ## repr 函数用于定义对象被输出时的输出结果
    def __repr__(self):
        return str((self.name, self.math_score, self.language_score))
    
    def change_score(self, course_name, score):
        if course_name == 'math':
            self.math_score = score
        elif course_name == 'language':
            self.language_score = score
        else:
            print(course_name, 'course is still not in current system')
            
    def print_name(self, ):
        print(self.name)
    
    name = 'Undefined'
    math_score = -1
    language_score = -1