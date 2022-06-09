import DataBase.View as V
import DataBase.format as Ft
import DataBase.keeper as K
import Search.search as S
import Search.fnder as F

def add_db():
    b = V.new_entry()
    f = Ft.choose_format()
    K.keeper_dt(b,f)

def srch_smbd(m):
    if m == 3:
        nm=''
        S.search_result(F.srch_srnm(nm))
    else:
        nm = S.search_surname()
        S.search_result(F.srch_srnm(nm))

