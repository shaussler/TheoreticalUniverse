Contribute
==========

neovim configuration
--------------------

I use the following configuration.

.. code:: bash

   " Set fold marker method and fold markers
   set foldmethod=marker
   set foldmarker={{{,}}}
   
   " Set tab settings
   set tabstop=2
   set softtabstop=0
   set shiftwidth=2
   set expandtab
   
   " Set encoding
   set encoding=utf-8
   
   " Set one column at 81 and 121
   if has("nvim")
     set colorcolumn=81,121
     highlight ColorColumn guibg=green
     highlight ColorColumn ctermbg=235 guibg=#2c2d27
     highlight ColorColumn ctermbg=237
   endif
   
   " Set spetial characters
   imap \alpha   α
   imap \beta    β
   imap \gamma   γ
   imap \eta     η
   imap \rho     ρ
   imap \epsilon ε
   imap \mu      μ
   imap \nu      ν
   imap \delta   δ
   imap \nabla   ∇
   imap \partial ∂
   imap \star    ⋆
   imap \wedge   ∧
   imap \otimes  ⊗
   imap \times   ⨯
   imap \flat    ♭
   imap \sharp   ♯
   imap \etilde  Ẽ
