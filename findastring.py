def count_substring(string, sub_string):
    k = len(sub_string)
    ans = 0
    for i in range(len(string)):
        if i+k > len(string):
            break
        if sub_string == string[i:i+k]:
            ans += 1
    return ans

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

