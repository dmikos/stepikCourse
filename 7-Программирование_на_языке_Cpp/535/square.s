	.file	"square.cpp"
	.text
	.globl	_Z6squarei
	.type	_Z6squarei, @function
_Z6squarei:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, -4(%rbp)
	movl	-4(%rbp), %eax
	imull	-4(%rbp), %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	_Z6squarei, .-_Z6squarei
	.ident	"GCC: (Debian 6.2.0-10) 6.2.0 20161027"
	.section	.note.GNU-stack,"",@progbits
