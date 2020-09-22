# Usage python percFile.py
# to do:insert the patch names as arguments

fout=open('fperc','w')

f1='postProcessing/flowRatePatch(name=inlet_1)/4021/surfaceFieldValue.dat' 
f2="postProcessing/flowRatePatch(name=inlet_2)/4021/surfaceFieldValue.dat"
f3='postProcessing/flowRatePatch(name=Outlet)/4021/surfaceFieldValue.dat' 

f1=open(f1,'r')
f2=open(f2,'r')
f3=open(f3,'r')

data1 = f1.readlines()
data2 = f2.readlines()
data3 = f3.readlines()

lin = len(data1)

i=5 #skip the first 5 lines (Headers)

while i < lin:
	inlet_1=data1[i]
	inlet_2=data2[i]
	Outlet_=data3[i]
	
	inlet1=inlet_1.split( )
	inlet2=inlet_2.split( )
	Outlet=Outlet_.split( )
	it=float(inlet1[0])
	num1=float(inlet1[1])
	num2=float(inlet2[1])
	num3=float(Outlet[1])
	num=num1+num2+num3
	den=num3
	perc=num/den*100.0
	i=i+1
	fout.write(str(it)+'  '+str(perc)+'\n')

f1.close()
f2.close()
f3.close()
fout.close()
