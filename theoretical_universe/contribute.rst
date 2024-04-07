Contribute
==========

neovim configuration
--------------------

.. code:: vim

   " Fold marker method and fold markers
   set foldmethod=marker
   set foldmarker={{{,}}}
   
   " Tab settings
   set tabstop=2
   set softtabstop=0
   set shiftwidth=2
   set expandtab
   
   " Encoding
   set encoding=utf-8
   
   " Greyed out columns at 81 and 121
   if has("nvim")
     set colorcolumn=81,121
     highlight ColorColumn guibg=green
     highlight ColorColumn ctermbg=235 guibg=#2c2d27
     highlight ColorColumn ctermbg=237
   endif
   
   " Special characters
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
   imap \nabla   ∇
   imap \partial ∂
   imap \star    ⋆
   imap \wedge   ∧
   imap \otimes  ⊗
   imap \times   ⨯
   imap \flat    ♭
   imap \sharp   ♯
