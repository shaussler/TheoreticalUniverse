" Set custom fold markers
set foldmethod=marker
set foldmarker={{{,}}}

" Enable syntax highlighting
syntax on

" Set color scheme to 'desert'
colorscheme desert

" Set textwidth to 100 characters
set textwidth=80

" Tab settings
set tabstop=2
set softtabstop=0
set shiftwidth=2
set expandtab

" Set Android system clipboard
set clipboard+=unnamedplus

" Line numbering
set number

" Mouse support
set mouse=a

" Backspace behavior
set backspace=2

" Encoding
set encoding=utf-8

" Color column
if has("nvim")
  set colorcolumn=4,81,121
  highlight ColorColumn guibg=green
  highlight ColorColumn ctermbg=235 guibg=#2c2d27
  highlight ColorColumn ctermbg=237
endif

" Shortcuts to UTF-8 characters
imap \alpha   α
imap \beta    β
imap \gamma   γ
imap \delta   δ
imap \epsilon ε
imap \zeta    ζ
imap \eta     η
imap \theta   θ
imap \iota    ι
imap \kappa   κ
imap \lamda   λ
imap \mu      μ
imap \nu      ν
imap \xi      ξ
imap \omicron ο
imap \pi      π
imap \rho     ρ
imap \sigma   σ
imap \tau     τ
imap \upsilon υ
imap \phi     φ
imap \chi     χ
imap \psi     ψ
imap \omega   ω
imap \Lambda  Λ
imap \nabla   ∇
imap \partial ∂
imap \star    ⋆
imap \wedge   ∧
imap \vee     ∨
imap \otimes  ⊗
imap \times   ⨯
imap \flat    ♭
imap \sharp   ♯
imap \rightarrow →
