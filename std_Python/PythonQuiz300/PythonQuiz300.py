
def Quiz001():
    print('''
    001 print 기초
    화면에 Hello World 문자열을 출력하세요.
    ''')
    
    print("\n정답 : ")
    print("Hello World")
    print("\n")    

def Quiz002():
    print('''
    002 print 기초
    화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)    
    ''')
    
    print("\n정답 : ")
    print("Mary's cosmetics")
    print("\n")    

def Quiz003():
    print('''
    003 print 기초
    화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)

    신씨가 소리질렀다. "도둑이야".  ''')
      
    print("\n정답 : ")
    print('신씨가 소리질렀다. "도둑이야".')
    print("\n")    


def Quiz004():
    print('''
    004 print 기초
    화면에 "C:\Windows"를 출력하세요.
    ''')

    print("\n정답 : ")
    print('"c:\Windows"')
    print("\n")    


    
def Quiz005():
    print('''
    005 print 탭과 줄바꿈
    다음 코드를 실행해보고 \\t와 \\n의 역할을 설명해보세요.

    print("안녕하세요.\\n만나서\\t\\t반갑습니다.")
    ''')

    print("\n정답 :")

    print("\\n : 한줄 띄우기")
    print("\\t : 탭 간격 띄우기 ( 4칸 )")
    print("\n")    



def Quiz006():
    print('''
    006 print 여러 데이터 출력
    print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.

    print ("오늘은", "일요일")
    ''')
    
    print("\n정답 : ")
    print("print 문 내에서 , 는 한칸 띄워주는 역할을 하므로 '오늘은' 다음에 한칸 띄운 후 '일요일'이 출력 된다")
    print("오늘은", "일요일")
    print("\n")    

def Quiz007():
    print('''
    007 print 기초
    print() 함수를 사용하여 다음과 같이 출력하세요.

    naver;kakao;sk;samsung
    ''')
    
    print("\n정답 : ")
    print("naver","kakao","sk","samsung", sep=";")
    print("\n")

def Quiz008():
    print('''
    008 print 기초
    print() 함수를 사용하여 다음과 같이 출력하세요.

    naver/kakao/sk/samsung
    ''')
    
    print("\n정답 : ")
    print("naver","kakao","sk","samsung", sep="/")
    print("\n")

def Quiz009():
    print('''
    009 print 줄바꿈
    다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.

    print("first");print("second")
    ''')

    print("\n정답 : ")
    print("first", end="");print("second")

def Quiz010():
    print('''
    010 연산 결과 출력
    5/3의 결과를 화면에 출력하세요.
    ''')

    print("\n정답 : ")
    print(5/3)

def Quiz011():
    print('''
    011 변수 사용하기
    삼성전자라는 변수로 50,000원을 바인딩해보세요.
    삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
    ''')
    
    samsungelec = 50000
    Result = samsungelec * 10
    print("삼성전자 총 평가 금액 : {0} 원".format(Result))
    
def Quiz012():
    print('''
    012 변수 사용하기
    다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.

    항목	    값
    시가총액	298조
    현재가	    50,000원
    PER	        15.79
    ''')

    result = 298
    current = 50000
    per = 15.79


Quizprint = Quiz011()