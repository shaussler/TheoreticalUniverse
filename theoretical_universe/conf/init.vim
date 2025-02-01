
" Set color scheme to 'desert'
" ----------------------------
colorscheme desert

" Set textwidth to 100 characters
" -------------------------------

" set textwidth=100

" Tab settings
" ------------

set tabstop=2
set softtabstop=0
set shiftwidth=2
set expandtab

" Set Android system clipboard
set clipboard+=unnamedplus

" Line numbering
set number

" Show white spaces
set list

" Mouse support
set mouse=a

" Backspace behavior
set backspace=2

" Encoding
set encoding=utf-8

" Color column
set colorcolumn=4,81,101,121
highlight ColorColumn guibg=green
highlight ColorColumn ctermbg=235 guibg=#2c2d27
highlight ColorColumn ctermbg=237

" Use vim-plug as the plugin manager
" ----------------------------------

" call plug#begin('~/.vim/plugged')
" 
" " Add the reStructuredText syntax highlighting plugin
" " ---------------------------------------------------
" 
" Plug 'marshallward/vim-restructuredtext'
" Plug 'habamax/vim-rst'
" 
" " Linting with ALE
" Plug 'dense-analysis/ale'
" 
" call plug#end()
" 
" let g:ale_linters = {'python': ['flake8']}
" let g:ale_fixers = {'python': ['autopep8']}
" let g:ale_python_flake8_executable = 'flake8'
" let g:ale_fix_on_save = 1

" Set custom fold markers
" -----------------------

set foldmethod=marker
set foldmarker={{{,}}}

" Enable filetype plugins and indentation
" ---------------------------------------

filetype plugin indent on

" Enable syntax highlighting
" --------------------------

syntax on

" Auto-apply filetype and syntax highlighting for .rst files
" ----------------------------------------------------------

" autocmd BufRead,BufNewFile *.rst set filetype=rst

" Shortcuts to UTF-8 characters
" -----------------------------

imap \alpha     α
imap \beta      β
imap \gamma     γ
imap \delta     δ
imap \epsilon   ε
imap \zeta      ζ
imap \eta       η
imap \theta     θ
imap \iota      ι
imap \kappa     κ
imap \lambda    λ
imap \mu        μ
imap \nu        ν
imap \xi        ξ
imap \omicron   ο
imap \pi        π
imap \rho       ρ
imap \sigma     σ
imap \tau       τ
imap \upsilon   υ
imap \phi       φ
imap \chi       χ
imap \psi       ψ
imap \omega     ω
imap \Pi        Π
imap \Delta     Δ
imap \Lambda    Λ
imap \nabla     ∇
imap \laplacian ∆
imap \partial   ∂
imap \star      ⋆
imap \wedge     ∧
imap \vee       ∨
imap \otimes    ⊗
imap \times     ⨯
imap \flat      ♭
imap \sharp     ♯
imap \rightarrow →
