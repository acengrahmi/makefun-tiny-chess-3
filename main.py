import json,os,urllib.request as U
V=[0,100,320,330,500,900,0]
ND=[31,33,14,18,-14,-18,-31,-33]
BS=[15,17,-15,-17];RD=[16,1,-16,-1];KD=BS+RD
CM={0:13,7:14,4:12,112:7,119:11,116:3}
D2=(0,0,ND,BS,RD,KD,KD)
SQ=[i for i in range(128)if not i&136]
MF=[0,1,2,3,3,2,1,0]
TB=[0]*1920
for i in SQ:
 f=MF[i&7];r=i>>4;c=f+MF[r]
 for u,v in enumerate((100+r*7,302+c*7,330,500,900,c*3),1):TB[i*15+u]=v;TB[(i^112)*15+u+8]=-v
def ATK(b,sq,by):
 for ds,tp,sl in((ND,2,0),(KD,6,0),(BS,3,1),(RD,4,1),((15,17)if by else(-15,-17),1,0)):
  for d in ds:
   x=sq
   while 1:
    x+=d
    if x&136:break
    p=b[x]
    if p:
     if p-8*by==tp or p-8*by==5 and sl:return 1
     break
    if not sl:break
 return 0
def GEN(P,co):
 b,s,c,ep=P;ms=[];ap=ms.append
 for i in SQ:
  p=b[i]
  if not p or p>>3!=s:continue
  u=p&7
  if u==1:
   d=16-32*s;one=i+d
   def AD(t):[ap(i|t<<7|pr<<14)for pr in(5,4,3,2)]if t>>4 in(0,7)else ap(i|t<<7)
   if not b[one]:AD(one)if one>>4 in(0,7)else co or ap(i|one<<7)or(i>>4==1+5*s and not b[i+2*d]and ap(i|(i+2*d)<<7))
   for df in(-1,1):
    t=one+df
    if t&136:continue
    if b[t]and b[t]>>3!=s:AD(t)
    elif t==ep:ap(i|t<<7)
  else:
   for d in D2[u]:
    t=i
    while 1:
     t+=d
     if t&136:break
     q=b[t]
     if q and q>>3!=s or not q and not co:ap(i|t<<7)
     if q:break
     if u in(2,6):break
   if u==6 and not co and i==4+112*s:
    for sg,bit,rf in((1,1,i+3),(-1,2,i-4)):
     if c&(bit<<2*s)and b[rf]==4+8*s and all(not b[i+sg*x]for x in(1,2,3)[:2+(sg<0)])and all(not ATK(b,i+sg*x,1-s)for x in(0,1,2)):ap(i|(i+2*sg)<<7)
 return ms
def MK(P,m):
 b,s,c,ep=P
 f=m&127;t=(m>>7)&127;pr=m>>14
 b=b.copy();p=b[f]
 if p&7==1 and t==ep and not b[t]:b[t-16+32*s]=0
 b[f]=0;b[t]=pr+8*s if pr else p
 if p&7==6 and abs(t-f)==2:
  u=t<f;b[t-1+2*u]=b[t+1-3*u];b[t+1-3*u]=0
 return(b,1-s,c&CM.get(f,15)&CM.get(t,15),t-16+32*s if p&7==1 and abs(t-f)==32 else-1)
def PF(s):
 q=s.split();b=[0]*128;r=8;e=q[3]
 for row in q[0].split('/'):
  r-=1;f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    u='PNBRQK'.find(ch.upper())+1;b[r*16+f]=u+8*(ch.islower());f+=1
 cc=sum(1<<j for j,ch in enumerate('KQkq')if ch in q[2])
 return(b,q[1]!='w',cc,-1 if e=='-'else ord(e[0])+16*ord(e[1])-881)
def PK(P):return(bytes(P[0]),P[1],P[2],P[3])
def FM(P,u):return[m for m in GEN(P,0)if UC(m)==u][0]
def UC(m):return f"{chr(97+m%8)}{1+m//16%8}{chr(97+m//128%8)}{1+m//2048%8}{'..nbrq'[m>>14]if m>>14 else''}"
def EV(b):return sum(TB[i*15+b[i]]for i in SQ if b[i])
TT={};SEEN=set();N=BD=0;RB=[0];I=9**9;E=ValueError
def IL(Q,s):return ATK(Q[0],Q[0].index(6+8*s),1-s)
def S(P,d,a,be,ply):
 global N;N+=1
 if N>BD:raise E
 b,s,c,ep=P;ic=ATK(b,b.index(6+8*s),1-s);tm=0;oa=a
 if d>0:
  key=PK(P)
  if ply and key in SEEN:return 0
  e=TT.get(key)
  if e:
   tm=e[3]
   if ply and e[0]>=d and(e[2]>=be if e[1]>0 else e[2]<=a if e[1]<0 else 1):return e[2]
 if d<=0 and not ic:
  best=(1,-1)[s]*EV(b)
  if best>=be:return best
  if best>a:a=best
  ms=GEN(P,1)
 else:
  best=-I;ms=GEN(P,0)
 ms.sort(key=lambda m:((m==tm)<<28)+(V[b[t]&7]*32-V[b[m&127]&7]+9 if b[(t:=(m>>7)&127)]else 0),reverse=True);lg=0;bm=0
 for m in ms:
  Q=MK(P,m)
  if IL(Q,s):continue
  lg+=1
  dd=d-1-(d>2 and lg>4 and not b[(m>>7)&127]and m>>14<1 and ic<1)
  sc=-S(Q,dd,-a-1,-a,ply+1)if lg>1 else-S(Q,d-1,-be,-a,ply+1)
  if lg>1 and a<sc<be:sc=-S(Q,d-1,-be,-a,ply+1)
  if sc>best:best,bm=sc,m
  if sc>a:a=sc
  if a>=be:break
 if not lg:return best if d<=0 and not ic else(ply-100000 if ic else 0)
 if ply<1:RB[0]=bm
 if d>0:TT[key]=(d,(best>=be)-(best<=oa),best,bm)
 return best
EU=os.getenv('MAKEFUN_ENV_URL')
def POST(p,b):return json.load(U.urlopen(EU+p,json.dumps(b).encode()))
while(g:=POST('/game',{}))['status']>'e':
 while g['status']=='your_move':
  P=PF(g['start_fen']);SEEN={PK(P)}
  for u in g['moves']:
   P=MK(P,FM(P,u));SEEN.add(PK(P))
  ms=[m for m in GEN(P,0)if not IL(MK(P,m),P[1])]
  mv=ms[0]
  if len(ms)>1:
   TT.clear();N=0;RB[0]=mv;BD=90000+30000*(len(g['moves'])>=20)
   for d in range(39):
    try:S(P,d+1,-I,I,0);mv=RB[0]
    except E:break
  g=POST('/move',{'game':g['game'],'move':UC(mv)})
