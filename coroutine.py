#Consumer
def writeDB():
    print("DB conn Open")
    try:
        while True:
            record=yield
            print(f"[DB] consumer Save record {record}")
    except GeneratorExit:
        print("DB conn Close")

#Producer
def data_scraper(consumer):
    #data simulation
    fake_data=["Abhishek","Swapna","Vikramaditya"]

    for item in fake_data:
        print(f"[Scraper] producer found data: {item}")
        #Send data directly into the waiting consumer
        consumer.send(item)

cons=writeDB()
next(cons) # Prime it

data_scraper(cons) # run the producer

cons.close() # safely shut down the consumer