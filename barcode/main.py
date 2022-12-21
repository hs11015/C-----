#!/usr/bin/env python3

import function


print("가계부 프로그램에 오신 것을 환영합니다!")
print("\n====================\n")
print(" 로그인 을 원하시면 \"1\" 혹은  \"로그인\" 을\n회원가입을 원하시면 \"2\" 혹은 \"회원가입\"을 입력해주세요.\n")

### 로그인 ###

start, account = "", ""
while (start != "로그인" and start != "1" and start != "회원가입" and start !='2'):
	start = input("로그인(1)/회원가입(2): ")

print()

while (account == ""):
	account = input("사용자명을 입력하세요: ")

if (start == "로그인" or start == "1"):
	function.MEMBER, function.index = function.login(account)

	if (function.MEMBER == False):
		function.ACCOUNTLIST.append(account)
		function.CATEGORY, function.PRICE, function.DATE, function.ITEM = [],[],[],[]
	else:
	 	function.CATEGORY, function.PRICE, function.DATE, function.ITEM = function.load_list(function.index)

elif (start == "회원가입" or start =='2'):
	function.ACCOUNTLIST.append(account)
	function.MEMBER, function.index = function.signin(account)
	function.CATEGORY, function.PRICE, function.DATE, function.ITEM = [],[],[],[]

print()
### 기능 구현 시작 ###
menu = 0
while (menu != '3'):
	print("----------\n| 메뉴판 |\n----------")
	print("1) 가계부 보기\n2) 항목 추가하기\n3) 가계부  종료")
	menu = input("메뉴를 입력하세요: ")

	### 가계부 보기 ###
	if menu == '1':
		function.printing(function.CATEGORY, function.PRICE, function.DATE, function.ITEM)

	### 항목 추가하기 ###
	elif menu == '2':
		category, price, date, item = function.add_expanse()
		function.CATEGORY.append(category)
		function.PRICE.append(price)
		function.DATE.append(date)
		function.ITEM.append(item)

		function.CATEGORY, function.PRICE, function.DATE, function.ITEM = function.sortingList(function.CATEGORY, function.PRICE, function.DATE, function.ITEM)
		function.printing(function.CATEGORY ,function.PRICE, function.DATE, function.ITEM)

	### 가계부 종료 ###
	elif menu == '3':
		function.ACCOUNTBOOK.append({'category':function.CATEGORY, 'price':function.PRICE, 'date':function.DATE, 'item':function.ITEM})
		function.ACCOUNTLIST, function.ACCOUNTBOOK = function.save(function.CATEGORY, function.PRICE, function.DATE, function.ITEM)	
		function.end(function.ACCOUNTLIST, function.ACCOUNTBOOK)

	### 예외처리 ###
	else:
		print("1, 2, 3을 입력해주세요.")


