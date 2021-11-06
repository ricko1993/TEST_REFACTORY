def cek_palindrome(string):
    length = len(string)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
            if(string[first]==string[last]):
                first=first+1
                last=last-1
            else:
                status = 0
                break
    return int(status)  
string = input("Masukan teks: ")
status= cek_palindrome(string)
if(status):
    print("palindrome ")
else:
    print("Bukan palindrome")