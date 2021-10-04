module mod
  Implicit None 
  private 
  public::test
  integer::const=100
Contains
  Subroutine test()
    print *,"running test", const
  end Subroutine
end module
