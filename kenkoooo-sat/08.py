from z3 import *

s = Solver()

v1 = Bool("1")
v2 = Bool("2")
v3 = Bool("3")
v4 = Bool("4")
v5 = Bool("5")
v6 = Bool("6")
v7 = Bool("7")
v8 = Bool("8")
v9 = Bool("9")
v10 = Bool("10")
v11 = Bool("11")
v12 = Bool("12")
v13 = Bool("13")
v14 = Bool("14")
v15 = Bool("15")
v16 = Bool("16")
v17 = Bool("17")
v18 = Bool("18")
v19 = Bool("19")
v20 = Bool("20")
v21 = Bool("21")
v22 = Bool("22")
v23 = Bool("23")
v24 = Bool("24")
v25 = Bool("25")
v26 = Bool("26")
v27 = Bool("27")
v28 = Bool("28")
v29 = Bool("29")
v30 = Bool("30")
v31 = Bool("31")
v32 = Bool("32")
v33 = Bool("33")
v34 = Bool("34")
v35 = Bool("35")
v36 = Bool("36")
v37 = Bool("37")
v38 = Bool("38")
v39 = Bool("39")
v40 = Bool("40")
v41 = Bool("41")
v42 = Bool("42")
v43 = Bool("43")
v44 = Bool("44")
v45 = Bool("45")
v46 = Bool("46")
v47 = Bool("47")
v48 = Bool("48")
v49 = Bool("49")
v50 = Bool("50")

s.add(Or(Not(v3), v36, v7))
s.add(Or(Not(v3), Not(v42), Not(v48)))
s.add(Or(Not(v49), Not(v47), Not(v41)))
s.add(Or(v8, Not(v40), v17))
s.add(Or(Not(v21), Not(v31), Not(v39)))
s.add(Or(v36, Not(v22), v49))
s.add(Or(v27, v38, v14))
s.add(Or(v15, Not(v18), v6))
s.add(Or(v6, v7, Not(v43)))
s.add(Or(v34, Not(v7), v23))
s.add(Or(v2, v14, Not(v13)))
s.add(Or(v2, v47, Not(v42)))
s.add(Or(Not(v33), Not(v35), v3))
s.add(Or(v44, v40, v49))
s.add(Or(v50, v36, v31))
s.add(Or(Not(v36), Not(v3), Not(v37)))
s.add(Or(v26, Not(v29), v43))
s.add(Or(v15, v29, Not(v45)))
s.add(Or(v24, Not(v11), v18))
s.add(Or(Not(v47), Not(v26), v6))
s.add(Or(Not(v50), Not(v33), Not(v10)))
s.add(Or(v32, v6, v16))
s.add(Or(Not(v34), v37, v41))
s.add(Or(v7, Not(v28), Not(v17)))
s.add(Or(Not(v44), v46, v19))
s.add(Or(v7, v22, Not(v48)))
s.add(Or(v3, v39, v34))
s.add(Or(v31, v46, Not(v43)))
s.add(Or(Not(v27), v32, v23))
s.add(Or(v37, Not(v50), Not(v18)))
s.add(Or(v20, v5, v11))
s.add(Or(Not(v45), Not(v24), v6))
s.add(Or(Not(v34), Not(v23), Not(v14)))
s.add(Or(Not(v22), v21, v20))
s.add(Or(Not(v17), v50, v24))
s.add(Or(Not(v25), Not(v24), Not(v27)))
s.add(Or(v3, v35, v21))
s.add(Or(Not(v26), v47, Not(v36)))
s.add(Or(Not(v28), Not(v45), v49))
s.add(Or(Not(v21), Not(v6), v12))
s.add(Or(Not(v17), Not(v15), Not(v39)))
s.add(Or(v41, v2, Not(v14)))
s.add(Or(v25, v36, Not(v23)))
s.add(Or(Not(v39), Not(v3), Not(v40)))
s.add(Or(v50, v20, v35))
s.add(Or(v27, v31, Not(v39)))
s.add(Or(v45, Not(v15), Not(v40)))
s.add(Or(v34, v50, v35))
s.add(Or(Not(v1), Not(v48), v12))
s.add(Or(v18, Not(v35), Not(v30)))
s.add(Or(v27, Not(v24), Not(v25)))
s.add(Or(Not(v4), Not(v33), Not(v12)))
s.add(Or(Not(v43), Not(v24), Not(v37)))
s.add(Or(Not(v37), v31, Not(v44)))
s.add(Or(Not(v9), Not(v38), v14))
s.add(Or(v33, Not(v16), v34))
s.add(Or(v4, Not(v35), Not(v5)))
s.add(Or(Not(v3), Not(v21), Not(v19)))
s.add(Or(Not(v35), Not(v36), Not(v29)))
s.add(Or(v7, Not(v43), v36))
s.add(Or(v30, v14, v41))
s.add(Or(Not(v35), Not(v24), Not(v7)))
s.add(Or(v35, Not(v42), v6))
s.add(Or(Not(v1), Not(v15), v39))
s.add(Or(v27, v49, Not(v16)))
s.add(Or(Not(v37), v49, Not(v10)))
s.add(Or(v50, Not(v46), Not(v3)))
s.add(Or(Not(v41), v20, v34))
s.add(Or(Not(v1), v23, v28))
s.add(Or(Not(v12), Not(v30), Not(v20)))
s.add(Or(Not(v24), v29, Not(v37)))
s.add(Or(v12, v5, Not(v44)))
s.add(Or(Not(v6), Not(v2), v48))
s.add(Or(Not(v2), Not(v49), Not(v43)))
s.add(Or(v1, Not(v50), v24))
s.add(Or(Not(v7), Not(v50), Not(v44)))
s.add(Or(Not(v41), v43, v4))
s.add(Or(v13, v15, Not(v11)))
s.add(Or(Not(v3), Not(v11), v23))
s.add(Or(v33, v48, v41))
s.add(Or(v9, v23, Not(v49)))
s.add(Or(Not(v43), v47, v1))
s.add(Or(Not(v40), v16, Not(v29)))
s.add(Or(v30, v19, v3))
s.add(Or(v19, Not(v34), v48))
s.add(Or(Not(v16), Not(v44), v14))
s.add(Or(v38, Not(v45), Not(v12)))
s.add(Or(Not(v4), Not(v14), Not(v31)))
s.add(Or(Not(v48), v35, Not(v1)))
s.add(Or(v45, Not(v13), v19))
s.add(Or(v9, v42, Not(v7)))
s.add(Or(Not(v1), Not(v15), v8))
s.add(Or(Not(v13), Not(v44), Not(v14)))
s.add(Or(Not(v43), Not(v37), Not(v31)))
s.add(Or(Not(v27), Not(v29), v47))
s.add(Or(v7, v4, v17))
s.add(Or(v7, v10, v35))
s.add(Or(Not(v25), v20, v17))
s.add(Or(v35, Not(v5), Not(v42)))
s.add(Or(Not(v50), v24, Not(v5)))
s.add(Or(Not(v21), Not(v26), v2))
s.add(Or(Not(v8), v45, Not(v21)))
s.add(Or(Not(v16), v33, v49))
s.add(Or(Not(v38), v6, v16))
s.add(Or(v5, v21, v37))
s.add(Or(v8, v38, v31))
s.add(Or(Not(v21), v33, v14))
s.add(Or(v20, v40, Not(v5)))
s.add(Or(Not(v29), Not(v9), v31))
s.add(Or(Not(v7), v42, Not(v22)))
s.add(Or(Not(v48), v8, v26))
s.add(Or(v48, Not(v38), v33))
s.add(Or(Not(v34), v49, v46))
s.add(Or(Not(v14), Not(v46), v25))
s.add(Or(Not(v46), v4, v18))
s.add(Or(v36, Not(v12), Not(v31)))
s.add(Or(v12, Not(v18), v14))
s.add(Or(Not(v7), v46, Not(v16)))
s.add(Or(v9, Not(v8), v7))
s.add(Or(v49, Not(v42), Not(v22)))
s.add(Or(v22, Not(v15), v38))
s.add(Or(v34, Not(v41), v47))
s.add(Or(v22, Not(v26), v32))
s.add(Or(Not(v25), Not(v45), Not(v21)))
s.add(Or(Not(v26), v32, Not(v11)))
s.add(Or(v15, v26, Not(v25)))
s.add(Or(Not(v1), v46, v25))
s.add(Or(Not(v14), Not(v31), v30))
s.add(Or(Not(v9), Not(v22), v12))
s.add(Or(Not(v18), v26, Not(v35)))
s.add(Or(Not(v16), Not(v32), Not(v21)))
s.add(Or(v31, Not(v49), Not(v21)))
s.add(Or(v11, v9, v41))
s.add(Or(Not(v13), Not(v30), v19))
s.add(Or(Not(v10), v4, v6))
s.add(Or(Not(v4), v3, Not(v22)))
s.add(Or(Not(v25), Not(v50), Not(v18)))
s.add(Or(Not(v40), v4, v9))
s.add(Or(v37, v20, v46))
s.add(Or(Not(v27), v22, Not(v29)))
s.add(Or(v34, v14, v3))
s.add(Or(v3, Not(v31), v20))
s.add(Or(Not(v50), v2, Not(v26)))
s.add(Or(v17, Not(v29), v38))
s.add(Or(Not(v49), v12, Not(v41)))
s.add(Or(v15, Not(v35), Not(v43)))
s.add(Or(Not(v22), Not(v23), Not(v49)))
s.add(Or(Not(v9), v33, v48))
s.add(Or(v26, v29, v35))
s.add(Or(v27, Not(v50), v37))
s.add(Or(Not(v7), v46, Not(v43)))
s.add(Or(Not(v46), Not(v37), Not(v8)))
s.add(Or(Not(v40), v36, Not(v24)))
s.add(Or(Not(v44), v46, v15))
s.add(Or(Not(v3), v36, Not(v16)))
s.add(Or(Not(v48), v9, v43))
s.add(Or(Not(v25), Not(v4), v44))
s.add(Or(Not(v22), v37, Not(v7)))
s.add(Or(Not(v31), Not(v17), Not(v22)))
s.add(Or(Not(v11), Not(v48), v17))
s.add(Or(v23, v34, Not(v28)))
s.add(Or(v23, Not(v48), Not(v39)))
s.add(Or(Not(v37), Not(v1), Not(v23)))
s.add(Or(Not(v19), v27, v14))
s.add(Or(Not(v22), v33, Not(v6)))
s.add(Or(Not(v6), Not(v32), Not(v26)))
s.add(Or(v18, Not(v20), Not(v46)))
s.add(Or(v43, v22, v27))
s.add(Or(Not(v13), v34, v49))
s.add(Or(Not(v35), Not(v46), v3))
s.add(Or(v32, v39, Not(v43)))
s.add(Or(v6, Not(v39), Not(v9)))
s.add(Or(v27, v39, Not(v16)))
s.add(Or(v25, Not(v17), Not(v15)))
s.add(Or(Not(v43), v27, v34))
s.add(Or(Not(v6), v49, v5))
s.add(Or(Not(v38), v11, v14))
s.add(Or(v40, Not(v38), v47))
s.add(Or(v37, Not(v14), v17))
s.add(Or(v39, v29, v36))
s.add(Or(Not(v39), Not(v28), v1))
s.add(Or(Not(v18), v14, Not(v16)))
s.add(Or(Not(v40), v50, v15))
s.add(Or(v37, Not(v42), v18))
s.add(Or(Not(v13), v31, v33))
s.add(Or(v2, Not(v42), v33))
s.add(Or(v8, Not(v3), Not(v22)))
s.add(Or(v1, v23, Not(v31)))
s.add(Or(Not(v20), Not(v45), v26))
s.add(Or(v42, v11, v49))
s.add(Or(v29, v11, Not(v43)))
s.add(Or(Not(v20), Not(v21), v30))
s.add(Or(v23, v45, Not(v35)))
s.add(Or(v38, Not(v30), Not(v14)))
s.add(Or(Not(v9), v48, Not(v29)))
s.add(Or(v11, Not(v18), Not(v23)))
s.add(Or(Not(v41), Not(v1), Not(v29)))
s.add(Or(v5, v41, v26))
s.add(Or(v44, Not(v30), Not(v7)))
s.add(Or(v38, Not(v6), Not(v41)))
s.add(Or(v46, v48, Not(v15)))
s.add(Or(Not(v18), Not(v10), Not(v47)))
s.add(Or(v38, v46, Not(v32)))
s.add(Or(Not(v32), v46, v12))
s.add(Or(v31, v40, v14))
s.add(Or(Not(v18), v2, v49))
s.add(Or(v28, Not(v38), v27))
s.add(Or(Not(v16), Not(v21), v14))
s.add(Or(Not(v29), v15, v12))
s.add(Or(v49, v34, v5))
s.add(Or(v14, v22, Not(v12)))
s.add(Or(v30, v33, v20))
s.add(Or(Not(v24), v22, v25))
s.add(Or(v4, Not(v48), Not(v23)))
s.add(Or(Not(v30), Not(v36), v9))
s.add(Or(v44, v12, Not(v35)))
s.add(Or(v38, v3, Not(v21)))
s.add(Or(Not(v11), v33, v49))


r = s.check()
if r == sat:
    print(s.model())
