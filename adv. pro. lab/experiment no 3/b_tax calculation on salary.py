#for income = 250000 no tax,,, for income in bet 250000-500000 tax will be 5%,, 
# for 500000-800000 tax 15%,,for above than 8lakh tax 30%

income=int(input('enter your total income:'));
if income<=250000:
     tax=income*(0/100);
     print('tax amout=',tax);
elif income>250000 and income<=500000:
     gross=income-250000;
     tax=gross*(5/100);
     print('tax amount=',tax)
elif income>500000 and income<=800000:
     gross=income-250000;
     gross1=gross-250000;
     tax1=250000*(5/100)
     tax2=gross1*(15/100)
     tax=tax1+tax2;
     print('tax amount=',tax)
else:
     gross=income-250000;
     gross1=gross-250000;
     gross2=gross1-300000;
     tax1 = 250000 * (5 / 100)
     tax2 = 300000 * (15 / 100)
     tax3 = gross2 * (30 /100)
     tax=(tax1+tax2+tax3)
     print('tax amount=', tax);

