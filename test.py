#1.
#도형 넓이 구하기
from pickle import APPEND
from typing_extensions import Self


class shape object:
    def __int__ (self, width, height):
#사각형 넓이 구하기
    def squre:
        self, width() * self, height()
#삼각형 넓이 구하기
    def triangle:
        self, width() * self, height()       
#원 넓이 구하기
    def circle:
        self, width() * self, width()/4*math.pi        

#2.
# 계산기 만들기
global_number = 0
class calculator:
    #더하기
    def add(self. inp):
        global global_number    
        global_number = global_number + inp
    #빼기
    def sub(self. inp):
        global global_number
        global_number = global_number - inp
    #곱하기
    def mul(self. inp):
        global global_number
        global_number = global_number * inp
    #나누기
    def div(self. inp):
        global global_number
        global_number = global_number / inp 
    #에러발생
    try:        
        (0/global_number)   
    except ZeroDivisionError:
        print(f'0으로 나눌 수 없습니다.')
    try:
        global_number != int
    except ValueError:
        print(f'숫자만 입력 가능합니다')                   

#3
#프로필 관리 기능 만들어보기
class profile()
#각각의 출력값 메소드 설정하기
def set_profile(self, profile):
    self.profile = profile
profile = profile()    
print(profile.get_name(self):
    return self.profile["name"] # 이름 출력
print(profile.get_gender(self):
    return self.profile["gender"] # 성별 출력
print(profile.get_birthday(Self):
    return self.profile["birthday"] # 생일 출력
print(profile.get_age(self):    
    return self.profile["age"] # 나이 출력
print(profile.get_phone(self):
    return self.profile["phon"] # 핸드폰번호 출력
print(profile.email(self):
    return self.profile["email"] # 이메일 출력

#4.
#리스트축약식
people = [
    ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
    ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
    ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
    ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
    ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
    ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
    ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
    ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
    ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
    ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
    ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
    ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
    ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
    ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
    ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
]

#제공 된 사용자들 중 나이가 20살 미만인 사람들은 제외해주세요
under_age = [20<[2] for x in pelple]
print(under_age)
#사용자들을 나이 순으로 정렬해주세요
people = {age: {}{for name, nationality, age, email in people}
print(people)

"""
[('Winnie Hall', 'Palestinian )Territories', 22, 'moci@pacivhe.net'),
 ('Brent Peterson', 'Svalbard & Jan Mayen', 22, 'le@wekciga.lr'),
 ('Eric Townsend', 'Svalbard & Jan Mayen', 22, 'jijer@cipzo.gp'),
 ('Inez Little', 'Namibia', 26, 'meewi@mirha.ye'),
 ('Carrie Palmer', 'Mauritius', 28, 'fenlofi@tor.aq'),
 ('Alfred Schwartz', 'Syria', 29, 'ic@tolseuc.pr'),
 ('Katharine Little', 'Anguilla', 29, 'am@kifez.et'),
 ('Peter Bowen', 'Burundi', 30, 'vinaf@rilkov.il'),
 ('Erik Lane', 'Turkey', 30, 'efumazza@va.hn')]
"""
        