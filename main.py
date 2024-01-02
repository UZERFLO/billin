from flask import *
import csv
app = Flask(__name__)
@app.route('/')
def input():
    return render_template('pmet.html')
global x
@app.route('/pop', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        global x
        x = request.form['TAN']
        f = []
        w = []
        g = []
        z = []

        with open('//mani5/User-5/VIJI 2023/New folder/TDS Bills 2022 onwards.csv', 'r') as a:
            r = csv.reader(a)
            next(r)
            next(r)
            next(r)
            next(r)
            f = next(r)
            for i in r:
                w.append(i)
        with open('//mani5/User-5/VIJI 2023/New folder/TDS BIlls old cases.csv', 'r') as b:
            s = csv.reader(b)
            g = next(s)
            for i in s:
                z.append(i)
        wz=z+w
        print(" ANNEXURE A 2022 ONWARDS  \n")
        q=0
        za=0
        pe=0
        qu=0
        zau=0
        peu=0
        for i in f:
            print(i, end=" ")
        print("\n")
        for i in wz:
            if x in i:
                sa=i
            if len(i)!=0:
                if i[22]!='' and x in i:
                   q+=int(i[22])
                if i[23] != '' and x in i:
                   za += int(i[23])
            if x in i:
                for j in i:
                    if j != "":
                        print(j, end=" ")
                print("\n")
        pe=q-za
        return render_template("result_data.html",wz=wz,x=x,f=f,w=w,g=g,z=z,q=q,za=za,pe=pe,sa=sa)
@app.route('/pdf', methods=['GET', 'POST'])
def ouput():
    if request.method == 'POST':
        qw = request.form['qw']
        dt = request.form['dt']
        md = request.form['md']
        bn = request.form['bn']
        f = []
        w = []
        g = []
        z = []
        with open('//mani5/User-5/VIJI 2023/New folder/TDS Bills 2022 onwards.csv', 'r') as a:
            r = csv.reader(a)
            f = next(r)
            for i in r:
                w.append(i)
        with open('//mani5/User-5/VIJI 2023/New folder/TDS BIlls old cases.csv', 'r') as b:
            s = csv.reader(b)
            g = next(s)
            for i in s:
                z.append(i)
        
        with open('//mani5/User-5/VIJI 2023/New folder/TDS Bills 2022 onwards.csv', 'w') as b:
            k=csv.writer(b)
            k.writerow(f)
            se=0
            for i in w:
                if x in i:
                    sa=i
                if len(i)!=0:
                    if i[22]==qw and i[23]=='' and i[20]==bn and x in i and se==0:
                        i[23]=qw
                        i[31]="*"
                        se=1
                        k.writerow(i)
                    else:
                        k.writerow(i)
                else:
                    k.writerow(i)

            a = {'0':'ZERO','1':'ONE','2':'TWO','3':'THREE','4':'FOUR','5':'FIVE','6':'SIX',\
	    '7':'SEVEN','8':'EIGHT','9':'NINE','10':'TEN','11':'ELEVEN','12':'TWELVE',\
	    '13':'THIRTEEN','14':'FOURTEEN','15':'FIFTEEN','16':'SIXTEEN','17':'SEVENTEEN',\
	    '18':'EIGHTEEN','19':'NINETEEN','20':'TWENTY','30':'THIRTY','40':'FORTY',\
	    '50':'FIFTY','60':'SIXTY','70':'SEVENTY','80':'EIGHTY','90':'NINETY','100':'HUNDRED','1000':'THOUSAND'}
            n = qw
            l = len(n)
            s=''
            if l == 1:
                s = a[n]
            elif l == 2:
                if n < '21':
                    s = a[n]
                else:
                    s = a[n[0]+'0'] + " " + a[n[1]]
            elif l == 3:
                if n == '100':
                    s = a[n]
                elif n[1]==0:
                     if n[2]==0:
                         s = a[n[0]] + " HUNDRED "
                     else:
                         s = a[n[0]] + " HUNDRED " + "AND " + a[n[2]]
                else:
                    s = a[n[0]] + " HUNDRED " + "AND " + a[n[1]+'0'] + " " + a[n[2]]
            elif l == 4:
                if n == '1000':
                    s = a[n]
                elif n[1] == 0:
                    if n[2] == 0:
                        s = a[n[0]] + " THOUSAND " + "AND " + a[n[3]]
                    else:
                        s = a[n[0]] + " THOUSAND " + "AND " + a[n[2]+'0'] + " " + a[n[3]]
                elif n[2]==0:
                    if n[3]==0:
                        s = a[n[0]] + " THOUSAND " + a[n[1]] + " HUNDRED "
                    else:
                        s = a[n[0]] + " THOUSAND " + a[n[1]] + " HUNDRED " + "AND " + a[n[2]]
                else:
                    s = a[n[0]] + " THOUSAND " + a[n[1]] + " HUNDRED " + "AND " + a[n[2]+'0'] + " " + a[n[3]]
            else:
                if n[0:2] < '21':
                    s = a[n[0:2]] + " THOUSAND " + a[n[2]] + " HUNDRED " + "AND " + a[n[3]+'0'] + " " + a[n[4]]
                elif n[2] == 0:
                    if n[3] == 0:
                        s = a[n[0]+'0'] + " " + a[n[1]] + " THOUSAND " + "AND " + a[n[4]]
                    else:
                        s = a[n[0]+'0'] + " " + a[n[1]] + " THOUSAND " + "AND " + a[n[3]+'0'] + " " + a[n[4]]
                elif n[2]==0:
                    if n[3]==0:
                        s = a[n[0]+'0'] + " " + a[n[1]] + " THOUSAND " + a[n[2]] + " HUNDRED "
                        if n[4]==0:
                            s = a[n[0]+'0'] + " " + a[n[1]] + " THOUSAND "
                    else:
                        s = a[n[0]+'0'] + " " + a[n[1]] + " THOUSAND " + a[n[2]] + " HUNDRED " + "AND " + a[n[3]]
                else:
                    s = a[n[0]+'0'] + " " + a[n[1]] + " THOUSAND " + a[n[2]] + " HUNDRED " + "AND " + a[n[3]+'0'] + " " + a[n[4]]
	    


        return render_template('pdf.html',qw=qw,dt=dt,md=md,w=w,sa=sa,bn=bn, s = s)
    else:
        qw=request.form['qw']
        return render_template('pdf.html', qw=qw)
@app.route('/view', methods=['GET', 'POST'])
def v():
    if request.method == 'POST':
        bn = request.form.getall('bn')
        return render_template('view.html',bn=bn)
    else:
        return render_template('view.html')
if __name__ == '__main__':
    app.run()
f=[]
w=[]
g=[]
z=[]
with open('//mani5/User-5/VIJI 2023/New folder/TDS Bills 2022 onwards.csv','r') as a:
    r=csv.reader(a)
    f=next(r)
    for i in r:
        w.append(i)
with open('//mani5/User-5/VIJI 2023/New folder/TDS BIlls old cases.csv','r') as b:
    s = csv.reader(b)
    g = next(s)
    for i in s:
        z.append(i)
print(" ANNEXURE A 2022 ONWARDS  \n")
for i in f:
    print(i, end = " ")
print("\n")
for i in w:
    if x in i:
        for j in i:
            if j != "":
                print(j, end = " ")
        print("\n")
print(" OLD CASES  \n")
for i in g:
    print(i, end = " ")
print("\n")
for i in z:
    if x in i:
        for j in i:
            if j != "":
                print(j, end = " ")
        print("\n")