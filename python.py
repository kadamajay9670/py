# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")

# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))

# class I:
#     def __init__(self):
#         self.s ='abc'
#         self.i= 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i== len(self.s):
#             raise StopIteration
#         v= self.s[self.i]
#         self.i+=1
#         return v
#
# for x in I():
#     print(x,end='')

#
# class A:
#     A=1
#     def __init__(self):
#         self.a=0
#
# print(hasattr(A,'a'))


# x="\\"
# print(len(x))



# class A:
#     pass
# class B(A):
#     pass
#
# class C(B,A):
#     pass
# print(issubclass(A,C))
# t=(1,2,3,4,5)
# print(t[-1])





# i=4
# while i>0:
#     i-=2
#     print("*")
#     if i==2:
#         break
# else:
#     print("*")



# class A:
#     A=1
#     def __init__(self,v=2):
#         self.v=v+A.A
#         A.A+=1
#     def set(self,v):
#         self.v+=v
#         A.A+=1
#         return
# a=A()
# a.set(2)
# print(a.v)
#
#




#
# def fun(d,k,v):
#     d[k]=v
# dc={}
#
# print(fun(dc,'1','v'))


# check this concept
# d={}
# d['2']=[1,2]
# d['1']=[3,4]
#
# for x in d.keys():
#     print(d[x][1])



# it is very important
# print(len((1,)))





#
# def fun(x):
#     return 1 if x%2 !=0 else 2
#
# print(fun(fun(1)))





# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A,B):
#     pass
# # x=X()
# # z=Z()
# print(issubclass(C,A), issubclass(C,B))
# # print(isinstance(x,Z), isinstance(z,X))



# very important
# def a(x):
#     def b():
#         return x+x
#     return b
#
# x=a('x')
# y=a('')
# print(x()+y())





# imp
# x=16
# while x>0:
#     print("*")
#     x//=2






# imp for exam
# i=4
# while i>0:
#     i-=2
#     print("*")
#     if i==2:
#         break
# else:
#     print("*")






# exam que
# lt=[1,2,3,4]
# lt=list(map(lambda x: 2 * x ,1 ))
# print(lt)




# str='abcdef'
# def fun(s):
#     del s[2]
#     return s
# print(fun(str))

#
# class A:
#     def __init__(self,name):
#         self.name=name
# a=A("class")
# print(a)



# hasattr
#
# class A:
#     A=1
#     def __init__(self):
#         self.a=0
# print(hasattr(A,"A"))






#
# def I(n):
#     s=''
#     for i in range(n):
#         s+='*'
#         yield s
# for x in I(3):
#     print(x)

#
#
# print(len([i for i in range(0,-2)]))



#
# class A:
#     def __init__(self):
#         pass
#     def f(self):
#         return 1
#     def g():
#         return self.f()
# a=A()
# print(a.g())



# d= {1:0,2:1,3:2,0:1}
# x=0
# # for y in range(len(d)):
# #     x=d[x]
# print(x)








#
# class A:
#     def __init__(self,v):
#         self._a = v+1
# a=A(0)
# print(a._a)














print("my", "name is",sep="_",end"*")
print("monty", "python", sep="?", end="&")
