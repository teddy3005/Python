class product(object):
    def __init__(self, price,item_name,weight,brand):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.status="for sale"

    def sell(self):
        self.status="sold"
        return self

    def addTax(self,tax):
        self.price+=tax*self.price
        return self
        

    def returnProd(self,reason):
        if reason=="defective":
            self.price=0
            print "item has been returned"
        
        elif reason=="returned in box":
            self.status="sale"
        
        elif reason=="open box":
            self.status="used"
            self.price*=.8
        return self

    def displayInfo(self):
        print "price",self.price
        print "item name",self.item_name     
        print "weight", self.weight    
        print "brand",self.brand
        print "status",self.status
        

item_1=product(1,"apples","12oz","jeep")
#item_1.sell().addTax(.08).displayInfo()

item_2=product(200,"thing","10oz","fendi")
item_2.sell().addTax(.15).returnProd("defective").displayInfo()
