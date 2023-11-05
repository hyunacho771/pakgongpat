section .data
    newline db 10
    format db "%d x %d = %d", 10, 0

section .bss
    i resb 1
    j resb 1

section .text
    global main

main:
    mov ecx, 2  ; 시작 단 (2단)

outer_loop:
    cmp ecx, 10  ; 끝 단 (9단 + 1)
    jg exit

    mov byte [i], cl  ; i 초기화

inner_loop:
    mov byte [j], 1  ; j 초기화

    ; i * j 계산
    movzx eax, byte [i]  ; i를 32비트 레지스터로 확장
    movzx ebx, byte [j]  ; j를 32비트 레지스터로 확장
    imul eax, ebx  ; 결과 계산 (i * j)

    ; 결과를 스택에 푸시하여 printf에 전달
    push eax
    push ebx
    push ecx
    push format
    call printf
    add esp, 16

    inc byte [j]  ; j 증가
    cmp byte [j], 10  ; 곱할 숫자가 10 이상이면 종료
    jl inner_loop

    ; 줄바꿈 출력
    mov eax, 4
    mov ebx, 1
    mov ecx, newline
    mov edx, 1
    int 0x80

    inc byte [i]  ; i 증가
    jmp outer_loop

exit:
    ; 종료 시스템 호출
    mov eax, 1
    int 0x80

section .data
    extern printf