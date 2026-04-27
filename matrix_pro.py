def improve_matrix():
    import numpy as np
    r=int(input("Enter number of rows:"))
    c=int(input("Enter number of columns:"))
    l=[]
    a=[]
    if r!=c:
        print("Error , number of rows and columns are not equal")
    if r==c:
        for i in range(r):
            for f in range(c):
                ele=int(input("Enter element a{}{}:".format(i+1,f+1)))
                l.append(ele)
    for v in range(r):
        x=l[-1:-r-1:-1]
        x1=x[::-1]
        a.append(x1)
        for s in range(r):
            l.pop()
        nl=a[::-1]
    x=np.matrix(nl)
    print("click 1 to find the determinant of the matrix")
    print("click 2 to find the main diagonl of the matrix")
    print("click 3 to find the transpose of the matrix")
    print("click 4 to find the adjoint of the matrix")
    print("click 5 to find the inverse of the matrix")
    print("click 6 to skip")
    print("The matrix is:")
    print(x)
    while True:
        choice=int(input("Enter your choice in numbers only:"))
        if choice==1:
            det=np.linalg.det(x)
            deter=round(det,4)
            print("the determinant of the matrix is:")
            print(deter)
        if choice==2:
            mdiag=np.diag(x)
            print("The main diagonal of the matrix is:")
            print(mdiag)
        if choice==3:
            trans=np.transpose(x)
            print("The transpose of the matrix is:")
            print(trans)
        if choice==5:
            det=np.linalg.det(x)
            deter=round(det,4)
            if deter==0:
                print("It is a singular matrix and hence no inverse:")
            else:
                inv=np.linalg.inv(x)
                print("The inverse of the matrix is:")
                print(inv)
        if choice==4:
            #i need to learn more about this ,AI assisted
            n = x.shape[0]  
            minors = np.zeros((n,n))
            for i in range(n):
                for j in range(n):
                    submatrix=np.delete(x,i,axis=0)
                    submatrix=np.delete(submatrix,j,axis=1)
                    minors[i,j]=round(np.linalg.det(submatrix),5)
            cofactors = np.zeros((n,n))
            for i in range(n):
                for j in range(n):
                    cofactors[i,j] =((-1)**(i+j))*minors[i,j]
            adj=cofactors.T
            print("The adjoint of the matrix is:")
            print(adj)
        if choice==6:
            break
improve_matrix()
