driving = input('請問您有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit #出發系統離開
	
age = int (input('請問您的年齡？') ) 
if driving == '有':
	if age >= 18:
		print('您通過測驗了')
	else:
		print('奇怪，你怎麼開過車？')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照啦，怎麼不去考')
	else:
		print('很好，再過幾年就可以考駕照了')
else:
	print('只能輸入有/沒有')