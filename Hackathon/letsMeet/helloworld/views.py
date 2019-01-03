from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from event.models import Event, Response


def createEvent(request):
	#error = False
	#urlExist = False
	#if request.method == 'GET':
	if request.GET:
		eventName = request.GET.get('eventName')
		#try:
			#Event.objects.filter(eventName=eventName)
			#error = True
		#except:
		owner = request.GET.get('owner')
		dayChosen = request.GET.get('dayChosen')
		timeChosen = request.GET.get('timeChosen')
		randUrl = '/' + request.GET.get('randUrl') + '/'
		Event.objects.create(eventName=eventName, owner=owner, dayChosen=dayChosen, timeChosen=timeChosen, randUrl=randUrl)
		return redirect(randUrl)
	return render(request, 'week_trydate.html')



def newEvent(request):
	current = request.get_full_path()
	event = Event.objects.get(randUrl=current)
	eventName = event.eventName

	dC = event.dayChosen
	dayChosen = dC.split(",",dC.count(","))
	while "" in dayChosen:
		dayChosen.remove("")
	tC = event.timeChosen
	timeChosen = tC.split(",",tC.count(","))
	while "" in timeChosen:
		timeChosen.remove("")

	error = False # 完成使用者名稱不重複！
	if request.method == 'POST':
		yourName = request.POST.get('yourName')
		try:
			Response.objects.get(yourName=yourName, event=event)
			error = True
		except:
			freeTime = request.POST.get('freeTime')
			Response.objects.create(yourName=yourName, freeTime=freeTime, event=event)
			return redirect(current+'result')
	lastDay = dayChosen[len(dayChosen)-1]

	ifDate = False
	num = "0123456789"
	for i in num:
		if i in dC:
			ifDate = True

	if ifDate == True:
		return render(request, 'user_trydate.html',locals())
	else:
		return render(request, 'user.html',locals())



	#return HttpResponse(dC)
	


def resultpage(request):
	copy = request.build_absolute_uri()[0:-6]
	current = request.get_full_path()
	current = current[0:-6]
	event = Event.objects.get(randUrl=current)
	eventName = event.eventName

	dC = event.dayChosen
	dayChosen = dC.split(",",dC.count(","))
	while "" in dayChosen:
		dayChosen.remove("")
	tC = event.timeChosen
	timeChosen = tC.split(",",tC.count(","))
	while "" in timeChosen:
		timeChosen.remove("")
	
	options = []
	for h in timeChosen:
		for d in dayChosen:
			options.append(d + "_" + h)
	lo = len(options)

	results = Response.objects.filter(event=event)
	
	fT = []
	yourName = []
	freeTime = []
	for i in range(len(results)):
		yourName.append(results[i].yourName)
		f = results[i].freeTime
		freeTime.extend(f.split(",",f.count(",")))
		fT.append({results[i].yourName:f.split(",",f.count(","))})
		#fD.extend(f)


	# 計算各個時段出現幾次：

	#times = []
	#for t in fT:
	#	a = list(t.values())
	#	times.extend(a[0])
	
	counting = []
	for o in options:
		counting.append(freeTime.count(o))
	
	maxNum = max(counting)
	scaleRange = range(maxNum)
	reply = len(results)

	
	# 找出每個時段的人:

	ao = []
	do = []

	for o in options:
		p_in_o = []
		p_notin_o = []

		for p in yourName:
			r = Response.objects.get(yourName=p, event=event)  # 記得刪掉重複的名字！
			f = r.freeTime
			free = f.split(",",f.count(","))

			if o in free:
				p_in_o.append(p)
			else:
				p_notin_o.append(p)

			
			#for j in range(len(r)):
				#f = r[j].freeTime
				
		ao.append({o:p_in_o})
		do.append({o:p_notin_o})	

	lastDay = dayChosen[len(dayChosen)-1]

	ifDate = False
	num = "0123456789"
	for i in num:
		if i in dC:
			ifDate = True

	if ifDate == True:
		return render(request, 'result_trydate.html',locals())
	else:
		return render(request, 'result.html',locals())

	#return HttpResponse(do)

	# 分層設色done
	# 合併後debug continuing
	# 表單的提示訊息 使用者done 帳號? 事件notyet
	# 顯示填單的人
	# 連結關閉 notyet
	# 使用者名稱不重複done
	# 加入日期系統 第一頁done 第二頁done 第三頁done
	# 加入切換模式 notyet