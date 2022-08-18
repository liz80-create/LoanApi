import pandas as pd
import json

class Loan:
    def __init__(self,data):
        self.data=data

    def duration(self):
        i=0
        self.input_rec = self.data[i]
        self.loan_amount=self.input_rec['loan_amount']
        self.term_year=self.input_rec['term_year']
        self.interest=self.input_rec['interest']
        self.payment_type=self.input_rec['payment_type']

        return self.loan_amount,self.term_year,self.interest,self.payment_type
    
    def determineduration(self):
        if self.payment_type=='Monthly':
            self.rate=self.interest/(12*100)
            self.term=self.term_year*12
        elif self.payment_type=='Daily':
            self.rate=self.interest/(365*100)
            self.term=self.term_year*365
        elif self.payment_type=='Weekly':
            self.rate=self.interest/(52*100)
            self.term=self.term_year*52
        elif self.payment_type=='Biweekly':
            self.rate=self.interest/(26*100)
            self.term=self.term_year*26
        else:
            pass
        return self.rate,self.term
        
    def display_details(self):
        
        self.emi = self.loan_amount * self.rate * ((1+self.rate)**self.term)/((1+self.rate)**self.term - 1)
        no_of_total_payments=self.term
        total_payment_amt=no_of_total_payments*self.emi
        total_interest=total_payment_amt-self.loan_amount
        '''print("EMI = ", self.emi)
        print(f"total of {no_of_total_payments} payments = {total_payment_amt}")
        print("Total Interest=",total_interest)'''
        self.detailsdict={"EMI":self.emi,"NumberOfPayments":no_of_total_payments,"TotalPayment":total_payment_amt,"TotalInterest":total_interest}
        return self.detailsdict

    def cal(self,loan_amount,rate,emi):
        interest=self.loan_amount*self.rate
        princi=self.emi-interest
        self.loan_amount=self.loan_amount-princi
        return {"Balance":round(self.loan_amount,2),"Principal":round(princi,2),"Interest":round(interest,2)}

    def amortizationtab(self):
        self.duration()
        self.determineduration()
        self.display_details()
        frames=[{"Balance":self.loan_amount,"Principal":0,"Interest":0}]
        while self.loan_amount>0:
            frame=dict(self.cal(self.loan_amount,self.rate,self.emi))
            #print(frame['Balance'])
            self.loan_amount=frame['Balance']
            self.term=self.term-1
            frames.append(frame)
        finaldict={"Details":self.detailsdict,"loan_chedule":frames}
        jsondata=json.dumps(finaldict, indent = 4)
        return jsondata
'''
        #table=pd.DataFrame(data=frames,columns=['Balance',
         #                                     'Principal',
        #                                    'Interest']).rename_axis('Payment Number')
        #jsondata=table.to_json(orient='records')
        #return jsondata

input_data=[
    {
        "loan_amount": 100000,
        "term_year": 1,
        "interest": 6,
        "payment_type": "Monthly"
    }
]
obj=Loan(input_data)
data=Loan.amortizationtab(obj)
print(data)

'''

        
        