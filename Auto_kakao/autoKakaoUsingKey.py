import pyautogui as pag
import time, subprocess, os, pyperclip



def initialize():
    print("프로그램 시작! ")
    print("Kakaotalk 화면 가져오기!")
    filter_name = input("필터링 할 이름 : ")
    msg = input("전송할 메세지 : ")
    repeat = input("반복 횟수 : ")
    init_number = input("처음위치 : ")
    print("====================")
    print("메세지 전송 시작!")
    print("====================")
    openKakao()
    return (filter_name, msg, repeat, init_number)

def openKakao():
    #애플스크립트 이용
    print("카카오 화면 실행!")
    Kakaotalk = """
    tell application "KakaoTalk"
      activate
    end tell
    """
    Kakaotalk = Kakaotalk.encode()
    p = subprocess.Popen('osascript', stdin=subprocess.PIPE, stdout=subprocess.PIPE, 
    stderr=subprocess.STDOUT)
    p.communicate(Kakaotalk)[0]
    time.sleep(2)


def filter_friend(filter_name):
    time.sleep(1)
    #필터링할 이름 복사
    if filter_name == '':
        pag.keyDown('esc')
    else :
        # filter_name = 305
        pyperclip.copy(filter_name)
    print("붙여넣기할 이름 : {}".format(filter_name))

    #이미지 검색
    try :
        print("토크 단축키 준비!") 
        pag.hotkey('command', '2')
        time.sleep(1)
        print("토크 단축키 실행!") 
    except Exception as e:
        print('error : ', e)

    time.sleep(1)
    print("이름 검색")
    pag.hotkey('command','f')
    time.sleep(1)
    pag.hotkey('command','v')
    time.sleep(1)

def send_msg(msg, repeat):
    pyperclip.copy(msg)
    for i in range(int(repeat)):
        print('repeat number : ',i+1)
        pag.keyDown('enter')
        pag.hotkey('command','v')
        time.sleep(1)   
        # pag.keyDown('enter')
        pag.keyDown('esc')
        pag.keyDown('down')

def set_position(init_number):
    for i in range(int(init_number)):
        pag.keyDown('down')

if __name__ == "__main__":
    (filter_name, msg, repeat, init_number) = initialize()
    filter_friend(filter_name)
    set_position(init_number)
    send_msg(msg, repeat)

