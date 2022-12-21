#!/usr/bin/env python3

import pandas as pd
import copy

#일단 변수 호출
ACCOUNTLIST = []
ACCOUNTBOOK = []
CATEGORY = []
PRICE = []
DATE = []
ITEM = []
MEMBER = False
index = 0


########
# 함수 #
########



#선택정렬 함수
def selection_sort(unsorted):
	sort = []
	for i in range(len(unsorted)):
		smallest = find_smallest(unsorted)
		sort.append(unsorted.pop(smallest))
	
	return sort


def find_smallest(unsorted):
	smallest_index = 0
	smallest_value = unsorted[0]
	for i in range(1, len(unsorted)):
		if smallest_value > unsorted[i]:
			smallest_value = unsorted[i]
			smallest_index = i

	return smallest_index



#이진탐색 함수
def binary_search(LIST, item):
	left = 0
	right = len(LIST)-1

	while right >= left:
		mid = (right + left) // 2
		
		if LIST[mid] == item:
			return mid
		elif LIST[mid] < item:
			left = mid + 1
		else: # LIST[mid] > item:
			right = mid - 1
	
	return None


#데이터 불러오기
def load_data():
	database = "./database.txt"
	linenum = 0
	for line in open(database):
		if linenum == 0:
			ACCOUNTLIST = line[:-1].split(',')
			linenum += 1
		elif linenum == 1:
			ACCOUNTBOOK = line.split('/')
			for i in range(len(ACCOUNTBOOK)):
				ACCOUNTBOOK[i] = eval(ACCOUNTBOOK[i])
			linenum += 1
	
	if linenum != 2:
		ACCOUNTLIST = []
		ACCOUNTBOOK = []

	return ACCOUNTLIST, ACCOUNTBOOK



#로그인 기능
def login(account):

	index = 0
	if len(ACCOUNTLIST) == 0:
		print("해당 사용자는 존재하지 않습니다.\n회원가입 창으로 넘어가겠습니다.")
		MEMBER, index = signin(account)
	else:
		index = binary_search(ACCOUNTLIST, account)
		if (index!=None): #False가 아닌 값  반환시 LIST에 account 존재
			print("로그인에 성공하셨습니다.")
			MEMBER = True
		else:
			print("해당 사용자는 존재하지 않습니다.\n회원가입 창으로 넘어가겠습니다.")
			MEMBER, index =  signin(account)

	return MEMBER, int(index)


#회원가입 기능
def signin(account):
	
	index = 0
	if len(ACCOUNTLIST) == 0:
		print("회원가입 완료했습니다. 바로 로그인 후 가계부로 넘어가겠습니다.")
		MEMBER = False
	
	elif len(ACCOUNTLIST) == 1:
		ACCOUNTLIST[0] == account
		print("이미 존재하는 사용자입니다.\n바로 로그인 후 가계부로 넘어가겠습니다.")
		MEMBER = True
	
	else:
		index = binary_search(ACCOUNTLIST, account)
		if (index != None):
			print("이미 존재하는 사용자입니다.\n바로 로그인 후 가계부로 넘어가겠습니다.")
			MEMBER = True
		else:
			index = len(ACCOUNTLIST)-1
			print("회원가입 완료했습니다. 바로 로그인 후 가계부로 넘어가겠습니다.")
			MEMBER = False

	return MEMBER, int(index)


#데이터 불러오기
def load_list(index):
	CATEGORY = ACCOUNTBOOK[index]['category']
	PRICE = ACCOUNTBOOK[index]['price']
	DATE = ACCOUNTBOOK[index]['date']
	ITEM = ACCOUNTBOOK[index]['item']
	
	return CATEGORY, PRICE, DATE, ITEM

#데이터 추가하기
def add_expanse():
	print("\n내역 정보를 입력해주세요!")
	InOut = ""
	while (InOut!="지출" and InOut!="수입"):
		InOut = input("지출인가요?  수입인가요? (지출/수입): ")

	category = input("카테고리를 입력해주세요: ")
	
	price = input("금액을 입력해주세요: ")
	if (InOut == "지출"):
		price = "-"+price
	else :
		price = "+"+price

	date = input("날짜를 입력해주세요: ")
	item = input("상품을 입력해주세요: ")
	
	return category, price, date, item



#데이터 보여주기 (dataframe)
def printing(CATEGORY, PRICE, DATE, ITEM):
	if (len(CATEGORY)==0):
		print("\n아직 가계부 내역이 없습니다.\n")
	else:
		print()
		temp_accountbook = {'category':CATEGORY, 'price':PRICE , 'date':DATE, 'item':ITEM}
		accountbook = pd.DataFrame(temp_accountbook, index=[i for i in range(1, len(CATEGORY)+1)], columns=['category','price','date','item'])
		print(ACCOUNTLIST[index]+"\'s 가계부")
		print(accountbook)
		print()


#지금까지 내역 저장하기
def sortingList(CATEGORY, PRICE, DATE, ITEM):
	if (len(CATEGORY) > 1):
		TEMP_CATEGORY = copy.deepcopy(CATEGORY)
		NEW_CATEGORY = selection_sort(TEMP_CATEGORY)
		NEW_PRICE, NEW_DATE, NEW_ITEM = [],[],[]
		if (CATEGORY != NEW_CATEGORY):
			for i in range(len(NEW_CATEGORY)-1):
				if (NEW_CATEGORY[i] == CATEGORY[len(CATEGORY)-1]):
					NEW_PRICE.append(PRICE[len(PRICE)-1])
					NEW_DATE.append(DATE[len(DATE)-1])
					NEW_ITEM.append(ITEM[len(ITEM)-1])
				NEW_PRICE.append(PRICE[i])
				NEW_DATE.append(DATE[i])
				NEW_ITEM.append(ITEM[i])
	else:
		NEW_CATEGORY = CATEGORY
		NEW_PRICE = PRICE
		NEW_DATE = DATE
		NEW_ITEM = ITEM
	return NEW_CATEGORY, NEW_PRICE, NEW_DATE, NEW_ITEM


#파일로 저장하기
def save(CATEGORY, PRICE, DATE, ITEM):
	if (len(ACCOUNTLIST) >= 1):
		TEMP_ACCOUNTLIST = copy.deepcopy(ACCOUNTLIST)
		NEW_ACCOUNTLIST = selection_sort(TEMP_ACCOUNTLIST)
		NEW_ACCOUNTBOOK = []
		if (ACCOUNTLIST != NEW_ACCOUNTLIST):
			for i in range(len(NEW_ACCOUNTLIST)-1):
				if (NEW_ACCOUNTLIST[i] == ACCOUNTLIST[len(ACCOUNTLIST)-1]):		
					NEW_ACCOUNTBOOK.append(ACCOUNTBOOK[len(ACCOUNTBOOK)-1])
				NEW_ACCOUNTBOOK.append(ACCOUNTBOOK[i])
		else:
			NEW_ACCOUNTBOOK = ACCOUNTBOOK

	else:
		NEW_ACCOUNTLIST = ACCOUNTLIST
		NEW_ACCOUNTBOOK = ACCOUNTBOOK

	return NEW_ACCOUNTLIST, NEW_ACCOUNTBOOK


#프로그램 종료하기
def end(ACCOUNTLIST, ACCOUNTBOOK):
	database = open("./database.txt", "w")
	name = iter(str(ACCOUNTLIST))
	while True:
		temp = next(name, None)
		if temp != None:
			if temp == '\'' or temp == '[' or temp == ']' or temp == '\"':
				continue
			else:
				database.write(temp)
		else:
			database.write("\n")
			break
	
	book = iter(str(ACCOUNTBOOK)[1:-1])
	while True:
		temp = next(book, None)
		if temp != None:
			if temp == '}':
				database.write(temp)
				temp = next(book,None)
				if temp == ',':
					database.write("/")
				elif temp == ']':
					database.write(temp)
			else:
				database.write(temp)
		else:
			break
	
	database.close()
	print("가계부 프로그램을 종료하겠습니다.")


#여기서도 초기화 한 번 해줘야함
ACCOUNTLIST, ACCOUNTBOOK = load_data()

