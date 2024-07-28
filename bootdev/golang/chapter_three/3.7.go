package main

func monthlyBillIncrease(costPerSend, numLastMonth, numThisMonth int) float64 {
	lastMonthBill := getBillForMonth(lastMonthBill, costPerSend, numLastMonth)
	thisMonthBill := getBillForMonth(thisMonthBill, costPerSend, numThisMonth)
	
	return thisMonthBill - lastMonthBill
}



func getBillForMonth(bill, costPerSend, messagesSent int) float64{
	bill := costPerSend * messagesSent
	return bill
}
