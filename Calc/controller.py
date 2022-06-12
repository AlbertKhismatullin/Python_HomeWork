import UI.in_data as InD
import DataBase.keeper as DB
import Main_Logic.oper as ML
import UI.out_data as OD
import DataBase.logger as LG

def Click_Button():
    value_a, value_b = InD.indata()
    DB.save_data(value_a, value_b) 
    n,m = DB.return_data()
    result = ML.Summ(n,m)
    LG.log_data(f'Cумма чисел {n} и {m} равна {result}')
    OD.outdata(result)

