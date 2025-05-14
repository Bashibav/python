#'walrus' (:=) operator allow us to assign values to variable as part of expression

#example
if(n:=len([1,2,3,4,5,6,6,7]))>3: #here n:= len is used inside expression to assign value to n
    print(f"the list has {n} elements, expected<=3")