#!/usr/bin/python3

# iterarte upto n
def pascal_triangle(n) {
if (n <=0){
    return [];
} else{
    //ist = [];
    for i in range(n):
        # adjust space
        print([' '*(n-i)], end='')
        # compute power of 11
	    print([' '.join(map(str, str(11**i)])))
  }
};