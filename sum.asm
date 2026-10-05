; Сумма двух чисел (x86-64, NASM, Linux)
; Сборка: nasm -f elf64 sum.asm -o sum.o && ld sum.o -o sum
; Запуск:  ./sum; echo $?

section .data
    a dq 5
    b dq 7

section .text
    global _start

_start:
    mov rax, [a]
    add rax, [b]

    mov rdi, rax    ; код завершения = результат
    mov rax, 60     ; sys_exit
    syscall
