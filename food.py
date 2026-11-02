RESTAURANTS = [
    ("Mango Rice", 4.2,25),
    ("Pad Thai House", 4.8,40),
    ("Chicken Rice",4.6,15),
    ("Som Tam Corner",4.6,25),
    ("Boat Noodles",4.8,30)
]

def by_rating(RESTAURANTS):
    return (RESTAURANTS[1])


def by_time(RESTAURANTS):
     return (RESTAURANTS[2])
    
def main():
    option = input("Do want to sort by rating(r) or time(t): ").lower()

    if option not in ["r","t","time","rating"] or option == "":
        print("Unknown Option")
        exit()
    elif option == "r" or option == "rating":
        for i, (name, rating, minutes) in enumerate(sorted(RESTAURANTS, key=by_rating, reverse=True),start=1):
                print(f"{i}. {name}, {rating} stars, {minutes} min")
    else:
        for i, (name, rating, minutes) in enumerate(sorted(RESTAURANTS, key=by_time,),start =1):
                print(f"{i}. {name}, {rating} stars, {minutes} min")

if __name__=="__main__":
     main()