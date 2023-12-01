def find_next_prime(prime_need, prime_fined):
    check_num = prime_fined[len(prime_fined) - 1] + 2
    while len(prime_fined) < prime_need:
        prime_num = 0
        while prime_num <= len(prime_fined):
            prime_num = prime_num + 1
            prime = prime_fined[prime_num]
            if prime >> len(prime_fined):
                print("Something wrong")
                break
            if check_num % prime != 0:
                print('check :', check_num, 'by', prime)  # print for see which number are check
                if prime == prime_fined[len(prime_fined) - 1]:
                    prime_fined.append(check_num)
                    print(check_num, 'is new prime | out of checker')  # print when find new prime when lower prime
                    # can't divide
                    break
                elif prime ** 2 > check_num:
                    prime_fined.append(check_num)
                    print(check_num, 'is new prime |', prime, '^2 is', (prime ** 2), 'that over', check_num)  # print
                    # when minimum product from the largest prime , it will be new prime
                    break
            else:
                print(check_num, 'isn\'t prime number | it can divided by', prime, 'to', (check_num // prime))  #
                # that number can divide by other number , it will isn't prime number
                break
        if len(prime_fined) >= prime_need:
            break
        check_num += 2
    print('Now have prime are :', prime_fined)  # print all fond prime
    return prime_fined


def find_prime_factors(target_num, prime_list):
    check_by_prime = 0
    left_num = target_num
    member_list = []
    test_result = 1
    while test_result < target_num:
#        print('check', prime_list[check_by_prime], 'from', left_num)  # print for see which number are check
        if left_num % prime_list[check_by_prime] != 0:
#            print('don\'t have [', prime_list[check_by_prime], '] in member')  # that number can't divide target number
            if prime_list[check_by_prime] ** 2 > left_num:
                print('left number [', left_num, '] is prime number because', prime_list[check_by_prime], '^2 is',
                      ((prime_list[check_by_prime]) ** 2), 'it\'s over', left_num)  # print when minimum product from
                # the largest prime , it will be prime number but not record to prime_list
                member_list.append(left_num)
            else:
                check_by_prime += 1
                if check_by_prime == len(prime_list):
                    next_prime_require = len(prime_list) + 1
#                    print('find prime no.', next_prime_require)  # find new prime
                    prime_list = find_next_prime(next_prime_require, prime_list)
        else:
            member_list.append(prime_list[check_by_prime])
            print('have [', prime_list[check_by_prime], '] in member')  # fond prime factor
            left_num = left_num // prime_list[check_by_prime]
        test_result = 1
        for member in member_list:
            test_result *= member
#        print('now member are', member_list, '| result is :', test_result)  # print prime factors member and product
        # from member_list
    return member_list


list_prime = [2, 3]
while True:
    print('Which program is you want to use or end this program? \n [1] Find prime numbers from required quantity \n'
          ' [2] Show fined prime numbers list  \n [3] Find the prime factors of number \n [4] End this program')
    selected = input('What\'s your ans :')
    if selected == '1':
        want_prime = int(input('How many prime number are you want? :'))
        show_prime = []
        if len(list_prime) < want_prime:
            list_prime = find_next_prime(want_prime, list_prime)
        show_prime = list_prime[:want_prime]
        print('first', want_prime, 'prime numbers is :', show_prime)
        continue
    elif selected == '2':
        print('Now have', len(list_prime), 'prime number')
        print(list_prime)
        continue
    elif selected == '3':
        the_number = int(input("What 's your number are you want to fine prime factors :"))
        list_member = find_prime_factors(the_number, list_prime)
        member_value = len(list_member)
        print('your number is', the_number)
        if member_value == 1:
            print('that number is prime number')
        else:
            print('that have members are', list_member)
        list_member = []  # clear list for use in next number
    elif selected == '4':
        break
