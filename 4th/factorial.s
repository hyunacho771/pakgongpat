section .data
    format db "Factorial of %d is %d", 10, 0  ;출력 포맷
    extern printf

section .text
    global main

main:
		;함수 호출 준비
    push 5  ; 목표 변수 세팅
    call factorial
    ;출력
    mov eax, ebx
    push eax
    push 5
    push format
    call printf
    add esp, 12  ; 스택 정리
    mov eax, 1 
    xor ebx, ebx  
    int 0x80

factorial:
    push ebp
    mov ebp, esp
    sub esp, 4
    
		;팩토리얼 계산
    mov eax, [ebp + 8]  ;n 생성
    cmp eax, 1
    jbe .base_case
    
    dec eax  ; n 감소
    push eax  ; n - 1 푸쉬
    call factorial  ; 재귀함수 부르기
    pop eax 
    
    ; 곱하기
    imul eax, ebx
    
.base_case:
    ; 탈출 케이스
    mov ebx, eax  ; ebx에 결과 저장
    
    leave
    ret