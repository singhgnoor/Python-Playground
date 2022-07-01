from time import time, sleep 

lst = ['this is good', 'this is python', 'python is not python sanke']

def searcher(str):
    a = [i for i in lst if str in i] 
    sleep(0.00123)
    return a


if __name__ == "__main__":
    print("Enter your search")
    str = input()
    intime = time()
    a = searcher(str)
    endtime = time()
    print(f"results in {intime-endtime} \n{a}")
    
    
